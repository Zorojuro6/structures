from liste_chainee import ListeChainee

def test_ajouter_en_tete():
    l = ListeChainee()
    l.ajouter_en_tete(2)
    l.ajouter_en_tete(1)
    assert l.vers_liste() == [1,2]

def test_ajouter_en_queue_sur_liste_vide():
    l = ListeChainee()
    l.ajouter_en_queue("x")
    assert l.vers_liste() == ["x"]

def test_ajouter_en_queue():
    l = ListeChainee()
    l.ajouter_en_tete("b")
    l.ajouter_en_queue("c")
    l.ajouter_en_tete("a")
    assert l.vers_liste() == ["a","b","c"]