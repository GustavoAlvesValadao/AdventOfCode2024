def execute_program(registers, program):
    A, B, C = registers 
    output = []  
    pointer = 0  

    while pointer < len(program):
        opcode = program[pointer]  
        operand = program[pointer + 1] if pointer + 1 < len(program) else 0 

        if opcode == 0: 
            denominator = 2 ** get_operand_value(A, B, C, operand)
            A = A // denominator if denominator != 0 else 0

        elif opcode == 1: 
            B = B ^ operand

        elif opcode == 2: 
            B = get_operand_value(A, B, C, operand) % 8

        elif opcode == 3: 
            if A != 0:
                pointer = operand 
                continue 

        elif opcode == 4: 
            B = B ^ C

        elif opcode == 5: 
            output.append(get_operand_value(A, B, C, operand) % 8)

        elif opcode == 6: 
            denominator = 2 ** get_operand_value(A, B, C, operand)
            B = A // denominator if denominator != 0 else 0

        elif opcode == 7: 
            denominator = 2 ** get_operand_value(A, B, C, operand)
            C = A // denominator if denominator != 0 else 0

        pointer += 2 

    return ','.join(map(str, output))

def get_operand_value(A, B, C, operand):

    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        raise ValueError("Operando inválido!")

initial_registers = [729, 0, 0]
program = [0, 1, 5, 4, 3, 0]

result = execute_program(initial_registers, program)
print("Saída:", result)
