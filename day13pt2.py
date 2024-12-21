from math import gcd
from sympy import symbols, Eq, solve

def encontrar_minimo_tokens(machines):
    def resolver_maquina(Mx_A, My_A, Mx_B, My_B, Px, Py):
        a, b = symbols('a b', integer=True)

        eq1 = Eq(a * Mx_A + b * Mx_B, Px)
        eq2 = Eq(a * My_A + b * My_B, Py)

        sol = solve((eq1, eq2), (a, b), dict=True)

        menor_custo = float('inf')
        solucao_encontrada = False

        for s in sol:
            a_val = s[a]
            b_val = s[b]
            if a_val >= 0 and b_val >= 0:
                custo = 3 * a_val + b_val
                if custo < menor_custo:
                    menor_custo = custo
                    solucao_encontrada = True

        return (solucao_encontrada, menor_custo) if solucao_encontrada else (False, None)

    total_prizes = 0
    total_cost = 0

    for machine in machines:
        Mx_A, My_A = machine['A']
        Mx_B, My_B = machine['B']
        Px, Py = machine['prize']

        solucao_encontrada, custo = resolver_maquina(Mx_A, My_A, Mx_B, My_B, Px, Py)

        if solucao_encontrada:
            total_prizes += 1
            total_cost += custo

    return total_prizes, total_cost

CORRECAO = 10**13
machines = [
    {'A': (94, 34), 'B': (22, 67), 'prize': (8400 + CORRECAO, 5400 + CORRECAO)},
    {'A': (26, 66), 'B': (67, 21), 'prize': (12748 + CORRECAO, 12176 + CORRECAO)},
    {'A': (17, 86), 'B': (84, 37), 'prize': (7870 + CORRECAO, 6450 + CORRECAO)},
    {'A': (69, 23), 'B': (27, 71), 'prize': (18641 + CORRECAO, 10279 + CORRECAO)},
]

print("Novas coordenadas dos prêmios:")
for idx, machine in enumerate(machines, 1):
    Px, Py = machine['prize']
    print(f"Máquina {idx}: X={Px}, Y={Py}")

prizes, cost = encontrar_minimo_tokens(machines)
print(f"\nPrêmios conquistados: {prizes}")
print(f"Custo total: {cost}")
