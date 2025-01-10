def inicializar_entrada():
    mapa = [
        ['#','#','#','#','#','#','#','#'],
        ['#','.','.','O','.','O','.','#'],
        ['#','#','@','.','O','.','.','#'],
        ['#','.','.','.','O','.','.','#'],
        ['#','.','#','.','O','.','.','#'],
        ['#','.','.','.','O','.','.','#'],
        ['#','.','.','.','.','.','.','#'],
        ['#','#','#','#','#','#','#','#'],
    ]

    comandos = '<^^>>>vv<v>>v<<'

    return mapa, comandos

def obter_posicao_inicial(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "@":
                return i, j
    return None

def mover_para(atual, direcao, mapa):
    nova_x, nova_y = atual[0] + direcao[0], atual[1] + direcao[1]
    mapa[nova_x][nova_y] = mapa[atual[0]][atual[1]]
    mapa[atual[0]][atual[1]] = "."

def atualizar_posicao(atual, direcao):
    return atual[0] + direcao[0], atual[1] + direcao[1]

COMANDOS = {
    "<": (0, -1), 
    "^": (-1, 0), 
    ">": (0, 1), 
    "v": (1, 0), 
}

def avaliar_mapa(mapa, comandos, inicio):
    atual = inicio
    for comando in comandos:
        direcao = COMANDOS[comando]
        nova_x, nova_y = atual[0] + direcao[0], atual[1] + direcao[1]
        
        if mapa[nova_x][nova_y] == "#":
            continue  
        
        if mapa[nova_x][nova_y] == ".":
            mover_para(atual, direcao, mapa)
            atual = atualizar_posicao(atual, direcao)
        
        elif mapa[nova_x][nova_y] == "O":
            while mapa[nova_x][nova_y] == "O":
                nova_x, nova_y = nova_x + direcao[0], nova_y + direcao[1]
            if mapa[nova_x][nova_y] == "#":
                continue

            while (nova_x, nova_y) != atual:
                nova_x, nova_y = nova_x - direcao[0], nova_y - direcao[1]
                mover_para((nova_x, nova_y), direcao, mapa)

            atual = atualizar_posicao(atual, direcao)

def calcular_resultado(mapa):
    resultado = 0
    for i in range(1, len(mapa) - 1):
        for j in range(1, len(mapa[0]) - 1):
            if mapa[i][j] == "O":
                resultado += 100 * i + j  
    return resultado

mapa, comandos = inicializar_entrada()

inicio = obter_posicao_inicial(mapa)

avaliar_mapa(mapa, comandos, inicio)

resultado = calcular_resultado(mapa)

print(f"Resultado: {resultado}")
