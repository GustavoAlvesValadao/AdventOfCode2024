from collections import Counter

numeros1 = [1, 2, 3, 3, 3, 4]
numeros2 = [3, 3, 3, 4, 5, 9]
  
contagem_numero2 = Counter(numeros2)

contagem_numeros2 = Counter(numeros2)

total = sum(numero * contagem_numeros2[numero] for numero in numeros1 if contagem_numeros2[numero] > 0)


print(f"O total é: {total}")
