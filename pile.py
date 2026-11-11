class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if self.est_vide():
            raise ValueError("la pile est vide")
        return self.elements.pop()

    def sommet(self):
        if self.est_vide():
            raise ValueError("la pile est vide")
        return self.elements[-1]

    def est_vide(self):
        return len(self.elements) == 0

    def taille(self):
        return len(self.elements)


if __name__ == "__main__":
    p = Pile()
    p.empiler("a")
    p.empiler("b")
    p.empiler("c")
    print(p.depiler())
    print(p.sommet())
    print(p.taille())