# Resultats du benchmark LLM

- Cours de reference : `scripts/cours_reference.txt`
- Runs latence : 5
- Runs qualite : 2
- Seuil p95 : 15 s
- Score composite : {'latence': 0.4, 'qualite': 0.4, 'ressources': 0.2}
- Benchmark de reference : `composite`

## Synthese

| Modele | p50 (s) | p95 (s) | Qualite auto /10 | Ressources (Go) | Composite /100 | Dossier |
|---|---:|---:|---:|---:|---:|---|
| llama3.1:8b | 113.20 | 130.51 | 10.0 | 4.92 | 40.0 | `scripts/migration/llama3-1-8b` |
| llama3.2:3b | 61.01 | 73.63 | 7.5 | 2.02 | 60.0 | `scripts/migration/llama3-2-3b` |
| phi3:mini | 98.30 | 107.79 | 8.8 | 2.18 | 55.7 | `scripts/migration/phi3-mini` |

## Note

Les fichiers generes par modele sont stockes dans `scripts/migration/<modele>/`.
Chaque dossier contient `recapitulatif.md` et `generated_quizz.json`.
