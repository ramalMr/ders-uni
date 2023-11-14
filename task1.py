import numpy as np


n = int(input("setir olc: "))
m = int(input("stun olc: "))


matrix = np.empty((n, m), dtype=int)

for i in range(n):
    for j in range(m):
        istifadeci = int(input(f"matrixin {i+1}. setr {j+1}. daxil et: "))
        matrix[i][j] = istifadeci

en_boyuk_istifadeci = np.max(matrix)
en_boyuk_istifadeci_index = np.argmax(matrix)
setri, stunu = np.unravel_index(en_boyuk_istifadeci_index, matrix.shape)

print(f"en boyuk qiymet: {en_boyuk_istifadeci}")
print(f"setri: {setri + 1}")
print(f"stunu: {stunu + 1}")