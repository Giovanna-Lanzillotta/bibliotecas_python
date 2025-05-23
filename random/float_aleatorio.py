import random

# O #random.uniform(a,b) gera um número decimal aleatótio entre a e b
a = 1.0
b = 6.5
numeros_reais = random.uniform(a,b)
print(f"numero {numeros_reais}")
print(f"numero arredondado {numeros_reais:.2f}")