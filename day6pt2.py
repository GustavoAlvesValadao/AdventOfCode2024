def detectar_loops(mapa):
    direcoes = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
    n_linhas = len(mapa)
    n_colunas = len(mapa[0])

    for i in range(n_linhas):
        for j in range(n_colunas):
            if mapa[i][j] in '^v><':
                x_inicial, y_inicial = i, j
                direcao_inicial = '^v><'.index(mapa[i][j])
                break

    def simular_com_obstaculo(mapa, obstaculo_x, obstaculo_y):
        x, y = x_inicial, y_inicial
        direcao = direcao_inicial

        mapa_temp = [linha[:] for linha in mapa]
        mapa_temp[obstaculo_x][obstaculo_y] = 'O'

        visitadas = set()
        estado_guardas = set() 

        while True:
            estado_atual = (x, y, direcao)

            if estado_atual in estado_guardas:
                return True 
            estado_guardas.add(estado_atual)

            visitadas.add((x, y))

            nx, ny = x + direcoes[direcao][0], y + direcoes[direcao][1]

            if not (0 <= nx < n_linhas and 0 <= ny < n_colunas):
                break  

            if mapa_temp[nx][ny] in '#O':
                direcao = (direcao + 1) % 4  
            else:
                x, y = nx, ny

        return False  

    posicoes_livres = [
        (i, j)
        for i in range(n_linhas)
        for j in range(n_colunas)
        if mapa[i][j] == '.' and (i, j) != (x_inicial, y_inicial)
    ]

    posicoes_validas = []
    for x, y in posicoes_livres:
        if simular_com_obstaculo(mapa, x, y):
            posicoes_validas.append((x, y))

    return posicoes_validas


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

posicoes_validas = detectar_loops(mapa)

print(f"Há {len(posicoes_validas)} posições possíveis para criar um loop.")
print("Posições válidas:", posicoes_validas)
