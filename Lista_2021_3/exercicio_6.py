from random import randint

mat = []
somaColunas = [0]*10

for i in range(5):
    mat.append([0]*10)

for i in range(5):
    for j in range(10):
        mat[i][j] = randint(1, 50)

for i in range(5):
    for j in range(10): 
        if j == j:
            somaColunas[j] += mat[i][j]  

mat.append(somaColunas)

for linha in mat:
    print(linha)