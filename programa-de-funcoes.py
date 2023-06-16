#= == == GRÁFICO DE FUNÇÕES == == = //
import matplotlib.pyplot as plt
import numpy as np

#= == DADOS DE ENTRADA == ==

n = int(input('Digite a quantidade de valores de Y da função: '))
a = int(input('Digite o limite a esquerda do gráfico (negativo): '))  # limite à esquerda no gráfico
b = abs(int(input('Digite o limite a direita do gráfico: '))) 

coef_ang = int(input('Valor de A (coeficiente angular): '))
coef_linear = int(input('Valor de B (coeficiente linear): '))
coef_c = int(input('Digite o valor de C: '))

def F1(x):
    f = (coef_ang*x**2) - (coef_linear*x) - (coef_c)  #= == digite a expressão da função
    return f

#= == =CÁLCULO DA FUNÇÃO == == ==

x = np.linspace(a, b, n) #= == == domínio da função

y = []
for i in range(0,n): #= == cálculo dos valores de y da função
    y.append(F1(x[i]))
    print(f"y={y[i]} \n") #= == valores de x

#= == EIXOS X E Y PARA O GRÁFICO == == =

menor = 1000000 #= == cálculo do dy
maior = 0
for i in range(0,n): #= == procura do maior e menor absoluto no intervalo(a, b)
    if y[i] < menor:
        menor = y[i]
    else:
        if y[i] > maior:
            maior = y[i]

dy = 1.1 * abs((maior - menor) / (n - 1))

yy = []
X = []
yy.append(menor)
X.append(0)
for i in range(1,n): #= == cálculo dos valores de y da função
    yy.append(yy[i - 1] + dy)  #= == y do eixo Y
    X.append(0) #= == eixo X e x do eixo y

#= == =SAÍDA DE DADOS == == =

plt.plot(x, y, 'k', x, np.array(X).T, 'r', X, yy, 'r')
plt.show()