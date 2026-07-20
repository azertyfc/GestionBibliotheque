from datetime import datetime
from models.emprunt import Emprunt
from models.penalite import Penalite


def calculer_penalite(
    emprunt: Emprunt
) -> Penalite | None:

    if emprunt.date_retour is None:
        return None

    if emprunt.date_retour <= emprunt.date_retour_prevue:
        return None

    jours_retard = (
        emprunt.date_retour -
        emprunt.date_retour_prevue
    ).days

    if jours_retard < 7:
        return None

    if jours_retard > 30:
        # Pour l'instant on ne fait rien.
        # Plus tard on suspendra le compte.
        return None

    return Penalite(
        emprunt_id=emprunt.id,
        montant=jours_retard * 2,
        motif=f"Retard de {jours_retard} jours",
        date_creation=datetime.utcnow(),
        est_paye=False
    )