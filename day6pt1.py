def simular_patrulha(mapa):
    direcoes = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
    n_linhas = len(mapa)
    n_colunas = len(mapa[0])

    for i in range(n_linhas):
        for j in range(n_colunas):
            if mapa[i][j] in '^v><': 
                x, y = i, j
                direcao = '^v><'.index(mapa[i][j])
                mapa[i][j] = '.' 
                break

    visitadas = set()

    while True:
        visitadas.add((x, y))

        nx, ny = x + direcoes[direcao][0], y + direcoes[direcao][1]

        if not (0 <= nx < n_linhas and 0 <= ny < n_colunas):
            break  

        if mapa[nx][ny] == '#':
            direcao = (direcao + 1) % 4 
        else:
            x, y = nx, ny

    return len(visitadas)


mapa = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]

mapa = [list(linha) for linha in mapa]

resultado = simular_patrulha(mapa)
print(f"O guarda visitará {resultado} posições distintas antes de sair do mapa.")
