"""Petit module de gestion de notes d'étudiants."""


def moyenne(notes):
    """Moyenne d'une liste de notes sur 20, arrondie à 2 décimales."""
    if not notes:
        raise ValueError("La liste de notes est vide")
    return round(sum(notes) / len(notes), 2)


def mention(note):
    """Mention obtenue pour une moyenne sur 20."""
    if note >= 17:
        return "Très bien"
    if note >= 13.5:
        return "Bien"
    if note >= 12:
        return "Assez bien"
    if note >= 10:
        return "Passable"
    return "Ajourné"
def meilleure_note(notes):
    """retourne la note la plus élevée d'une liste."""
    if not notes:
        raise ValueError("la liste de notes est vide")
    return max(notes)