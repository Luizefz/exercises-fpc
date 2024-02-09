def percorrer_fazenda(tabela_fazenda, coor_visitada, i, j, quant_ovelha, quant_lobo):
    #Caso base, se a Linha/Coluna exceder o limite da tabela ou a coordenada já foi visitada ou ele achou o limite da cerca.
    if i < 0 or j < 0 or i >= len(tabela_fazenda) or j >= len(tabela_fazenda[0]) or coor_visitada[i][j] == True or tabela_fazenda[i][j] == "#":
        return  quant_ovelha, quant_lobo
    
    #Sinaliza em uma matriz que já visitou aquela coordenada.
    coor_visitada[i][j] = True

    match (tabela_fazenda[i][j]):
        case "k":
            quant_ovelha += 1
        case "v":
            quant_lobo += 1

    #Sai andando por todas as direções até bater em uma das delimitações no pasto. Se achar um bicho, soma na respectiva variavel.
    quant_ovelha, quant_lobo = percorrer_fazenda(tabela_fazenda, coor_visitada, i+1, j, quant_ovelha, quant_lobo)
    quant_ovelha, quant_lobo = percorrer_fazenda(tabela_fazenda, coor_visitada, i-1, j, quant_ovelha, quant_lobo)
    quant_ovelha, quant_lobo = percorrer_fazenda(tabela_fazenda, coor_visitada, i, j+1, quant_ovelha, quant_lobo)
    quant_ovelha, quant_lobo = percorrer_fazenda(tabela_fazenda, coor_visitada, i, j-1, quant_ovelha, quant_lobo)

    #Por fim, retorna a soma da quantidade de bicho que ele achou.
    return quant_ovelha, quant_lobo

fazenda_dimensoes = [int(i) for i in input().split()]
tabela_fazenda = [input() for _ in range(fazenda_dimensoes[0])]
coor_visitada = [[False for _ in range(fazenda_dimensoes[1])] for _ in range(fazenda_dimensoes[0])]
quant_ovelha, quant_lobo = 0, 0

for i in range(fazenda_dimensoes[0]):
        for j in range(fazenda_dimensoes[1]):
                ovelhas, lobos = percorrer_fazenda(tabela_fazenda, coor_visitada, i, j, 0, 0)
                if ovelhas > lobos:
                    quant_ovelha += ovelhas
                else: 
                    quant_lobo += lobos

print(quant_ovelha, quant_lobo)