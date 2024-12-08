def encontrar_antinodos(mapa):
    antenas = []
    for y, linha in enumerate(mapa):
        for x, char in enumerate(linha):
            if char != '.':
                antenas.append((char, x, y)) 

    antinodos = set()

    for i in range(len(antenas)):
        for j in range(i + 1, len(antenas)):
            freq1, x1, y1 = antenas[i]
            freq2, x2, y2 = antenas[j]

            if freq1 == freq2: 
                dx, dy = x2 - x1, y2 - y1

                x, y = x1, y1
                while 0 <= x < len(mapa[0]) and 0 <= y < len(mapa):
                    if (x, y) != (x1, y1) and (x, y) != (x2, y2):
                        antinodos.add((x, y))
                    x += dx
                    y += dy

                x, y = x1 - dx, y1 - dy
                while 0 <= x < len(mapa[0]) and 0 <= y < len(mapa):
                    antinodos.add((x, y))
                    x -= dx
                    y -= dy

    for _, x, y in antenas:
        antinodos.add((x, y))

    mapa_resultado = [list(linha) for linha in mapa]
    for x, y in antinodos:
        if mapa_resultado[y][x] == '.':
            mapa_resultado[y][x] = '#'

    return len(antinodos), [''.join(linha) for linha in mapa_resultado]

mapa = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]

resultado, mapa_resultado = encontrar_antinodos(mapa)
print(f"Locais únicos com antinodos: {resultado}")
print("\nMapa com antinodos:")
for linha in mapa_resultado:
    print(linha)
