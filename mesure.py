import time
from collections import deque

N = 50000

liste =list(range(N))
debut = time.perf_counter()
while liste:
    liste.pop(0)
print("liste.pop(0) :", round(time.perf_counter() - debut, 3), "s")

file = deque(range(N))
debut = time.perf_counter()
while file:
    file.popleft()
print("deque.popleft() :", round(time.perf_counter() - debut, 3), "s")