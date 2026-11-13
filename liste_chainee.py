class Noeud:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class ListeChainee:
    def __init__(self):
        self.tete = None

    def ajouter_en_tete(self, valeur):
        self.tete = Noeud(valeur, self.tete)

    def ajouter_en_queue(self, valeur):
        nouveau = Noeud(valeur)
        if self.tete is None:
            self.tete = nouveau
            return
        courant = self.tete
        while courant.suivant is not None:
            courant = courant.suivant
        courant.suivant = nouveau

    def vers_liste(self):
        resultat = []
        courant = self.tete
        while courant is not None:
            resultat.append(courant.valeur)
            courant = courant.suivant
        return resultat

l = ListeChainee()
l.ajouter_en_tete("c")
l.ajouter_en_tete("b")
l.ajouter_en_tete("a")
print(l.vers_liste())
l.ajouter_en_queue("d")
print(l.vers_liste())
print(ListeChainee().vers_liste())