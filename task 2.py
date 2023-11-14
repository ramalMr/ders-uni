from typing import Any
import numpy as np

n = int(input("Setr olc: "))
m = int(input("Sutun olc: "))


matrix = np.empty((n, m), dtype=int)

for i in range(n):
    for j in range(m):
        reqem = int(input(f"matrix {i+1}. setri {j+1}. reqemi yaz: "))
        matrix[i][j] = reqem


en_boyukleri = np.max(matrix, axis=1)


for i in range(n):
    print(f"{i+1}. setrin en boyuk reqremı: {en_boyukleri[i]}")
    
