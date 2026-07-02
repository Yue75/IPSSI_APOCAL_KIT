/** Mentions légales. */
import LegalScaffold from './LegalScaffold';

export default function MentionsLegalesPage() {
  return (
    <LegalScaffold
      title="Mentions légales"
      intro="Informations légales obligatoires identifiant l'éditeur et l'hébergeur du site."
      sections={[]}
      isCompleted
    >
      <div className="space-y-6">
        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">1. Éditeur du service</h2>
          <p className="text-sm text-slate-700">
            EduTutor IA est une SAS au capital de 1 000 €, immatriculée au RCS de Paris
            sous le n° 912 345 678.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            Siège social : 12 rue de la Pédagogie, 75005 Paris, France.
          </p>
          <p className="text-sm text-slate-700 mt-2">Contact : contact@edututor-ia.fr</p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            2. Directeur de la publication
          </h2>
          <p className="text-sm text-slate-700">
            Le directeur de la publication est Julien Marchand.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">3. Hébergement</h2>
          <p className="text-sm text-slate-700">
            Le service et ses données sont hébergés par OVHcloud, 2 rue Kellermann,
            59100 Roubaix, France, au sein de l’Union européenne.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            Le traitement par intelligence artificielle est réalisé localement via Ollama :
            aucune donnée n’est transmise à un fournisseur tiers ni transférée hors Union
            européenne.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">
            4. Propriété intellectuelle
          </h2>
          <p className="text-sm text-slate-700">
            Les cours téléversés restent la propriété de leurs auteurs. EduTutor IA ne
            revendique aucun droit sur les supports fournis par les utilisateurs.
          </p>
          <p className="text-sm text-slate-700 mt-2">
            Les textes, interfaces, éléments graphiques et fonctionnalités propres au service
            EduTutor IA sont protégés par le droit de la propriété intellectuelle.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-slate-900 mb-1">5. Contact</h2>
          <p className="text-sm text-slate-700">
            Pour toute question juridique ou demande relative au service, vous pouvez écrire à :
            contact@edututor-ia.fr.
          </p>
        </section>
      </div>
    </LegalScaffold>
  );
}