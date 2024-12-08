from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1])) 
    return result

def calibrate(equations):
    total_calibration = 0

    for equation in equations:
        test_value, *numbers = equation
        n = len(numbers) - 1 
        possible_operators = product("+*", repeat=n) 

        possible_operators_with_concat = product(["+", "*", "||"], repeat=n)

        found_valid = False
        for operators in possible_operators_with_concat:
            result = evaluate_expression(numbers, operators)
            print(f"Testando: {numbers} com operadores {operators} = {result}")
            if result == test_value:
                print(f"Encontrado: {numbers} com operadores {operators} = {test_value}")
                total_calibration += test_value
                found_valid = True
                break  
        
        if not found_valid:
            print(f"Nenhuma combinação válida para: {numbers} (valor esperado: {test_value})")

    return total_calibration

data = [
    (190, 10, 19),
    (3267, 81, 40, 27),
    (83, 17, 5),
    (156, 15, 6),
    (7290, 6, 8, 6, 15),
    (161011, 16, 10, 13),
    (192, 17, 8, 14),
    (21037, 9, 7, 18, 13),
    (292, 11, 6, 16, 20),
]

result = calibrate(data)
print("\nResultado total da calibração:", result)
