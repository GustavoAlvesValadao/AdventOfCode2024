def contar_palavras_X(caça_palavras):
    n_linhas = len(caça_palavras)
    n_colunas = len(caça_palavras[0])
    contador = 0
    resultados = []

    def verificar_X(linha, coluna):
        nonlocal contador

        # diagonais M e S com A no centro
        if linha - 1 >= 0 and coluna - 1 >= 0 and linha + 1 < n_linhas and coluna + 1 < n_colunas:
            if (caça_palavras[linha - 1][coluna - 1] == 'M' and
                caça_palavras[linha + 1][coluna + 1] == 'S' and
                caça_palavras[linha + 1][coluna - 1] == 'M' and
                caça_palavras[linha - 1][coluna + 1] == 'S'):
                contador += 1
                resultados.append(f"M.A.S encontrado no A ({linha},{coluna})")

        # diagonais S e M com A no centro
        if linha - 1 >= 0 and coluna - 1 >= 0 and linha + 1 < n_linhas and coluna + 1 < n_colunas:
            if (caça_palavras[linha - 1][coluna - 1] == 'S' and
                caça_palavras[linha + 1][coluna + 1] == 'M' and
                caça_palavras[linha + 1][coluna - 1] == 'S' and
                caça_palavras[linha - 1][coluna + 1] == 'M'):
                contador += 1
                resultados.append(f"S.A.M encontrado no A ({linha},{coluna})")

        # diagonais M e M com A no centro
        if linha - 1 >= 0 and coluna + 1 < n_colunas and linha + 1 < n_linhas and coluna - 1 >= 0:
            if (caça_palavras[linha - 1][coluna - 1] == 'M' and
                caça_palavras[linha - 1][coluna + 1] == 'M' and
                caça_palavras[linha + 1][coluna - 1] == 'S' and
                caça_palavras[linha + 1][coluna + 1] == 'S'):
                contador += 1
                resultados.append(f"M.M.A encontrado no A ({linha},{coluna})")

        # diagonais S e S com A no centro
        if linha - 1 >= 0 and coluna + 1 < n_colunas and linha + 1 < n_linhas and coluna - 1 >= 0:
            if (caça_palavras[linha - 1][coluna - 1] == 'S' and
                caça_palavras[linha - 1][coluna + 1] == 'S' and
                caça_palavras[linha + 1][coluna - 1] == 'M' and
                caça_palavras[linha + 1][coluna + 1] == 'M'):
                contador += 1
                resultados.append(f"S.S.A encontrado no A ({linha},{coluna})")

    for linha in range(1, n_linhas - 1):
        for coluna in range(1, n_colunas - 1):
            if caça_palavras[linha][coluna] == 'A':
                verificar_X(linha, coluna)

    return contador, resultados

caça_palavras = [
    ['M','M','M','S','X','X','M','A','S','M'],
    ['M','S','A','M','X','M','S','M','S','A'],
    ['A','M','X','S','X','M','A','A','M','M'],
    ['M','S','A','M','A','S','M','S','M','X'],
    ['X','M','A','S','A','M','X','A','M','M'],
    ['X','X','A','M','M','X','X','A','M','A'],
    ['S','M','S','M','S','A','S','X','S','S'],
    ['S','A','X','A','M','A','S','A','A','A'],
    ['M','A','M','M','M','X','M','M','M','M'],
    ['M','X','M','X','A','X','M','A','S','X'],
]

contador, resultados = contar_palavras_X(caça_palavras)
print(f"Total de ocorrências de 'MAS': {contador}")
for resultado in resultados:
    print(resultado)
