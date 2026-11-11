from pile import Pile

PAIRES = {")":"(", "]":"[", "}":"{"}

def est_equilibre(texte):
    pile = Pile()
    for caractere in texte:
        if caractere in "([{":
            pile.empiler(caractere)
        elif caractere in PAIRES:
            if pile.est_vide() or pile.depiler() != PAIRES[caractere]:
                return False
    return pile.est_vide()

print(est_equilibre("a[b]c"))
print(est_equilibre("(]"))
print(est_equilibre("(("))
print(est_equilibre(")("))
print(est_equilibre(""))
print(est_equilibre("a+b"))