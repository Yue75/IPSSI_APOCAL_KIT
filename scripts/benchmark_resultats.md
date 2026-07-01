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
| llama3.1:8b | 13.09 | 42.42 | 0.0 | 4.92 | 29.1 | `scripts/migration/llama3-1-8b` |
| llama3.2:3b | 4.87 | 15.18 | 0.0 | 2.02 | 60.0 | `scripts/migration/llama3-2-3b` |
| phi3:mini | 92.77 | 115.02 | 5.4 | 2.18 | 58.9 | `scripts/migration/phi3-mini` |

## Note

Les fichiers generes par modele sont stockes dans `scripts/migration/<modele>/`.
Chaque dossier contient `recapitulatif.md` et `generated_quizz.json`.
