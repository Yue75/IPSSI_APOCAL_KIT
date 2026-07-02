# ADR-005-1 · Stratégie de support multilingue de l'application

## Contexte

L'application est aujourd'hui pensée principalement pour un usage francophone. Cependant, le projet étant basé en France, il est naturel de démarrer avec le français tout en préparant dès maintenant une ouverture à l'anglais, langue largement utilisée par les utilisateurs et les écosystèmes techniques.

L'enjeu est de faire évoluer l'application sans créer de dette technique importante. La solution retenue doit permettre d'ajouter de nouvelles langues plus tard sans refonte profonde de l'interface ou des contenus.

## Options envisagées

* Conserver une application uniquement en français.
* Ajouter manuellement quelques textes traduits sans structure dédiée.
* Mettre en place une stratégie i18n basée sur des fichiers JSON.
* Externaliser immédiatement les traductions dans un service tiers.

## Décision

Nous décidons de mettre en place une stratégie d'internationalisation (`i18n`) basée sur des fichiers JSON.

L'application supportera en priorité deux langues :

* `FR` pour la langue principale du projet ;
* `EN` pour couvrir un usage international de base.

Cette base devra rester extensible afin de pouvoir ajouter d'autres langues ultérieurement sans modifier l'architecture applicative.

## Justification

Le choix d'une structure `i18n` avec JSON permet de séparer clairement le contenu traduisible du code applicatif.

Cette approche est simple à maintenir, facile à versionner et suffisamment souple pour faire évoluer l'application progressivement. Elle évite également de dupliquer les composants UI pour chaque langue et prépare une montée en charge raisonnable du nombre de langues supportées.

Le français reste la langue de référence du projet, tandis que l'anglais constitue la première ouverture logique pour les utilisateurs non francophones.

## Conséquences

### Positives

* Interface plus facile à adapter à plusieurs langues.
* Structure claire pour gérer les traductions.
* Ajout de nouvelles langues simplifié.
* Meilleure accessibilité pour un public plus large.

### Négatives

* Nécessité de maintenir les fichiers de traduction à jour.
* Risque de désynchronisation entre les clés JSON et les textes affichés si les traductions ne sont pas vérifiées.
* Travail initial supplémentaire pour extraire les libellés de l'interface.

## Points de vigilance

* Garder une clé de traduction stable et cohérente.
* Prévoir une langue de fallback, idéalement le français.
* Vérifier que les textes dynamiques générés par le LLM respectent aussi la langue choisie.
* Préparer l'application à l'ajout futur d'autres langues sans refonte du socle i18n.

---

**Date :** 02/07/2026

**Statut :** Accepté
