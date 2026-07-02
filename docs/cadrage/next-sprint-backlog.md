# Next Sprint Backlog
## Sprint 2

### Informations générales

- **Sprint :** Sprint 2
- **Date :** À définir
- **Équipe :** Équipe 22
- **Scrum Master :** Baptiste MAES
- **Product Owner :** Tom Lau
- **Capacité :** 28 h-personnes
- **Vélocité cible :** 10 à 12 Story Points

---

# Objectif du Sprint

Développer les premières fonctionnalités liées à l'internationalisation (i18n), à l'accessibilité et à la montée en charge de la plateforme EduTutor IA.

L'objectif est d'améliorer l'expérience utilisateur en rendant l'application accessible à tous, disponible en plusieurs langues et capable de supporter davantage d'utilisateurs simultanés.

---

# User Stories sélectionnées

## US-11 — Internationalisation (i18n)

> En tant qu'étudiant étranger, je souhaite utiliser l'application en anglais afin de comprendre facilement toutes les fonctionnalités.

**Référence : ADR-003 — Choix de la stratégie d'internationalisation (i18n).**

| ID | Tâche | Responsable | Estimation |
|----|--------|-------------|------------|
| T-11.1 | Mise en place du système de traduction (i18n) *(cf. ADR-003)* | Baptiste MAES | 2 h |
| T-11.2 | Traduction de l'interface en anglais | Antoine Vauthier | 3 h |
| T-11.3 | Tests de fonctionnement des langues | Tom Lau | 1 h |

---

## US-12 — Accessibilité (RGAA)

> En tant qu'utilisateur en situation de handicap, je souhaite utiliser l'application avec un lecteur d'écran afin d'accéder à toutes les fonctionnalités.

| ID | Tâche | Responsable | Estimation |
|----|--------|-------------|------------|
| T-12.1 | Ajout des labels d'accessibilité | Kyllian Vignocan | 2 h |
| T-12.2 | Navigation complète au clavier | Yacine Djebbouri | 2 h |
| T-12.3 | Compatibilité lecteur d'écran | Alainpatrick Gomas | 2 h |
| T-12.4 | Tests d'accessibilité | Cleg Loufoua | 2 h |

---

## US-13 — Scalabilité

> En tant qu'administrateur, je souhaite que la plateforme supporte plusieurs utilisateurs simultanément afin de garantir de bonnes performances.

| ID | Tâche | Responsable | Estimation |
|----|--------|-------------|------------|
| T-13.1 | Optimisation des performances backend | Baptiste MAES | 3 h |
| T-13.2 | Mise en cache des requêtes fréquentes | Antoine Vauthier | 2 h |
| T-13.3 | Tests de montée en charge | Tom Lau | 2 h |

---

# Charge de travail

| Élément | Valeur |
|----------|--------|
| Charge estimée | 21 h |
| Capacité équipe | 28 h |
| Marge disponible | 7 h |

---

# Répartition de l'équipe

| Membre | Charge |
|---------|--------|
| Baptiste MAES | 5 h |
| Antoine Vauthier | 5 h |
| Tom Lau | 3 h |
| Kyllian Vignocan | 2 h |
| Alainpatrick Gomas | 2 h |
| Cleg Loufoua | 2 h |
| Yacine Djebbouri | 2 h |

---

# État initial

Toutes les tâches sont positionnées en **Todo**.

- Todo
- In Progress
- Blocked
- Done

---

# Burndown prévisionnel

| Heure | Idéal | Réel |
|-------|------:|------:|
| 09h00 | 21 h | 21 h |
| 10h00 | 17 h | 18 h |
| 11h00 | 13 h | 13 h |
| 12h00 | 9 h | 9 h |
| 13h00 | 5 h | 5 h |
| 14h00 | 0 h | 0 h |

---

# Sprint Review

À la fin du Sprint 2, l'équipe devra être capable de démontrer :

- une interface disponible en français et en anglais ;
- une navigation compatible avec les recommandations RGAA ;
- une meilleure accessibilité pour les utilisateurs en situation de handicap ;
- des performances améliorées lors de plusieurs connexions simultanées.

---

# Définition de Done

Une tâche est considérée comme terminée lorsqu'elle :

- est développée ;
- est testée ;
- respecte les recommandations RGAA ;
- est validée par un membre de l'équipe ;
- est fusionnée dans la branche principale après validation de la Pull Request.

---

# Risques identifiés

- Difficultés d'intégration de l'internationalisation (i18n).
- Non-conformité partielle aux critères RGAA.
- Dégradation des performances sous forte charge.
- Manque de temps pour réaliser les tests de charge.
- Régressions sur les fonctionnalités existantes.

---

# Références

- **ADR-003 — Choix de la stratégie d'internationalisation (i18n).**