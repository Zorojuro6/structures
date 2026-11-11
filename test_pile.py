import pytest

from pile import Pile
from parentheses import est_equilibre

def test_dernier_arrive_avant_premier_sorti():
    p = Pile()
    p.empiler(1)
    p.empiler(2)
    assert p.depiler() == 2
    assert p.depiler() == 1
    assert p.est_vide()

def test_depiler_pile_vide():
    with pytest.raises(ValueError):
        Pile().depiler()

@pytest.mark.parametrize("texte, attendu", [
    ("a[b]c", True),
    ("(]", False),
    ("((", False),
    (")(", False),
    ("", True),
])
def test_equilibre(texte, attendu):
    assert est_equilibre(texte) == attendu