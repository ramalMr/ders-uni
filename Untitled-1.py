def en_boyuk_elementi_tap(matrix):
    en_boyuk = matrix[0][0]
    en_boyuk_setir = 0
    en_boyuk_sutun = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > en_boyuk:
                en_boyuk = matrix[i][j]
                en_boyuk_setir = i
                en_boyuk_sutun = j

    return en_boyuk, en_boyuk_setir, en_boyuk_sutun

n = int(input("setir olc: "))
m = int(input("sutun olc: "))

matrix = []

for i in range(n):
    setir = []
    for j in range(m):
        istifadeci = int(input(f"matrixin {i+1}. setrinin {j+1}. reqem yaz: "))
        setir.append(istifadeci)
    matrix.append(setir)

en_boyuk, satir, sutun = en_boyuk_elementi_tap(matrix)

print(f"matrix max qiymet: {en_boyuk}")
print(f"setri: {satir + 1}")  
print(f"stunu: {sutun + 1}")