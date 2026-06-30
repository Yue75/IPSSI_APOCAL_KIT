# ADR-002 · Choix du modèle LLM pour génération de quiz

## Contexte

Lors du beta-test du jour 2, un utilisateur a signalé une latence trop élevée lors de la génération de quiz (~45 secondes pour 10 questions). Cette latence est jugée inacceptable car elle donne l’impression que l’application est bloquée, ce qui impacte fortement l’expérience utilisateur et le taux de rétention.

Le modèle actuellement utilisé est **Llama 3.1 8B**, exécuté en local.

Un benchmark a été réalisé afin de comparer plusieurs modèles selon :

* Latence (p50, p95)
* Qualité perçue (/5 par 3 testeurs)
* Ressources nécessaires (RAM)

## Options envisagées

| Modèle       | p50  | p95  | Qualité (/5) | RAM requise |
| ------------ | ---- | ---- | ------------ | ----------- |
| Llama 3.1 8B | 42 s | 51 s | 4.5          | ~8 Go       |
| Llama 3.2 3B | 12 s | 18 s | 4            | ~2 Go       |
| Phi-3 Mini   | 14 s | 22 s | 3.8          | ~2 Go       |

## Décision

Nous décidons de **basculer vers Llama 3.2 3B**.

## Justification

Ce modèle offre le meilleur compromis entre performance et qualité :

* Latence divisée par ~3 (objectif < 15 s atteint)
* Qualité légèrement inférieure mais jugée acceptable pour un usage pédagogique
* Consommation mémoire réduite, facilitant le déploiement

Le modèle Llama 3.1 8B est écarté malgré sa meilleure qualité, car sa latence nuit fortement à l’expérience utilisateur.

Phi-3 Mini est également écarté car sa qualité est inférieure sans gain significatif en latence.

## Conséquences

### Positives

* Amélioration significative de l’expérience utilisateur
* Réduction du taux d’abandon
* Meilleure compatibilité avec des machines modestes

### Négatives

* Légère baisse de qualité des questions générées
* Nécessité de retester la pertinence pédagogique

### À surveiller

* Qualité des quiz sur des contenus complexes
* Possibilité d’optimisations futures (batching, streaming, caching)
* Éventuelle hybridation avec un modèle plus puissant à la demande

---

Date : 30/06/2026
Statut : Accepté
