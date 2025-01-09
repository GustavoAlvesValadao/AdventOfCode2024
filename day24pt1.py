
def and_gate(a, b):
    return a & b

def xor_gate(a, b):
    return a ^ b

def or_gate(a, b):
    return a | b

entradas = {
    'x00': 1,'x01': 0,'x02': 1,
    'y00': 0,'y01': 0,'y02': 0,
    }

operacoes = [
    ('x00' , 'y00', and_gate, 'z00'),
    ('x01' , 'y01', xor_gate, 'z01'),
    ('x02' , 'y02', or_gate, 'z02'),
]

resultados = {}  
pendentes = operacoes.copy()  

while pendentes:
    novas_pendentes = []
    for x, y, gate, saida in pendentes:
        if x in entradas and y in entradas:
            resultados[saida] = gate(entradas[x], entradas[y])
            entradas[saida] = resultados[saida]
        else:
            novas_pendentes.append((x, y, gate, saida))
    if len(novas_pendentes) == len(pendentes):
        print("Não foi possível resolver todas as operações. Entradas faltando:")
        for x, y, _, saida in novas_pendentes:
            print(f"  {saida}: depende de {x} e/ou {y}")
        break
    pendentes = novas_pendentes

print("Resultados:")
for saida, valor in resultados.items():
    print(f"{saida}: {valor}")
