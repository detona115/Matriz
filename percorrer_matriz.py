tabuleiro =[[1,1,1,1],[0,1,1,0],[0,1,0,1],[0,1,9,1],[1,1,1,1]]

#tabuleiro =[[1,1,1,1],[0,1,1,0],[9,1,0,1],[0,1,0,1],[1,1,1,1]]

path = []
encontrado = None

for i in range(len(tabuleiro[0]) +1): #loop que percorre o eixo y
    for j in range(len(tabuleiro) - 1): #loop que percorre o eixo x
        if tabuleiro[i][j] == 0: #para cada nó tendo o valor 0 pular
            continue
        else:            
            if tabuleiro[i][j] == 9:
                encontrado = (j, i, tabuleiro[i][j])
            path.append((j, i, tabuleiro[i][j]))
print('Todos os caminhos do tabuleiro são :',path)
print('O dois primeiros nós são a posições e o terceiro é o valor encontrado',encontrado)