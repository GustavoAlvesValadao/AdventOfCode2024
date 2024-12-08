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

                antinodo1 = (x1 - dx, y1 - dy)
                antinodo2 = (x2 + dx, y2 + dy)

                for ax, ay in [antinodo1, antinodo2]:
                    if 0 <= ax < len(mapa[0]) and 0 <= ay < len(mapa):
                        antinodos.add((ax, ay))

    return len(antinodos)

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

resultado = encontrar_antinodos(mapa)
print(f"Locais únicos com antinodos: {resultado}")
