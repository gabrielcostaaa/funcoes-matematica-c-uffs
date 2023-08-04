import matplotlib.pyplot as plt
import numpy as np

# Coeficientes da função
a = -0.102
b = 1

# Intervalo de distância horizontal
x = np.linspace(0, 10, 100)  # Altere os valores para ajustar o intervalo

# Calcular altura correspondente para cada valor de x
y = a * x**2 + b * x

# Plotar o gráfico
plt.plot(x, y)
plt.xlabel('Distância Horizontal (metros)')
plt.ylabel('Altura (metros)')
plt.title('Trajetória da Bola de Basquete')

# Adicionar linhas dos eixos x e y
plt.axhline(0, color='blue', linewidth=2)
plt.axvline(0, color='blue', linewidth=2)

plt.grid(True)
plt.show()
