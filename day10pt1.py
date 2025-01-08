from collections import deque

def bfs(mapa, start_x, start_y):
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    filas = deque([(start_x, start_y)]) 
    visitados = set() 
    visitados.add((start_x, start_y))
    alcance_nove = 0 

    while filas:
        x, y = filas.popleft()

        if mapa[x][y] == 9:
            alcance_nove += 1

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]) and (nx, ny) not in visitados:
                if mapa[nx][ny] == mapa[x][y] + 1: 
                    visitados.add((nx, ny))
                    filas.append((nx, ny))

    return alcance_nove

def calcular_pontuacoes(mapa):
    pontuacao_total = 0

    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == 0:
                pontuacao_total += bfs(mapa, i, j)

    return pontuacao_total

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

resultado = calcular_pontuacoes(mapa_exemplo)
print(f"A soma das pontuações é: {resultado}")
