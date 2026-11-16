import pytest
from notes import mention, moyenne, meilleure_note, rang


def test_rang_premier():
    assert rang(17, [17, 15, 12, 10]) == 1


def test_rang_deuxieme():
    assert rang(15, [17, 15, 12, 10]) == 2


def test_meilleure_note():
    assert meilleure_note([10, 18, 14]) == 18
    with pytest.raises(ValueError):
        meilleure_note([])


def test_moyenne():
    assert moyenne([10, 12, 14]) == 12


def test_moyenne_liste_vide():
    with pytest.raises(ValueError):
        moyenne([])


@pytest.mark.parametrize("note, attendu", [
    (17, "Très bien"),
    (15, "Bien"),
    (12.5, "Assez bien"),
    (10, "Passable"),
    (8, "Ajourné"),
])
def test_mention(note, attendu):
    assert mention(note) == attendu
