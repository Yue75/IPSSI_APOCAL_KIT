# Product Vision Board

## 1. Vision

Faire d'EduTutor IA la plateforme de revision intelligente de reference pour les lyceens en France, accessible a tous, capable d'accompagner chaque eleve dans sa langue et suffisamment robuste pour supporter un usage national.

La vision produit evolue donc d'un MVP de revision individuelle vers un service public de fait : fiable, inclusif, conforme RGAA, souverain sur les donnees pedagogiques et pret a s'internationaliser.

## 2. Cible (Target Group)

La cible principale devient le lyceen en France, de la seconde a la terminale, qui revise des cours, controles continus, epreuves de specialite ou examens nationaux a partir de supports fournis par ses enseignants ou son etablissement.

Ses caracteristiques cles :

- Il revise souvent sous contrainte de temps, avec des niveaux d'autonomie tres variables.
- Il a besoin d'un outil simple, rassurant et directement aligne sur les programmes et supports etudies.
- Il peut etre en situation de handicap temporaire ou durable : handicap visuel, moteur, cognitif, auditif, trouble dys, fatigue attentionnelle.
- Il peut utiliser le service depuis un ordinateur familial, un smartphone ou un poste d'etablissement.
- Il doit pouvoir comprendre l'interface et les reponses de l'IA, y compris dans un contexte d'apprentissage multilingue.

Les cibles secondaires deviennent structurantes :

- Enseignants, qui veulent proposer des exercices fiables sans perdre le controle pedagogique.
- Etablissements scolaires, qui attendent securite, administration, supervision et continuite de service.
- Ministere, rectorats et collectivites, qui imposent accessibilite RGAA, conformite, resilience et pilotage.
- Familles, qui cherchent un accompagnement utile, comprehensible et equitable pour leurs enfants.

## 3. Besoins (Needs)

Les utilisateurs ont besoin de passer rapidement d'un support de cours a une situation d'auto-evaluation concrete, sans exclure aucun eleve et sans faire porter la complexite technique aux etablissements.

Besoins eleves :

- Generer des quiz et explications a partir des cours reellement etudies.
- Comprendre ses erreurs avec des corrections claires, progressives et adaptees a son niveau.
- Utiliser l'application au clavier, avec lecteur d'ecran, contrastes suffisants, textes lisibles et navigation previsible.
- Changer de langue d'interface et obtenir des reponses IA dans la langue de l'eleve, a la volee.
- Retrouver son historique et suivre ses progres sans friction.

Besoins enseignants et etablissements :

- Garder une confiance pedagogique dans les contenus generes.
- S'assurer que les donnees des eleves et supports de cours sont protegees.
- Disposer d'une plateforme stable lors des pics d'usage, notamment avant les examens.
- Piloter les risques : accessibilite, conformite, qualite IA, couts d'inference, dependance fournisseur.

## 4. Produit (Product)

EduTutor IA est une plateforme web de revision personnalisee, accessible et multilingue, qui transforme les supports de cours en exercices interactifs et explications adaptees.

Les elements qui definissent son identite cible :

- Depot ou selection de supports de cours : PDF, texte brut, contenus enseignants ou ressources d'etablissement.
- Generation automatique de quiz, corrections et explications par IA.
- Historique de revision, progression et reprise des activites.
- Interface conforme RGAA : structure semantique, alternatives textuelles, contrastes, navigation clavier, messages d'erreur explicites, compatibilite lecteur d'ecran.
- Internationalisation de l'interface : separation des libelles, formats locaux, langue utilisateur et contenus traduisibles.
- IA multilingue : detection ou selection de langue, generation de questions et explications dans la langue de l'eleve, avec garde-fous pedagogiques.
- Architecture IA multi-fournisseurs : modele local par defaut lorsque possible, bascule controlee vers fournisseurs cloud selon charge, langue, qualite ou disponibilite.
- Architecture scalable et resiliente : files de traitement, services decouples, cache, observabilite, degradation controlee en cas de pic.

## 5. Objectifs business (Business Goals)

L'organisation cherche a transformer un succes d'usage soudain en plateforme nationale credible, contractualisable et extensible a l'international.

Objectifs principaux :

- Obtenir l'eligibilite a un deploiement dans les lycees en respectant les exigences RGAA et RGPD.
- Stabiliser la plateforme pour absorber les pics de connexion massifs lies aux revisions nationales.
- Construire une trajectoire d'internationalisation : langues d'interface, langues de reponse IA, adaptation progressive aux contextes pedagogiques locaux.
- Maintenir une differenciation par la souverainete, la confiance pedagogique et la maitrise des couts IA.
- Soutenir la levee de fonds par des artefacts a jour : vision produit, risques, priorisation, feuille de route et indicateurs de pilotage.
- Passer d'une logique MVP a une logique plateforme : maintenable, observable, testable et exploitable par des partenaires publics ou prives.

Indicateurs de pilotage proposes :

- Taux de conformite RGAA par parcours critique.
- Disponibilite de service et temps de reponse en periode de pic.
- Taux de generation IA reussie par langue.
- Cout moyen d'inference par quiz et par utilisateur actif.
- Taux de completion des quiz et progression moyenne des scores.
- Nombre d'incidents critiques lies a l'accessibilite, la securite ou la qualite IA.

Risques majeurs identifies :

- Non-conformite RGAA bloquant l'adoption par l'Etat.
- Saturation technique lors des pics d'usage televisuels ou pre-examens.
- Reponses IA incorrectes, mal traduites ou inadaptees au niveau scolaire.
- Derive des couts si le recours aux modeles cloud devient non maitrise.
- Complexite d'internationalisation sous-estimee : interface, contenus, prompts, evaluation qualite.
- Perte de confiance si la gouvernance des donnees eleves et supports pedagogiques n'est pas explicite.
