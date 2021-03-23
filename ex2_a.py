# Exercício 2
# a) m = 200, a1= 0.62, 1 < k <500_0000

# Precisaremos da biblioteca mathplotlib do PyPlot para que possamos fazer o gráfico
# Precisaremos da biblioteca NumPy importada como np
# Precisaremos importar a biblioteca math do Python 3

import matplotlib.pyplot as plt
import numpy as np
import math


# Função espalhamento da multiplicação
# h(k) = chão((m*(resto da divisão(K*a1))))
# Utilizada a função fmod para calcular o módulo de um valor, que nesse caso
# calcula também valores negativos
# É utilizada a função chão math.floor para calcular o menor inteiro de 
# um número e sua fração


def espalhamento_mult(m, k, a1):
      return math.floor((m * (math.fmod((k * a1), 1))))



# É requisitado que o usuário informe um valor da variável "m"
# O programa inicializa um vetor h para os valores h(x) da função espalhamento
# É requisitado do usuário que entre um valor inferior "k1" e superior "k2" para o intervalo de 
# valores de k.

 
m = int(input("Entre com um valor para m: "))
a1 = float(input("Entre com um valor para a1 entre 0 e 1: "))

#Teste do escopo de a1 que somente aceitará valores entre 0 e 1

while a1 < 0 or a1 > 1:
    a1 = float(input("Erro! Entre com um valor para A entre 0 e 1: "))

k1 = int(input("Entre com um valor para o início do intervalo da chave k: "))
k2 = int(input("Entre com um valor para o final do intervalo da chave k: "))



# criado um vetor de zeros para somar a quantidade de colisões para h(k) repetido
soma_espalha = np.zeros(m)

#criado um vetor para armazenar o valor da chave k na primeira posição e o valor de h(k) na segunda

espalha = []

for j in range(k1,k2):
    # criada uma variável temporária para armazenar a quantidade das colisões
    tmp = int(espalhamento_mult(m, j, a1))
    # o contador irá contar cada repetição de valor de h(k) para chaves k distintas
    soma_espalha[tmp] += 1
    # o valor da chave k será armazenado na primeira posiçào e h(k) que é espalhamento_div(j, m) será 
    # armazenado na segunda posição
    espalha.append((j, espalhamento_mult(m, j, a1)))
# print(espalha)



# Criado outro vetor com nome de "tabela_dispersao" para armazenar os valores das colisões
# É percorrido o vetor e é exibida as ocorrências de colisão para cada h(k) respectivo

tabela_dispersao = []
for i in range(m):
    tabela_dispersao.append((int(i), int(soma_espalha[i])))
# Código opcional para associar o valor de colisões a cada h(k) e exibi-lo na tela
#     print('A quantidade de repetiçoes de h(k) = ' + str(i) + ' é ' + str(int(soma_espalha[i])))


# Criando um vetor numpy de uma lista de lista
np_dis = np.array(tabela_dispersao)



# O vetor com a quantidade de colisões é separado em dois vetores
# O eixo x conterá o valor de h(k) e y conterá o número de colisões

x = [x for x, y in np_dis]
y = [y for x, y in np_dis]


# Com o comando plt.title é atribuído um título ao gráfico
# Com o comando plt.xlabel é dado um título ao eixo x
# que é o eixo com o valor da função espalhamento
# Com o comando plt.ylabel é atribuído um título ao eixo y
# plt.sactter(x, y) cria um gráfico de espalhamento para os valores
# Com o comando plt.show o gráfico é exibido.


plt.title("Espalhamento da multiplicação")
plt.xlabel("h(k) = Função de espalhamento")
plt.ylabel("Número de colisões")
plt.scatter(x,y)
plt.show()