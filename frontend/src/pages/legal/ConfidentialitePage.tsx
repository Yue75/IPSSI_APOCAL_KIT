/** Politique de confidentialité. */
import LegalScaffold from './LegalScaffold';

export default function ConfidentialitePage() {
  return (
    <LegalScaffold
      title="Politique de confidentialité"
      intro="Comment les données personnelles des utilisateurs sont collectées, utilisées et protégées (RGPD)."
      sections={[]}
      isCompleted
    >
      <div className="space-y-6">
        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            1. Responsable du traitement
          </h2>
          <p className="text-sm text-slate-700">
            Le responsable du traitement est EduTutor IA SAS.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            Contact du délégué à la protection des données : dpo@edututor-ia.fr.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            2. Données personnelles collectées
          </h2>
          <ul className="list-disc pl-5 text-sm text-slate-700 space-y-1">
            <li>Compte : adresse email utilisée comme identifiant et mot de passe chiffré.</li>
            <li>Contenus : cours téléversés au format PDF ou texte.</li>
            <li>Activité : quiz générés, réponses, scores, statistiques et historique.</li>
            <li>Signalements : questions signalées par les utilisateurs.</li>
            <li>Logs techniques : journaux nécessaires à la sécurité de la plateforme.</li>
          </ul>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            3. Finalités du traitement
          </h2>
          <p className="text-sm text-slate-700">
            Les données sont utilisées pour fournir le service, générer des quiz, suivre la
            progression des utilisateurs, améliorer la qualité des questions, assurer la sécurité
            de la plateforme et répondre aux obligations légales.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            Aucune donnée n’est utilisée à des fins publicitaires ni revendue à des tiers.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">4. Base légale</h2>
          <ul className="list-disc pl-5 text-sm text-slate-700 space-y-1">
            <li>Exécution du contrat : compte, génération de quiz, sauvegarde de l’historique.</li>
            <li>Intérêt légitime : sécurité, logs techniques et signalements.</li>
            <li>Obligation légale : gestion des demandes RGPD et conservation des preuves.</li>
          </ul>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            5. Souveraineté des données
          </h2>
          <p className="text-sm text-slate-700">
            Le traitement par IA est effectué localement via Ollama. Aucune donnée personnelle
            n’est envoyée à un fournisseur de modèle externe et aucun transfert hors Union
            européenne n’est réalisé.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            6. Durée de conservation
          </h2>
          <p className="text-sm text-slate-700">
            Les données sont conservées uniquement le temps nécessaire à leur finalité.
            Les comptes, cours, quiz et scores sont conservés tant que le compte est actif.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            Les journaux d’audit sont conservés 12 mois. Les signalements et demandes RGPD
            sont conservés 3 ans. À l’expiration des délais, les données sont supprimées ou
            anonymisées.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">7. Vos droits</h2>
          <p className="text-sm text-slate-700">
            Conformément au RGPD, vous disposez d’un droit d’accès, de rectification,
            d’effacement, de limitation et de portabilité de vos données.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            Vous pouvez exercer ces droits depuis votre page profil ou en écrivant à
            dpo@edututor-ia.fr. Vous pouvez également saisir la CNIL en cas de litige.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">8. Cookies</h2>
          <p className="text-sm text-slate-700">
            Les cookies et technologies de stockage utilisés par EduTutor IA sont détaillés
            dans la politique de gestion des cookies.
          </p>
        </section>
      </div>
    </LegalScaffold>
  );
}