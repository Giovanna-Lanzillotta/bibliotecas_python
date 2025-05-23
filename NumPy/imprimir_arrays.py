import numpy as np

# 1d array ("lista")
matriz_a = np.arange(6)   # uma array com 5 elemento                 
print(matriz_a)

# 2d array (matriz)
matriz_b = np.arange(12).reshape(4, 3)  # 4 linhas , 3 colunas , 12 elementos
print(matriz_b)

# 3d array
c = np.arange(24).reshape(2, 3, 4)  # 2 arrays com 3 linhas e 4 colunas, 24 elementos
print(c)

