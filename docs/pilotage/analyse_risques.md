# Analyse des risques – EduTutor IA

## Objectif

Dans le cadre du passage à l'échelle d'**EduTutor IA**, plusieurs risques ont été identifiés concernant la montée en charge de la plateforme, son accessibilité et son internationalisation.

Chaque risque est évalué selon sa **probabilité d'occurrence** et son **impact sur le projet**. Les risques les plus importants donnent lieu à des **actions préventives**, estimées en **Story Points (SP)** et intégrées au **Product Backlog** conformément à la démarche Scrum.

---

# Tableau d'analyse des risques

| ID | Risque | Probabilité | Impact | Priorité | Traitement | Action préventive |
|:--:|---------|:-----------:|:------:|:---------:|------------|-------------------|
| **R1** | Afflux massif d'utilisateurs entraînant une indisponibilité ou un ralentissement de la plateforme | Élevée | Élevé | 🔴 Critique | Réduire la probabilité | Réaliser des tests de charge, mettre en place un système de cache et optimiser l'architecture pour supporter la montée en charge. |
| **R2** | Non-conformité aux exigences d'accessibilité (RGAA) empêchant certains utilisateurs d'utiliser la plateforme | Moyenne | Élevé | 🟠 Élevée | Réduire la probabilité | Réaliser un audit RGAA puis corriger les principaux problèmes d'accessibilité. |
| **R3** | L'interface ou les réponses de l'IA ne sont pas disponibles dans la langue de l'utilisateur | Moyenne | Moyen | 🟡 Moyenne | Réduire la probabilité | Mettre en place un système d'internationalisation (i18n) et transmettre automatiquement la langue sélectionnée au modèle d'IA. |
| **R4** | Indisponibilité du fournisseur de modèle d'IA (LLM) | Faible | Élevé | 🟡 Moyenne | Réduire l'impact | Prévoir un fournisseur LLM secondaire afin d'assurer la continuité du service. |
| **R5** | Dégradation des performances de la base de données avec l'augmentation du nombre d'utilisateurs | Moyenne | Élevé | 🟠 Élevée | Réduire la probabilité | Optimiser les requêtes SQL, ajouter des index et mettre en cache les données les plus consultées. |

---

# Matrice Probabilité × Impact

| **Impact / Probabilité** | **Faible** | **Moyenne** | **Élevée** |
|---------------------------|:----------:|:-----------:|:----------:|
| **Élevé** | **R4** | **R2**, **R5** | **R1** |
| **Moyen** | | **R3** | |
| **Faible** | | | |

---

# Priorisation des risques

Les risques **R1**, **R2** et **R5** sont considérés comme prioritaires en raison de leur impact important sur la disponibilité, la conformité et les performances de la plateforme. Ils sont donc intégrés au prochain sprint.

Les risques **R3** et **R4** restent importants mais peuvent être traités dans les sprints suivants sans compromettre le fonctionnement immédiat du produit.

---

# Intégration des risques dans le Product Backlog

| Risque | Action préventive | User Story | Priorité (MoSCoW) | Estimation |
|---------|-------------------|------------|-------------------|------------|
| **R1** | Optimiser les performances de la plateforme, mettre en place un cache et réaliser des tests de charge | **US-32**, **US-33**, **US-34** | MUST / SHOULD | **13 SP + 8 SP + 8 SP** |
| **R2** | Mettre en conformité la plateforme avec le RGAA (navigation clavier, contraste, lecteurs d'écran...) | **US-28**, **US-29** | MUST | **5 SP + 8 SP** |
| **R3** | Ajouter la gestion multilingue de l'interface et des réponses du LLM | **US-30**, **US-31** | MUST / SHOULD | **8 SP + 5 SP** |
| **R4** | Prévoir un fournisseur LLM secondaire afin d'assurer la continuité du service | **US-35** | COULD | **5 SP** |
| **R5** | Optimiser les performances de la base de données et mettre en cache les données fréquemment utilisées | **US-33** | SHOULD | **8 SP** |

---

# Conclusion

Cette analyse met en évidence les principaux risques liés au passage à l'échelle d'**EduTutor IA**.

Les risques les plus critiques concernent :

- la **scalabilité** de la plateforme face à une forte augmentation du nombre d'utilisateurs ;
- la **conformité au RGAA**, indispensable pour une plateforme destinée au service public ;
- les **performances** de l'application afin de garantir une expérience fluide ;
- l'**internationalisation (i18n)** pour permettre l'utilisation de la plateforme par un public plus large.

Chaque risque prioritaire est associé à une ou plusieurs **User Stories** du **Product Backlog**, estimées en **Story Points** et priorisées selon la méthode **MoSCoW**, afin de réduire leur probabilité d'occurrence ou leur impact sur le projet.