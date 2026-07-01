# Story Map — EduTutor IA (Après perturbation J1)

## Backbone / Parcours utilisateur global

### Parcours Étudiant
- Authentification
- Import du cours
- Génération du quiz
- Réalisation du quiz
- Correction et résultats
- Suivi de progression
- Gestion du compte

### Parcours Enseignant (Mme Lefèvre)
- Suivi de classe
- Détection des étudiants en difficulté
- Accompagnement pédagogique

---

# MUST (Release 1)

## Authentification
- Créer un compte
- Se connecter
- Réinitialiser le mot de passe

## Import du cours
- Upload d'un PDF (≤ 5 Mo)
- Coller un texte (≥ 200 caractères)

## Génération du quiz
- Générer automatiquement un quiz de 10 QCM via une IA locale

## Réalisation du quiz
- Répondre aux questions
- Soumettre les réponses

## Résultats
- Voir le score sur 10
- Voir les bonnes et mauvaises réponses

## Progression de l'étudiant
- Consulter l'historique des quiz

---

# SHOULD (Ajout perturbation J1)

## Suivi enseignant
- Voir les scores des 28 étudiants
- Suivre la progression de chaque étudiant

## Détection des décrocheurs
- Identifier rapidement les étudiants en difficulté
- Repérer une baisse de performance

---

# COULD (Release 2)

## Améliorations côté étudiant
- Connexion Google / SSO
- OCR pour les documents scannés
- Difficulté configurable
- Mode examen avec timer
- Explications détaillées générées par l'IA
- Dashboard avancé

## Améliorations côté enseignant
- Analytics de classe
- Envoyer des conseils personnalisés
- Génération automatique de recommandations de révision

---

# User Stories — Étudiant

- En tant qu'étudiant, je veux créer un compte afin d'accéder à la plateforme.
- En tant qu'étudiant, je veux me connecter afin de retrouver mes données.
- En tant qu'étudiant, je veux importer un cours afin de générer un quiz.
- En tant qu'étudiant, je veux répondre à un quiz afin d'évaluer mes connaissances.
- En tant qu'étudiant, je veux voir mon score afin d'identifier mes lacunes.
- En tant qu'étudiant, je veux consulter mon historique afin de suivre ma progression.

---

# User Stories — Enseignant (J1)

- En tant qu'enseignante, je veux consulter les scores de mes étudiants afin d'évaluer leur niveau global.
- En tant qu'enseignante, je veux suivre leur progression afin d'observer leur évolution.
- En tant qu'enseignante, je veux identifier rapidement les étudiants en difficulté afin d'intervenir plus tôt.
- En tant qu'enseignante, je veux repérer les baisses de performance afin de prévenir le décrochage.
- En tant qu'enseignante, je veux envoyer des conseils personnalisés afin d'aider les étudiants à progresser.

---

# Priorisation MoSCoW

## MUST
- MVP étudiant complet

## SHOULD
- Dashboard enseignant
- Suivi des scores
- Détection des décrocheurs

## COULD
- Conseils personnalisés
- Analytics avancés
- Recommandations IA