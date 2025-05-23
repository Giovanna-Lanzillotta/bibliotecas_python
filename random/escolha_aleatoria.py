import random

# O random.choice() escolhe um elemento aleatório de uma sequência como uma lista,tupla,...
animais = ["🦆 pato","🐈 gato","🐀 rato","🐸 sapo"]
animal_sorteado = random.choice(animais)
print(f"O animal sorteado foi: {animal_sorteado}")

estacoes = ["⛄ inverno","🌼 primavera","🍂 outono","🌞 verão"]
estacao_sorteada = random.choice(estacoes)
print(f"A estação sorteada foi: {estacao_sorteada}")