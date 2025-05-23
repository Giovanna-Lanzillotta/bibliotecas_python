import random

# random.sample(lista,k) escolhe k elementos de uma lista.tupla
cores = ["🟡amarelo","🔵azul","🟢verde","🔴vermelho","🟠laranja","⚫preto","⚪branco"]
cores_sorteadas = random.sample(cores,4)
print(f"As cores sorteadas são: {cores_sorteadas}")