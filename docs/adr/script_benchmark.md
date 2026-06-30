ADR-002 · Stratégie de benchmark pour le choix du modèle LLM
Contexte
Afin de sélectionner le modèle LLM le plus adapté à la génération de quiz, plusieurs benchmarks sont envisagés. Chaque benchmark évalue les modèles selon différents critères, notamment les performances, la qualité des quiz générés et les ressources consommées.
Cependant, utiliser plusieurs benchmarks tout au long du projet pourrait produire des résultats difficiles à comparer, car les protocoles d'évaluation et les métriques peuvent varier d'un benchmark à l'autre.
Options envisagées
Utiliser plusieurs benchmarks pendant toute la durée du projet.
Sélectionner un benchmark unique dès le début.
Tester plusieurs benchmarks dans un premier temps, puis en sélectionner un seul comme référence pour toutes les évaluations ultérieures.
Décision
Nous décidons de tester plusieurs benchmarks lors de la phase d'évaluation initiale afin d'identifier celui qui est le plus pertinent pour notre cas d'usage.
À l'issue de cette phase, un seul benchmark sera retenu et utilisé comme référence pour comparer les différents modèles LLM tout au long du projet.
Justification
Cette approche permet :
d'évaluer les différentes méthodes de benchmark disponibles ;
de choisir un protocole d'évaluation adapté à notre application ;
de garantir des comparaisons cohérentes entre les modèles en utilisant ensuite une méthodologie unique ;
de limiter les biais liés à l'utilisation de plusieurs benchmarks différents.
Conséquences
Positives
Évaluations homogènes et comparables.
Meilleure reproductibilité des résultats.
Processus de sélection du modèle plus rigoureux.
Négatives
Temps supplémentaire nécessaire pour évaluer les différents benchmarks.
Nécessité de justifier le benchmark retenu.
À surveiller
La pertinence du benchmark choisi par rapport au cas d'usage.
L'évolution des besoins du projet pouvant nécessiter une réévaluation du benchmark.
La reproductibilité des résultats obtenus.
Date : 30/06/2026
Statut : Accepté