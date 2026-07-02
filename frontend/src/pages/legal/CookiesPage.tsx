/** Politique de gestion des cookies. */
import LegalScaffold from './LegalScaffold';

export default function CookiesPage() {
  return (
    <LegalScaffold
      title="Politique de gestion des cookies"
      intro="Les cookies et technologies de stockage utilisés par le site, et comment les gérer."
      sections={[]}
      isCompleted
    >
      <div className="space-y-6">
        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            1. Cookies et stockage utilisés
          </h2>
          <p className="text-sm text-slate-700">
            EduTutor IA utilise uniquement des cookies ou technologies de stockage strictement
            nécessaires au fonctionnement du service, notamment pour maintenir la session
            d’authentification de l’utilisateur.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            Le kit peut également utiliser le stockage local du navigateur pour conserver un jeton
            d’authentification technique nécessaire à l’accès au compte.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            2. Finalité de chaque cookie
          </h2>
          <p className="text-sm text-slate-700">
            Ces éléments servent uniquement à permettre la connexion, sécuriser l’accès au service
            et maintenir l’utilisateur authentifié pendant sa navigation.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            EduTutor IA n’utilise aucun cookie publicitaire, aucun traceur tiers et aucun outil de
            suivi commercial.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">3. Consentement</h2>
          <p className="text-sm text-slate-700">
            Les cookies strictement nécessaires au fonctionnement du service ne requièrent pas de
            consentement préalable. Aucun traceur de mesure d’audience non exempté n’est déposé
            sans accord de l’utilisateur.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            4. Durée de conservation
          </h2>
          <p className="text-sm text-slate-700">
            Les cookies et éléments de stockage strictement nécessaires sont conservés uniquement
            pendant la durée utile au fonctionnement de la session et à la sécurité du compte.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            5. Gérer ou refuser les cookies
          </h2>
          <p className="text-sm text-slate-700">
            Vous pouvez configurer votre navigateur pour refuser ou supprimer les cookies.
            Toutefois, le refus des cookies strictement nécessaires peut empêcher l’authentification
            ou dégrader le fonctionnement du service.
          </p>
        </section>
      </div>
    </LegalScaffold>
  );
}