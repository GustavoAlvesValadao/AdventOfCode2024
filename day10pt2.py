from collections import deque

def dfs_classificacao(mapa, x, y, visitados):
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if mapa[x][y] == 9:
        return 1

    visitados.add((x, y))
    trilhas_distintas = 0

    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]) and (nx, ny) not in visitados:
            if mapa[nx][ny] == mapa[x][y] + 1:
                trilhas_distintas += dfs_classificacao(mapa, nx, ny, visitados)

    visitados.remove((x, y))
    return trilhas_distintas

def calcular_classificacao(mapa):
    classificacao_total = 0

    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == 0:
                classificacao_total += dfs_classificacao(mapa, i, j, set())

    return classificacao_total

mapa_exemplo = [
    [8,9,0,1,0,1,2,3],
    [7,8,1,2,1,8,7,4],
    [8,7,4,3,0,9,6,5],
    [9,6,5,4,9,8,7,4],
    [4,5,6,7,8,9,0,3],
    [3,2,0,1,9,0,1,2],
    [0,1,3,2,9,8,0,1],
    [1,0,4,5,6,7,3,2],
]

resultado_classificacao = calcular_classificacao(mapa_exemplo)
print(f"A soma das classificações é: {resultado_classificacao}")
