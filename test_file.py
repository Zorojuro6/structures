import pytest 
from file_attente import File

def test_premier_arrive_premier_sorti():
    f = File()
    f.enfiler(1)
    f.enfiler(2)
    assert f.defiler() == 1 
    assert f.defiler() == 2
    assert f.est_vide()

def test_defiler_file_vide():
    with pytest.raises(ValueError):
        File().defiler()

def test_taille_et_premier():
    f = File()
    f.enfiler("a")
    f.enfiler("b")
    assert f.premier() == "a"
    assert f.taille() == 2