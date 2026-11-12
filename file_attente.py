from collections import deque

class File:
    def __init__(self):
        self.elements = deque()

    def enfiler(self, element):
        self.elements.append(element)

    def defiler(self):
        if self.est_vide():
            raise ValueError("la file est vide")
        return self.elements.popleft()

    def premier(self):
        if self.est_vide():
            raise ValueError("la file est vide")
        return self.elements[0]

    def est_vide(self):
        return len(self.elements) == 0

    def taille(self):
        return len(self.elements)

if __name__ == "__main__":
    f = File()
    f.enfiler("a")
    f.enfiler("b")
    f.enfiler("c")
    print(f.defiler())
    print(f.premier())
    print(f.taille())