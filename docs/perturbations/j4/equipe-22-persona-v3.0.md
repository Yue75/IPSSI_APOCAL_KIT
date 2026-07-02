# Fiches Personas — mise à jour J4 (v3.0)

**APOCAL'IPSSI — Perturbation J4 · Passage à l'échelle (accessibilité RGAA + i18n)**
Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum

## Identification du document

| Champ | Valeur |
|---|---|
| Équipe n° | 22 |
| Membres | Alain-Patrick GOMAS *(co-construction persona, ≥ 2 membres)* |
| Sprint concerné | Perturbation J4 |
| Version | **v3.0 (nouvel utilisateur ajouté suite à la perturbation J4)** |
| Date de remise | 02/07/2026 — *[ HHhMM ]* |
| Statut | Draft |
| Dépôt | `/docs/perturbations/j4/` |

> Convention de nommage : `equipe-22-persona-v3.0.md`
> Les personas étudiant (Léa Martin) et établissement (M. David Chen) restent **conservés** dans `/docs/cadrage/`. La persona enseignante (Mme Lefèvre, J1) est **conservée ci-dessous** (CA-J4-6, conservation de l'historique). J4 **ajoute** une nouvelle cible, il ne remplace rien.

---

## Ce qui change depuis J1 (v2.0 → v3.0)

| | v2.0 (post-perturbation J1) | v3.0 (post-perturbation J4) |
|---|---|---|
| Cibles | Léa (étudiante) · Mme Lefèvre (enseignante) · M. Chen (établissement) | **+ Lucia Fernández** (nouvelle) |
| Axes produit couverts | suivi pédagogique de classe | **+ accessibilité RGAA (a11y) + internationalisation (i18n)** |
| Contexte | intégration de la cible enseignante | **passage à l'échelle** : plateforme de référence pour l'État, exigence RGAA + multilingue |

---

# Persona 1 (conservée) — Mme Sophie Lefèvre

### 1. Identité & rôle
Mme Sophie Lefèvre, **42 ans**, professeure de Communication en **BTS** (lycée privé sous contrat, Lyon 6ᵉ). Encadre **28 étudiants** en BTS Communication 1ʳᵉ année. Mariée, 2 enfants (12 et 15 ans), ~2 700 € net/mois. Trajet voiture 25 min.
**Rôle produit :** utilisatrice enseignante qui veut **piloter la révision de sa classe**, pas seulement produire des quiz.

### 2. Objectifs (jobs-to-be-done, SMART)
- Voir en un coup d'œil les **scores de ses 28 étudiants** après chaque quiz (vue classe), sans tableur manuel
- **Repérer les décrocheurs en ≤ 3 clics** (ex. score < 5/10 sur 2 quiz consécutifs)
- **Envoyer un conseil ciblé** à un étudiant en difficulté en moins de 5 minutes
- *(conservé)* Générer un quiz personnalisé sur n'importe quel chapitre en moins de 5 minutes
- *(conservé)* Exporter un quiz en Word/PDF imprimable en moins de 2 minutes

### 3. Besoins
- Un **dashboard enseignant** : score moyen de la classe, distribution, liste d'étudiants triable par score
- Une **mise en évidence des décrocheurs** (alerte visuelle, filtre « en difficulté »)
- Un **canal de feedback** pour adresser un message/conseil aux étudiants concernés
- Une **conformité RGPD** sur les données de ses 28 étudiants (angle local-first, lien perturbation J3-bis)

### 4. Contraintes
- Réseau d'établissement lent (salle info en 4G partagée) → l'app doit rester fluide en conditions dégradées
- Pas d'ordinateur dédié en classe : laptop personnel branché au vidéoprojecteur
- ~12h/semaine déjà absorbées par cours + préparation + correction → **zéro temps pour apprendre un outil complexe**
- Données de 28 étudiants à manipuler → exigence RGPD non négociable

### 5. Frustrations / pain points (chiffrés)
- Corrige 28 copies × 3 quiz/semaine = **~12h de correction par mois**
- Créer 1 quiz cohérent lui prend **~90 minutes** ; recréer des variantes anti-triche = **~2h/semaine perdues**
- Pour repérer un décrocheur, elle **compile les notes à la main dans Excel (~30 min/semaine)**
- Les outils existants sont **non-pédagogiques** : ils résument, mais ne montrent jamais *qui* décroche
- Aucune visibilité sur l'engagement réel des étudiants entre deux cours

### 6. Expérience / niveau tech
- **À l'aise avec le numérique mais pas développeuse** : power user Word/Excel, autonome sur Moodle et Pronote
- A testé ChatGPT 2 fois ; **allergique aux installations en ligne de commande** → exige une interface zéro configuration
- Suit l'edtech via X/Twitter et la newsletter du Café Pédagogique

### 7. Critères de succès personnels (au « je »)
- « Si je repère mes décrocheurs en 3 clics, j'utilise l'outil chaque semaine. »
- « Si je vois les scores de mes 28 sans ouvrir un tableur, c'est gagné. »
- « Si ça plante 1 fois en cours devant 28 ados, je n'y reviens jamais. »
- « Si je peux envoyer un conseil à un élève en difficulté sans quitter l'app, je le recommande à mes collègues. »

---

# Persona 2 (nouvelle J4) — Lucia Fernández · accessibilité RGAA + i18n

> Utilisatrice que le produit « franco-français » actuel exclut totalement. Elle rend concrètes **2 des 3 exigences** du passage à l'échelle : **accessibilité (RGAA)** et **internationalisation (i18n)**.

### 1. Identité
Lucia Fernández, **17 ans**, élève en 1ʳᵉ année de Bachillerato (lycée public, **Séville, Espagne**). **Malvoyante de naissance** (résidu visuel ~10 %). Vit chez ses parents, boursière.

### 2. Contexte d'usage
- Ordinateur portable avec **lecteur d'écran NVDA** + zoom système à 200 %
- **Navigation exclusivement au clavier** (n'utilise pas de souris)
- Smartphone Android avec **TalkBack** activé
- Révise ~12h/semaine, le soir, connexion domestique stable
- **Langue : espagnol** — ne lit pas le français

### 3. Compétences numériques
- **Experte des technologies d'assistance** : lecteurs d'écran, raccourcis clavier, gestes TalkBack
- Très autonome **à condition** que l'interface soit correctement balisée (attributs ARIA, ordre de tabulation logique, libellés de boutons)
- Abandonne immédiatement toute application non navigable au clavier ou dont les boutons/images n'ont pas de description

### 4. Contraintes
- Dépend d'une **structure sémantique correcte** (sans quoi le lecteur d'écran est perdu)
- **Aucune information transmise uniquement par la couleur** (elle ne la perçoit pas fiablement)
- **Barrière de langue** : tout contenu en français seul lui est inaccessible

### 5. Frustrations / pain points (chiffrés)
- Environ **1 appli edtech sur 3 est inutilisable** au lecteur d'écran (boutons sans libellé, images sans texte alternatif)
- Perd **~30 min par session** à contourner des interfaces mal balisées
- Les contenus **uniquement en français lui sont 100 % inaccessibles**
- Les **contrastes insuffisants** rendent le texte illisible malgré le zoom

### 6. Objectifs (jobs-to-be-done, SMART)
- Générer et passer un quiz **entièrement au clavier + lecteur d'écran**, sans aide extérieure
- Utiliser l'**interface et les quiz traduits en espagnol** (i18n)
- Passer un quiz complet avec **zéro blocage d'accessibilité**

### 7. Critères de succès personnels (au « je »)
- « Si mon lecteur d'écran annonce clairement chaque question et chaque option, je l'utilise. »
- « Si l'interface et les quiz sont en espagnol, c'est enfin une appli pensée pour moi. »
- « Si je peux tout faire au clavier, sans souris, je la recommande à mon centre. »
- « Si je bute une seule fois sur un bouton non annoncé, je laisse tomber. »

---

## Annexe J4 — Matière pour les autres artefacts

*À transmettre à l'équipe (story map, backlog, release planning, analyse de risques).*

### Items de backlog nourris par Lucia (taggés + estimés)
- `[a11y]` Audit RGAA + focus clavier visible & contrastes conformes — **8 pts · Must**
- `[a11y]` Libellés ARIA et textes alternatifs sur tout le parcours quiz — **5 pts · Must**
- `[i18n]` Externaliser les textes de l'interface en fichiers de langue (fr / en / es) — **8 pts · Must**
- `[i18n]` Paramètre de langue du LLM à la volée (quiz généré dans la langue de l'élève) — **5 pts · Should**

### Risques à remonter (matrice probabilité × impact, livrable J4)
- **Non-conformité RGAA** → blocage du contrat État (probabilité moyenne, impact critique) → action : audit RGAA dès le prochain sprint.
- **Quiz généré dans la mauvaise langue** par le LLM → expérience cassée pour l'utilisateur international (probabilité moyenne, impact fort) → action : forcer la langue dans le prompt + validation de sortie.
