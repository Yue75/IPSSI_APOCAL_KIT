/** Conditions Générales d'Utilisation. */
import LegalScaffold from './LegalScaffold';

export default function CGUPage() {
  return (
    <LegalScaffold
      title="Conditions Générales d'Utilisation"
      intro="Les règles d'utilisation du service EduTutor IA, acceptées par chaque utilisateur."
      sections={[]}
      isCompleted
    >
      <div className="space-y-6">
        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">1. Objet</h2>
          <p className="text-sm text-slate-700">
            Les présentes conditions générales d’utilisation régissent l’accès et l’usage
            d’EduTutor IA, service de génération de quiz de révision à partir de cours fournis
            par l’utilisateur.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">2. Accès au service</h2>
          <p className="text-sm text-slate-700">
            L’inscription requiert une adresse email valide. L’utilisateur est responsable de la
            confidentialité de ses identifiants et de l’usage de son compte.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">3. Usage acceptable</h2>
          <p className="text-sm text-slate-700">
            L’utilisateur s’engage à ne téléverser que des contenus dont il détient les droits
            ou pour lesquels il dispose d’une autorisation suffisante.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            Il s’engage également à ne pas détourner le service, notamment par l’envoi de contenus
            illicites, de tentatives d’atteinte à la sécurité ou d’instructions malveillantes
            insérées dans un cours, comme des tentatives de prompt injection.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            4. Contenu généré par IA
          </h2>
          <p className="text-sm text-slate-700">
            Les quiz sont générés automatiquement par une intelligence artificielle et peuvent
            comporter des erreurs. Ils constituent une aide à la révision et ne remplacent pas
            les supports officiels, les enseignants ou le jugement de l’utilisateur.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            5. Limite de responsabilité
          </h2>
          <p className="text-sm text-slate-700">
            EduTutor IA met en œuvre des mesures raisonnables pour fournir un service fiable,
            sécurisé et utile pédagogiquement. Toutefois, l’utilisateur reste responsable de
            l’usage des quiz générés et de la vérification de leur exactitude.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">6. Résiliation</h2>
          <p className="text-sm text-slate-700">
            L’utilisateur peut supprimer son compte et ses données à tout moment depuis sa page
            profil, sous réserve des données conservées pour obligation légale ou sécurité pendant
            la durée prévue par la politique de rétention.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            7. Propriété intellectuelle
          </h2>
          <p className="text-sm text-slate-700">
            Les contenus déposés par l’utilisateur restent sa propriété ou celle de leurs auteurs.
            Les éléments propres au service EduTutor IA restent protégés par le droit de la
            propriété intellectuelle.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            8. Droit applicable
          </h2>
          <p className="text-sm text-slate-700">
            Les présentes conditions sont soumises au droit français. En cas de litige, les parties
            rechercheront une solution amiable avant toute procédure.
          </p>
        </section>
      </div>
    </LegalScaffold>
  );
}