import matplotlib.pyplot as plt

fig, ax = plt.subplots()

categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 30, 25]


bar_labels = ['vermelho', 'azul', 'verde', 'laranja']
bar_colors = ['tab:red', 'tab:blue',  'tab:green', 'tab:orange']

ax.bar(categorias, valores, label=bar_labels, color=bar_colors)


ax.set_title("Gráfico em Barras")
plt.xlabel("Categorias")
ax.set_ylabel("Valores")

ax.legend(title='Legenda')

plt.show()