import random

# random.shuffle(lista) - Mistura os elementos de uma lista
ingredientes = ["🧁 Açucar","🧂 sal","🥚 ovo","🍞farinha"]
print(f"Ordem antes: {ingredientes}")
random.shuffle(ingredientes)
print(f"Nova ordem: {ingredientes}")