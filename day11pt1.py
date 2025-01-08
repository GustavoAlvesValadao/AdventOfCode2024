def blink(pedras):
    nova_lista = []

    for pedra in pedras:
        if pedra == 0:
            nova_lista.append(1)
        elif len(str(pedra)) % 2 == 0:
            metade = len(str(pedra)) // 2
            esquerda = int(str(pedra)[:metade])
            direita = int(str(pedra)[metade:])
            nova_lista.append(esquerda)
            nova_lista.append(direita)
        else:
            nova_lista.append(pedra * 2024)

    return nova_lista

def contar_pedras_iniciais(pedras_iniciais, piscadas):
    pedras = pedras_iniciais
    for _ in range(piscadas):
        pedras = blink(pedras)
    return len(pedras)

pedras_iniciais = [125, 17]
piscadas = 25

resultado = contar_pedras_iniciais(pedras_iniciais, piscadas)
print(f"Número de pedras após {piscadas} piscadas: {resultado}")
