import numpy as np

n = int(input("setir sayi: "))


matrix = np.empty((n, 2), dtype=int)

for i in range(n):
    for j in range(2):
        reqrem = int(input(f"matrixin {i+1}. setrini {j+1}. reqremini girin: "))
        matrix[i][j] = reqrem


tek_setirler = matrix[::2]  
cut_setirler = matrix[1::2]  

en_boyuk_tek = np.max(tek_setirler)
en_kicik_cut = np.min(cut_setirler)

print(f"tek setrin enkesi: {en_boyuk_tek}")
print(f"cut setrin korpesi: {en_kicik_cut}")