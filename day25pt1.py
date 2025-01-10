def converter_para_alturas(esquema):
    linhas = esquema
    num_colunas = len(linhas[0])
    alturas = [0] * num_colunas

    for col in range(num_colunas):
        for linha in linhas:
            if linha[col] == '#':
                alturas[col] += 1

    return alturas

def verificar_compatibilidade(fechadura, chave, altura_maxima):
    for altura_fechadura, altura_chave in zip(fechadura, chave):
        if altura_fechadura + altura_chave > altura_maxima:
            return False
    return True

def separar_fechaduras_e_chaves(esquemas):
    fechaduras = []
    chaves = []

    for esquema in esquemas:
        linhas = esquema
        if linhas[0].startswith("#") and linhas[-1].startswith("."):
            fechaduras.append(esquema)
        elif linhas[0].startswith(".") and linhas[-1].startswith("#"):
            chaves.append(esquema)

    return fechaduras, chaves

def contar_pares_validos(esquemas):
    fechaduras, chaves = separar_fechaduras_e_chaves(esquemas)
    altura_maxima = len(fechaduras[0])

    fechaduras_alturas = [converter_para_alturas(esquema) for esquema in fechaduras]
    chaves_alturas = [converter_para_alturas(esquema) for esquema in chaves]

    pares_validos = 0

    for fechadura in fechaduras_alturas:
        for chave in chaves_alturas:
            if verificar_compatibilidade(fechadura, chave, altura_maxima):
                pares_validos += 1

    return pares_validos

esquemas = [
    [
        "#####",
        ".####",
        ".####",
        ".####",
        ".#.#.",
        ".#...",
        "....."
    ],
    [
        "#####",
        "##.##",
        ".#.##",
        "...##",
        "...#.",
        "...#.",
        "....."
    ],
    [
        ".....",
        "#....",
        "#....",
        "#...#",
        "#.#.#",
        "#.###",
        "#####"
    ],
    [
        ".....",
        ".....",
        ".....",
        "#....",
        "#.#..",
        "#.#.#",
        "#####"
    ],
    [
        ".....",
        ".....",
        ".....",
        ".....",
        "#....",
        "##...",
        "###.."
    ]
]

resultado = contar_pares_validos(esquemas)
print("Número de pares válidos:", resultado)
