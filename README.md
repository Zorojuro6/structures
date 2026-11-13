# Structures de données

Implémentation en Python de trois structures de données classiques : la pile, la file et la liste chaînée. Un petit programme vérifie aussi si les parenthèses d'un texte sont bien équilibrées, avec la pile.

## Contenu
- **Pile** (`pile.py`) : dernier arrivé, premier sorti. Méthodes : `empiler`, `depiler`, `sommet`, `est_vide`, `taille`.
- **Vérification de parenthèses** (`parentheses.py`) : `est_equilibre(texte)` gère `()`, `[]` et `{}` avec une pile.
- **File** (`file_attente.py`) : premier arrivé, premier sorti. Méthodes : `enfiler`, `defiler`, `premier`, `est_vide`, `taille`.
- **Liste chaînée** (`liste_chainee.py`) : des nœuds qui pointent vers le suivant. Méthodes : `ajouter_en_tete`, `ajouter_en_queue`, `vers_liste`.
- **Mesure** (`mesure.py`) : compare le retrait au début d'une liste et d'un `deque`.

## Installation
Testé avec Python 3.14 sous Windows. Aucune bibliothèque externe n'est nécessaire pour utiliser le projet.

Pour lancer les tests, installe `pytest` :

```
py -m pip install pytest
```

## Utilisation
Chaque structure est une classe qu'on importe dans ses propres programmes :

```python
from pile import Pile
from parentheses import est_equilibre

p = Pile()
p.empiler("a")
p.empiler("b")
print(p.depiler())            # affiche b
print(est_equilibre("(a[b]c)"))   # affiche True
print(est_equilibre("(]"))        # affiche False
```

Les fichiers `pile.py` et `file_attente.py` contiennent aussi une petite démonstration :

```
py pile.py
py file_attente.py
py mesure.py
```

## Pourquoi une `File` basée sur `deque` ?
Retirer le premier élément d'une liste Python oblige à décaler tous les autres : le temps croît vite avec la taille. `collections.deque` est conçu pour retirer au début sans rien décaler. Sur ma machine, pour 50 000 éléments, `mesure.py` donne environ 0,178 s pour `liste.pop(0)` contre 0,003 s pour `deque.popleft()` : un facteur d'environ 25. Passer à 100 000 éléments multiplie le temps de la liste bien plus que par deux.

## Coût des opérations
| Opération | Structure | Coût |
|---|---|---|
| `empiler` / `depiler` | Pile (liste Python) | constant |
| `enfiler` / `defiler` | File (`deque`) | constant |
| `ajouter_en_tete` | Liste chaînée | constant |
| `ajouter_en_queue` | Liste chaînée | proportionnel à la longueur (il faut parcourir la chaîne) |

## Tests
Depuis la racine du projet :

```
py -m pytest
```

Les tests vérifient :
- l'ordre de sortie : dernier arrivé premier sorti pour la pile, premier arrivé premier sorti pour la file ;
- les erreurs sur une pile ou une file vide ;
- les parenthèses, y compris les cas fermés dans le mauvais ordre, jamais fermés, fermés sans avoir été ouverts, et le texte vide ;
- l'ajout en tête et en queue de la liste chaînée, y compris sur une liste vide.

## Structure du projet
- `pile.py`, `file_attente.py`, `liste_chainee.py` : les structures
- `parentheses.py` : la vérification d'équilibre
- `mesure.py` : la comparaison de temps
- `test_pile.py`, `test_file.py`, `test_liste_chainee.py` : les tests automatiques
- `.gitignore` : exclut les caches Python et les fichiers de travail

## Limites connues
- La `Pile` s'appuie sur une liste Python et la `File` sur un `deque` : seule la liste chaînée est construite à la main avec des nœuds.
- La liste chaînée ne permet ni suppression, ni recherche, ni mesure de taille.
- `ajouter_en_queue` parcourt toute la chaîne à chaque appel.
- `est_equilibre` ne regarde que `()`, `[]` et `{}` : il ne sait pas ignorer des parenthèses placées dans des guillemets ou des commentaires.
- Aucune des structures n'est conçue pour être utilisée par plusieurs programmes en même temps.

## Améliorations futures
- Ajouter la suppression, la recherche et la taille à la liste chaînée.
- Garder un pointeur vers la queue pour rendre `ajouter_en_queue` constant.
- Ajouter une liste doublement chaînée.
- Utiliser la pile pour évaluer une expression mathématique.