# ADR-004-2 · Choix final du modèle LLM après benchmark

## Contexte

Le benchmark défini dans [001-2_script_benchmark.md](./001-2_script_benchmark.md) a permis de comparer plusieurs modèles sur un protocole unique et reproductible.

Les résultats consolidés dans [benchmark_resultats.md](../../scripts/benchmark_resultats.md) montrent que `llama3.2:3b` offre le meilleur compromis pour notre usage, avec une latence plus faible que les autres modèles testés.

## Décision

Nous décidons de partir sur le modèle `llama3.2:3b` pour la génération de quiz.

Ce choix s'appuie sur les résultats du benchmark, qui montrent qu'il répond mieux au besoin de rapidité tout en restant cohérent avec les contraintes du projet.

## Justification

Le modèle `llama3.2:3b` ressort comme le plus adapté pour notre cas d'usage car il réduit le temps d'attente lors de la génération.

Dans notre contexte applicatif, la latence est un critère déterminant pour l'expérience utilisateur. Un modèle plus rapide permet d'éviter l'impression de blocage pendant la génération des quiz.

## Conséquences

### Positives

* Génération plus rapide des quiz.
* Meilleure expérience utilisateur.
* Décision fondée sur un benchmark unique et comparable.

### Négatives

* Le modèle retenu est plus léger que `llama3.1:8b`, ce qui peut imposer quelques arbitrages sur la richesse de génération.
* Toute évolution future du besoin pourra nécessiter un nouveau benchmark.

## Révision

Cette décision pourra être revue si de nouveaux benchmarks montrent un modèle plus performant pour notre usage ou si les priorités du projet évoluent.

---

**Date :** 01/07/2026

**Statut :** Accepté
