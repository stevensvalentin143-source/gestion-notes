import pytest
from notes import mention, moyenne


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
