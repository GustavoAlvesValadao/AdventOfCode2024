def inicializar_entrada():
    mapa = [
        ['#','#','#','#','#','#','#','#','#','#'],
        ['#','.','O','.','O','.','O','O','O','#'],
        ['#','.','.','.','.','.','.','.','.','#'],
        ['#','O','O','.','.','.','.','.','.','#'],
        ['#','O','O','@','.','.','.','.','.','#'],
        ['#','O','#','.','.','.','.','.','O','#'],
        ['#','O','.','.','.','.','.','O','O','#'],
        ['#','O','.','.','.','.','.','O','O','#'],
        ['#','O','O','.','.','.','.','O','O','#'],
        ['#','#','#','#','#','#','#','#','#','#'],
    ]

    comandos = '<^^>>>vv<v>>v<<'

    mapa_duplicado = []
    for linha in mapa:
        nova_linha = []
        for bloco in linha:
            if bloco == '#':
                nova_linha += ['#', '#']
            elif bloco == 'O':
                nova_linha += ['[', ']']
            elif bloco == '.':
                nova_linha += ['.', '.']
            elif bloco == '@':
                nova_linha += ['@', '.']
        mapa_duplicado.append(nova_linha)

    return mapa_duplicado, comandos

def obter_posicao_inicial(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "@":
                return i, j
    return None

def mover_para(atual, direcao, mapa, simbolo):
    nova_x, nova_y = atual[0] + direcao[0], atual[1] + direcao[1]
    mapa[nova_x][nova_y] = simbolo
    mapa[atual[0]][atual[1]] = "."

def atualizar_posicao(atual, direcao):
    return atual[0] + direcao[0], atual[1] + direcao[1]

def cords_do_proximo_conteiner(atual, direcao, mapa):
    x, y = atual
    if mapa[x + direcao[0]][y] == "[":
        return (x + direcao[0], y), (x + direcao[0], y + 1)
    return (x + direcao[0], y - 1), (x + direcao[0], y)

def interagir_com_conteiner(atual, direcao, mapa):
    if direcao[0] == 0:
        nova_x, nova_y = atual[0] + direcao[0], atual[1] + direcao[1]
        while mapa[nova_x][nova_y] in ["[", "]"]:
            nova_x, nova_y = nova_x + direcao[0], nova_y + direcao[1]
        if mapa[nova_x][nova_y] == "#":
            return atual
        while (nova_x, nova_y) != atual:
            nova_x, nova_y = nova_x - direcao[0], nova_y - direcao[1]
            mover_para((nova_x, nova_y), direcao, mapa, mapa[nova_x][nova_y])
        return atualizar_posicao(atual, direcao)

    conteineres_ligados = [cords_do_proximo_conteiner(atual, direcao, mapa)]
    index = 0

    while index < len(conteineres_ligados):
        conteiner = conteineres_ligados[index]
        esquerda, direita = conteiner[0], conteiner[1]
        nova_x_esquerda, nova_y_esquerda = atualizar_posicao(esquerda, direcao)
        nova_x_direita, nova_y_direita = atualizar_posicao(direita, direcao)
        if (mapa[nova_x_esquerda][nova_y_esquerda] == "#"
                or mapa[nova_x_direita][nova_y_direita] == "#"):
            return atual
        if mapa[nova_x_esquerda][nova_y_esquerda] in ["[", "]"]:
            conteineres_ligados.append(cords_do_proximo_conteiner(esquerda, direcao, mapa))

        if mapa[nova_x_direita][nova_y_direita] == "[":
            conteineres_ligados.append(cords_do_proximo_conteiner(direita, direcao, mapa))

        index += 1
      
    index -= 1
    while index >= 0:
        conteiner = conteineres_ligados[index]
        esquerda, direita = conteiner[0], conteiner[1]
        mover_para(esquerda, direcao, mapa, simbolo="[")
        mover_para(direita, direcao, mapa, simbolo="]")
        index -= 1
    mover_para(atual, direcao, mapa, simbolo="@")

    return atualizar_posicao(atual, direcao)

def avaliar_mapa(mapa, comandos, inicio):
    atual = inicio
    for comando in comandos:
        direcao = {
            "<": (0, -1),
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0),
        }[comando]
        
        nova_x, nova_y = atual[0] + direcao[0], atual[1] + direcao[1]
        if mapa[nova_x][nova_y] == "#":
            continue
        if mapa[nova_x][nova_y] == ".":
            mover_para(atual, direcao, mapa, "@")
            atual = atualizar_posicao(atual, direcao)
        if mapa[nova_x][nova_y] in ["[", "]"]:
            atual = interagir_com_conteiner(atual, direcao, mapa)

def calcular_resultado(mapa):
    resultado = 0
    for i in range(1, len(mapa) - 1):
        for j in range(1, len(mapa[0]) - 1):
            if mapa[i][j] == "[":
                resultado += 100 * i + j
    return resultado

mapa, comandos = inicializar_entrada()

inicio = obter_posicao_inicial(mapa)

avaliar_mapa(mapa, comandos, inicio)

resultado = calcular_resultado(mapa)

print(f"Resultado: {resultado}")
