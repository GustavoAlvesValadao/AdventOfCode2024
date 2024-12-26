def gerar_proximo_numero_secreto(num_secreto):
    num_secreto = num_secreto ^ (num_secreto * 64)
    num_secreto = num_secreto % 16777216 

    num_secreto = num_secreto ^ (num_secreto // 32)
    num_secreto = num_secreto % 16777216  

    num_secreto = num_secreto ^ (num_secreto * 2048)
    num_secreto = num_secreto % 16777216  
    
    return num_secreto

def soma_dos_2000_seguinte_inicial(iniciais):
    soma = 0
    for num_secreto in iniciais:
        for _ in range(2000):
            num_secreto = gerar_proximo_numero_secreto(num_secreto)
        soma += num_secreto
    return soma

iniciais = [1, 10, 100, 2024]

resultado = soma_dos_2000_seguinte_inicial(iniciais)
print(f"Soma do 2000º número secreto de cada comprador: {resultado}")
