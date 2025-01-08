from collections import defaultdict

def blink_optimized_count(pedras_count):
    nova_contagem = defaultdict(int)

    for pedra, count in pedras_count.items():
        if pedra == 0:
            nova_contagem[1] += count
        elif len(str(pedra)) % 2 == 0:
            metade = len(str(pedra)) // 2
            esquerda = int(str(pedra)[:metade])
            direita = int(str(pedra)[metade:])
            nova_contagem[esquerda] += count
            nova_contagem[direita] += count
        else:
            nova_contagem[pedra * 2024] += count

    return nova_contagem

def contar_pedras_75(pedras_iniciais, piscadas):
    pedras_count = defaultdict(int)

    for pedra in pedras_iniciais:
        pedras_count[pedra] += 1

    for _ in range(piscadas):
        pedras_count = blink_optimized_count(pedras_count)

    total_pedras = sum(pedras_count.values())

    return total_pedras

pedras_iniciais = [125, 17]
piscadas = 75

resultado = contar_pedras_75(pedras_iniciais, piscadas)
print(f"Número de pedras após {piscadas} piscadas: {resultado}")
