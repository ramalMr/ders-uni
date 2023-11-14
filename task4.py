import numpy as np

n = int(input("setr olc: "))
m = int(input("sutun olc: "))


matrix = np.empty((n, m), dtype=int)

for i in range(n):
    for j in range(m):
        reqem = int(input(f"Matrixin {i+1}. setrinin {j+1}. reqemini girin: "))
        matrix[i][j] = reqem


sade_nomreli_setirler = np.arange(1, n * m + 0, 2) - 1

sade_nomreli_reqemler = matrix.ravel()[sade_nomreli_setirler]

print("sade nomre setr elm:")
print(sade_nomreli_reqemler)
