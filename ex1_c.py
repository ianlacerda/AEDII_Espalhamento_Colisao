# Questão 1
# c) m = 97, 0 < k < 10000, contar quantas colisões tem para cada valor de função

# Precisaremos da biblioteca mathplotlib do PyPlot para que possamos fazer o gráfico
# Precisaremos da biblioteca NumPy importada como np
# Precisaremos importar a biblioteca math do Python 3


import csv
import matplotlib.pyplot as plt
import numpy as np
import math


# Função espalhamento
#  k mod m
# Utilizada a função fmod para calcular o módulo de um valor, que nesse caso
# calcula também valores negativos

def espalhamento_div(k, m):
    
    return math.fmod(k, m)
    
# O programa inicializa um vetor h para os valores h(x) da função espalhamento
# É requisitado do usuário que entre um valor inferior "k1" e superior "k2" para o intervalo de 
# valores de k.
# É requisitado que o usuário informe um valor do operador de módulo

k1 = int(input("Entre com um valor para o início do intervalo da chave k: "))
k2 = int(input("Entre com um valor para o final do intervalo da chave k: "))
m = int(input("Entre com um valor para m: "))



# É criado um vetor de zeros através da biblioteca NumPy
# para somar a quantidade de colisões para h(k) repetido

soma_espalha = np.zeros(m)
# print(soma_espalha)

#criado um vetor para armazenar o valor da chave k na primeira posição e o valor de h(k) na segunda

espalha = []

for j in range(k1,k2):
    # criada uma variável temporária para armazenar a quantidade das colisões
    tmp = int(espalhamento_div(j, m))
    # o contador irá contar cada repetição de valor de h(k) para chaves k distintas
    soma_espalha[tmp] += 1
    # o valor da chave k será armazenado na primeira posiçào e h(k) que é espalhamento_div(j, m) será 
    # armazenado na segunda posição
    espalha.append((j, espalhamento_div(j, m)))

# Opcional, o usuário pode imprimir o vetor com todas as saídas    
# print(espalha)


# Criado outro vetor com nome de "tabela_dispersao" para armazenar os valores das colisões
# É percorrido o vetor e é exibida as ocorrências de colisão para cada h(k) respectivo

tabela_dispersao = []
for i in range(m):
    # Opcional: imprimir na tela todos h(k) e suas colisões
#     print('A quantidade de repetiçoes de h(k) = ' + str(i) + ' é ' + str(int(soma_espalha[i])))
    tabela_dispersao.append((int(i), int(soma_espalha[i])))
    
# Opcional: imrpimir todos os valores de h(k) e suas colisões na tela
# print(tabela_dispersao)

# Função open para abrir o arquivo ex1c.csv e imprimir os valores do
# resultado da função h(k) e a quantidade de suas colisões

with open('ex1c.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(tabela_dispersao)

# Criando um vetor numpy de uma lista de lista
np_dis = np.array(tabela_dispersao)



# [[x1, y1], [x2, y2], ...]]

# O vetor com a quantidade de colisões é separado em dois vetores
# O eixo x conterá o valor de h(k) e y conterá o número de colisões

x = [x for x, y in np_dis]
y = [y for x, y in np_dis]

# plt.plot(x, y)
# plt.show()


# Com o comando plt.title é atribuído um título ao gráfico
# Com o comando plt.xlabel é dado um título ao eixo x
# que é o eixo com o valor da função espalhamento
# Com o comando plt.ylabel é atribuído um título ao eixo y
# plt.sactter(x, y) cria um gráfico de espalhamento para os valores
# Com o comando plt.show o gráfico é exibido.

# print(np_dis)
plt.title("Espalhamento da divisão")
plt.xlabel("h(k) = Função de espalhamento")
plt.ylabel("Número de colisões")
plt.scatter(x,y)
plt.show()