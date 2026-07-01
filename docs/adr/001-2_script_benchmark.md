# ADR-001-2 · Conservation d'un benchmark unique pour les comparaisons LLM

- **Date :** 01/07/2026
- **Statut :** Accepté

---

## Contexte

Deux scripts de benchmark existent dans le projet :

- `scripts/benchmark_llm.py`, qui compare plusieurs LLM avec un protocole commun ;
- `scripts/migration/llama318b/benchmark.py`, qui valide un seul modèle avec des mesures plus ciblées.

Les deux approches sont utiles, mais elles ne produisent pas le même niveau de comparabilité entre modèles.

## Constat

Le benchmark dédié à `llama3.1:8b` est plus précis sur un modèle isolé, car il ajoute une mesure de RAM pic et une notation humaine de la qualité.

En revanche, cette précision locale rend la comparaison entre plusieurs modèles moins homogène, car le protocole est centré sur un seul cas d'usage.

## Décision

Nous décidons de conserver un seul benchmark de référence pour les comparaisons entre modèles :

- le benchmark multi-modèles porté par `scripts/benchmark_llm.py`.

Ce choix permet de garder un protocole unique, reproductible et comparable pour tous les LLM testés.

## Justification

Cette décision repose sur trois points :

- un seul protocole de référence évite les écarts de mesure ;
- les résultats restent comparables d'un modèle à l'autre ;
- les sorties du benchmark peuvent être historisées de manière uniforme dans `scripts/migration/`.

## Conséquences

### Positives

- Résultats plus fiables pour la comparaison entre modèles.
- Organisation standardisée des artefacts de benchmark par modèle.
- Réduction du risque d'interpréter deux benchmarks différents comme s'ils mesuraient la même chose.

### Négatives

- Le benchmark de référence est un peu moins précis qu'un benchmark spécialisé sur un seul modèle.
- Certaines mesures très ciblées restent disponibles seulement dans le script de migration.

## Révision

Cette décision pourra être revue si un futur besoin exige une évaluation plus fine d'un modèle isolé ou un protocole matériel plus spécialisé.
