def contar_palavras(caça_palavras, palavra):
    contador = 0
    n_linhas = len(caça_palavras)
    n_colunas = len(caça_palavras[0])


    def verificar_direcao(linha, coluna, dx, dy):

        for i in range(len(palavra)):

            nova_linha = linha + i * dx
            nova_coluna = coluna + i * dy

            if not (0 <= nova_linha < n_linhas and 0 <= nova_coluna < n_colunas):
                return False

            if caça_palavras[nova_linha][nova_coluna] != palavra[i]:
                return False
        return True


    for linha in range(n_linhas):
        for coluna in range(n_colunas):

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                if verificar_direcao(linha, coluna, dx, dy):
                    contador += 1

    return contador


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

palavra = "XMAS"
resultado = contar_palavras(caça_palavras, palavra)
print(f"A palavra '{palavra}' foi encontrada {resultado} vezes.")
