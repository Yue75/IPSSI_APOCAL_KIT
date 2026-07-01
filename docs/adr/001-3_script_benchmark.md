# ADR-001-3 · Normalisation du format JSON du benchmark

- **Date :** 01/07/2026
- **Statut :** Accepté

---

## Contexte

Le benchmark génère bien des quiz, mais le format JSON produit par certains modèles ne correspond pas encore au format de référence attendu dans le projet.

Le format cible est celui utilisé par [demo_quizzes.json](../../backend/quizzes/management/commands/demo_quizzes.json) : une liste d'objets contenant `title`, `source_text` et `questions`, avec des questions décrites par `prompt`, `options` et `correct_index`.

## Constat

Le modèle testé ne renvoie pas systématiquement ce format exact. Il peut produire une structure plus simple, ou des clés différentes, ce qui rend l'artefact de benchmark difficile à réutiliser directement dans le reste de l'application.

## Décision

Nous décidons de faire évoluer [scripts/benchmark_llm.py](../../scripts/benchmark_llm.py) pour qu'il génère un JSON aligné sur [demo_quizzes.json](../../backend/quizzes/management/commands/demo_quizzes.json).

Le fichier produit à la fin du benchmark devra donc reprendre les mêmes clés et la même structure métier que les quiz de démo du projet.

## Justification

Cette normalisation permet de :

- rendre les artefacts de benchmark compatibles avec le reste de l'application ;
- conserver un format homogène entre les quiz de démonstration et les quiz générés par benchmark ;
- simplifier la comparaison, la lecture et la réutilisation des résultats.

## Conséquences

### Positives

- Les fichiers générés par le benchmark deviennent directement exploitables.
- Le format de sortie est cohérent avec les données métier du projet.
- Les comparaisons entre modèles restent possibles tout en conservant une structure commune.

### Négatives

- Le script de benchmark doit faire un travail de normalisation supplémentaire.
- Certains modèles qui ne suivent pas le format attendu devront être corrigés ou encadrés plus strictement par le prompt.

## Révision

Cette décision pourra être réévaluée si le format de référence des quiz évolue dans l'application.
