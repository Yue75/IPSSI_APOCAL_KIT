#!/usr/bin/env python3
"""Benchmark multi-model LLM local with Ollama.

The script compares several models with the same prompt, records latency,
structural quiz quality, disk footprint and a composite score, then writes one
folder per model under ``scripts/migration/``.
"""

from __future__ import annotations

import json
import re
import statistics
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path

OLLAMA_URL_GEN = "http://localhost:11434/api/generate"
OLLAMA_URL_TAGS = "http://localhost:11434/api/tags"

MODELS = ["llama3.1:8b", "llama3.2:3b", "phi3:mini"]
ROOT_DIR = Path(__file__).resolve().parent
COURS_PATH = ROOT_DIR / "cours_reference.txt"
EXPORT_PATH = ROOT_DIR / "benchmark_resultats.md"
MIGRATION_DIR = ROOT_DIR / "migration"

RUNS_LATENCE = 5
RUNS_QUALITE = 2
SEUIL_P95 = 15

POIDS = {"latence": 0.40, "qualite": 0.40, "ressources": 0.20}
BENCHMARK_REFERENCE = "composite"
REPO_ROOT = ROOT_DIR.parent

PROMPT_TEMPLATE = """Tu es un generateur de quiz pedagogique.
A partir du cours ci-dessous, genere EXACTEMENT 10 questions a choix multiples.
Reponds UNIQUEMENT par un tableau JSON valide, sans texte autour, au format :
[
  {{
    "title": "...",
    "source_text": "...",
    "questions": [
      {{"prompt": "...", "options": ["...", "...", "...", "..."], "correct_index": 0}}
    ]
  }}
]
La liste JSON doit contenir un seul objet.
Le champ "questions" doit contenir exactement 10 questions.
Chaque question doit avoir exactement 4 options.
Le champ "correct_index" doit etre un entier entre 0 et 3.

COURS :
{cours}
"""


@dataclass
class ModelResult:
    model: str
    slug: str
    p50: float | None
    p95: float | None
    quality_auto_10: float | None
    disk_go: float | None
    composite_100: float | None
    recap_path: Path
    quiz_path: Path


def ollama_generate(model: str, prompt: str) -> tuple[str, float]:
    payload = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.4},
            "format": "json",
        },
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(
        OLLAMA_URL_GEN,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    start = time.perf_counter()
    with urllib.request.urlopen(request, timeout=600) as response:
        data = json.loads(response.read())
    return data.get("response", ""), time.perf_counter() - start


def ollama_taille_go(model: str) -> float | None:
    try:
        with urllib.request.urlopen(OLLAMA_URL_TAGS, timeout=30) as response:
            tags = json.loads(response.read()).get("models", [])
    except Exception:
        return None

    for tag in tags:
        if tag.get("name") == model or tag.get("name", "").startswith(model):
            return round(tag.get("size", 0) / 1e9, 2)
    return None


def percentile(values: list[float], p: float) -> float:
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    k = (len(ordered) - 1) * p
    lower = int(k)
    upper = min(lower + 1, len(ordered) - 1)
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (k - lower)


def normaliser(valeurs: dict[str, float | None], plus_petit_est_mieux: bool) -> dict[str, float]:
    nums = [v for v in valeurs.values() if v is not None]
    if not nums:
        return {k: 0.0 for k in valeurs}

    lo, hi = min(nums), max(nums)
    out: dict[str, float] = {}
    for key, value in valeurs.items():
        if value is None:
            out[key] = 0.0
        elif hi == lo:
            out[key] = 1.0
        else:
            scaled = (value - lo) / (hi - lo)
            out[key] = 1.0 - scaled if plus_petit_est_mieux else scaled
    return out


def sanitize_model_name(model: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", model.lower()).strip("-")
    return slug or "model"


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def parse_quiz_payload(text: str):
    stripped = text.strip()
    if not stripped:
        return None

    try:
        return json.loads(stripped)
    except Exception:
        pass

    for pattern in (r"\[[\s\S]*\]", r"\{[\s\S]*\}"):
        match = re.search(pattern, stripped)
        if match:
            try:
                return json.loads(match.group(0))
            except Exception:
                continue
    return None


def _quiz_from_payload(payload):
    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict):
                return item
        return None
    if isinstance(payload, dict):
        return payload
    return None


def _question_items(payload) -> list[dict]:
    quiz = _quiz_from_payload(payload)
    if not quiz:
        return []
    questions = quiz.get("questions", [])
    if not isinstance(questions, list):
        return []
    return [item for item in questions if isinstance(item, dict)]


def _normalize_question(question: dict) -> dict:
    options = question.get("options", [])
    if not isinstance(options, list):
        options = []
    normalized_options = [str(option) for option in options[:4]]
    while len(normalized_options) < 4:
        normalized_options.append("")

    correct_index = question.get("correct_index")
    if not isinstance(correct_index, int) or not 0 <= correct_index <= 3:
        correct_index = 0

    return {
        "prompt": str(question.get("prompt") or question.get("question") or "").strip(),
        "options": normalized_options,
        "correct_index": correct_index,
    }


def normalize_quiz_payload(payload, *, model: str, source_text: str) -> list[dict]:
    quiz = _quiz_from_payload(payload) or {}
    raw_questions = quiz.get("questions", [])
    if not isinstance(raw_questions, list):
        raw_questions = []

    normalized_questions = [
        _normalize_question(question)
        for question in raw_questions
        if isinstance(question, dict)
    ]

    if not normalized_questions and isinstance(payload, list):
        normalized_questions = [
            _normalize_question(question)
            for question in payload
            if isinstance(question, dict)
        ]

    title = str(quiz.get("title") or f"Benchmark LLM - {model}")
    source = str(quiz.get("source_text") or source_text)

    return [
        {
            "title": title,
            "source_text": source,
            "questions": normalized_questions[:10],
        }
    ]


def score_quiz(payload) -> float:
    quiz = _quiz_from_payload(payload)
    if not quiz:
        return 0.0

    total = 4
    points = 0.0

    if str(quiz.get("title", "")).strip():
        points += 1.0

    if str(quiz.get("source_text", "")).strip():
        points += 1.0

    questions = _question_items(payload)
    if len(questions) == 10:
        points += 1.0

    structure_ok = 0
    for question in questions:
        normalized = _normalize_question(question)
        options = normalized["options"]
        if normalized["prompt"] and len(options) == 4 and 0 <= normalized["correct_index"] <= 3:
            structure_ok += 1

    if questions:
        points += structure_ok / len(questions)

    return round(points / total * 10, 1)


def build_prompt(cours: str) -> str:
    return PROMPT_TEMPLATE.format(cours=cours)


def write_model_artifacts(
    model_dir: Path,
    payload,
    model: str,
    source_path: Path,
    source_text: str,
    quality_score: float,
    p50: float | None,
    p95: float | None,
    disk_go: float | None,
    composite_100: float | None,
) -> tuple[Path, Path]:
    model_dir.mkdir(parents=True, exist_ok=True)

    quiz_path = model_dir / "generated_quizz.json"
    recap_path = model_dir / "recapitulatif.md"
    normalized_payload = normalize_quiz_payload(payload, model=model, source_text=source_text)

    with quiz_path.open("w", encoding="utf-8") as fh:
        json.dump(normalized_payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    recap_lines = [
        f"# Recapitulatif benchmark - {model}",
        "",
        f"- Cours de reference : `{display_path(source_path)}`",
        f"- Latence p50 : {p50:.2f} s" if p50 is not None else "- Latence p50 : n/a",
        f"- Latence p95 : {p95:.2f} s" if p95 is not None else "- Latence p95 : n/a",
        f"- Qualite automatique : {quality_score:.1f} / 10",
        f"- Ressources disque : {disk_go:.2f} Go" if disk_go is not None else "- Ressources disque : n/a",
        f"- Score composite : {composite_100:.1f} / 100"
        if composite_100 is not None
        else "- Score composite : n/a",
        f"- Dossier de sortie : `{display_path(model_dir)}`",
        f"- Fichier quiz : `{quiz_path.name}`",
    ]
    recap_path.write_text("\n".join(recap_lines) + "\n", encoding="utf-8")
    return recap_path, quiz_path


def build_composite(results: list[ModelResult]) -> None:
    p95_values = {result.model: result.p95 for result in results}
    quality_values = {result.model: result.quality_auto_10 for result in results}
    disk_values = {result.model: result.disk_go for result in results}

    normalized_latency = normaliser(p95_values, plus_petit_est_mieux=True)
    normalized_quality = normaliser(quality_values, plus_petit_est_mieux=False)
    normalized_disk = normaliser(disk_values, plus_petit_est_mieux=True)

    for result in results:
        result.composite_100 = round(
            (
                POIDS["latence"] * normalized_latency.get(result.model, 0.0)
                + POIDS["qualite"] * normalized_quality.get(result.model, 0.0)
                + POIDS["ressources"] * normalized_disk.get(result.model, 0.0)
            )
            * 100,
            1,
        )


def write_summary_file(cours_path: Path, results: list[ModelResult]) -> None:
    lines = [
        "# Resultats du benchmark LLM",
        "",
        f"- Cours de reference : `{display_path(cours_path)}`",
        f"- Runs latence : {RUNS_LATENCE}",
        f"- Runs qualite : {RUNS_QUALITE}",
        f"- Seuil p95 : {SEUIL_P95} s",
        f"- Score composite : {POIDS}",
        f"- Benchmark de reference : `{BENCHMARK_REFERENCE}`",
        "",
        "## Synthese",
        "",
        "| Modele | p50 (s) | p95 (s) | Qualite auto /10 | Ressources (Go) | Composite /100 | Dossier |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]

    for result in results:
        lines.append(
            "| {model} | {p50} | {p95} | {quality} | {disk} | {composite} | `{dir}` |".format(
                model=result.model,
                p50=f"{result.p50:.2f}" if result.p50 is not None else "-",
                p95=f"{result.p95:.2f}" if result.p95 is not None else "-",
                quality=f"{result.quality_auto_10:.1f}",
                disk=f"{result.disk_go:.2f}" if result.disk_go is not None else "-",
                composite=f"{result.composite_100:.1f}" if result.composite_100 is not None else "-",
                dir=f"scripts/migration/{result.slug}",
            )
        )

    lines.extend(
        [
            "",
            "## Note",
            "",
            "Les fichiers generes par modele sont stockes dans `scripts/migration/<modele>/`.",
            "Chaque dossier contient `recapitulatif.md` et `generated_quizz.json`.",
            "",
        ]
    )
    EXPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    try:
        cours = COURS_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Erreur: cree d'abord {COURS_PATH}")
        return 1

    prompt = build_prompt(cours)
    results: list[ModelResult] = []
    payloads: dict[str, object] = {}

    for model in MODELS:
        latency_runs: list[float] = []
        quality_runs: list[float] = []
        last_payload = None
        last_text = ""

        print(f"==> Benchmark {model}")
        for idx in range(1, RUNS_LATENCE + 1):
            text, elapsed = ollama_generate(model, prompt)
            last_text = text
            latency_runs.append(elapsed)
            print(f"    latence {idx}/{RUNS_LATENCE} : {elapsed:.2f}s")
            if idx <= RUNS_QUALITE:
                payload = parse_quiz_payload(text)
                quality_runs.append(score_quiz(payload if payload is not None else text))
                if payload is not None:
                    last_payload = payload

        if last_payload is None:
            last_payload = parse_quiz_payload(last_text)
        if last_payload is None:
            last_payload = {"raw_response": last_text}

        model_dir = MIGRATION_DIR / sanitize_model_name(model)
        p50 = percentile(latency_runs, 0.50) if latency_runs else None
        p95 = percentile(latency_runs, 0.95) if latency_runs else None
        quality_score = round(sum(quality_runs) / len(quality_runs), 1) if quality_runs else 0.0
        disk_go = ollama_taille_go(model)
        payloads[model] = last_payload

        temp_result = ModelResult(
            model=model,
            slug=sanitize_model_name(model),
            p50=p50,
            p95=p95,
            quality_auto_10=quality_score,
            disk_go=disk_go,
            composite_100=None,
            recap_path=model_dir / "recapitulatif.md",
            quiz_path=model_dir / "generated_quizz.json",
        )
        results.append(temp_result)

    build_composite(results)

    for result in results:
        recap_path, quiz_path = write_model_artifacts(
            model_dir=MIGRATION_DIR / result.slug,
            payload=payloads.get(result.model, {}),
            model=result.model,
            source_path=COURS_PATH,
            source_text=cours,
            quality_score=result.quality_auto_10 or 0.0,
            p50=result.p50,
            p95=result.p95,
            disk_go=result.disk_go,
            composite_100=result.composite_100,
        )
        result.recap_path = recap_path
        result.quiz_path = quiz_path

    write_summary_file(COURS_PATH, results)

    print("")
    print("| Modele | p50 (s) | p95 (s) | Qualite /10 | Go | Composite /100 | Dossier |")
    print("|---|---:|---:|---:|---:|---:|---|")
    for result in results:
        print(
            "| {model} | {p50} | {p95} | {quality} | {disk} | {composite} | {dir} |".format(
                model=result.model,
                p50=f"{result.p50:.2f}" if result.p50 is not None else "-",
                p95=f"{result.p95:.2f}" if result.p95 is not None else "-",
                quality=f"{result.quality_auto_10:.1f}",
                disk=f"{result.disk_go:.2f}" if result.disk_go is not None else "-",
                composite=f"{result.composite_100:.1f}" if result.composite_100 is not None else "-",
                dir=display_path(MIGRATION_DIR / result.slug),
            )
        )

    print("")
    print(f"Resultats ecrits dans {EXPORT_PATH}")
    print(f"Dossiers modeles crees sous {MIGRATION_DIR}")
    if BENCHMARK_REFERENCE:
        print(f"Methode de reference retenue : {BENCHMARK_REFERENCE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
