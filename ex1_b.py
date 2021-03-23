# Questão 1
# b) m = 11, 0 < k < 100, se return h == 3 print(k)

# Precisaremos importar a biblioteca math do Python 3

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
# É pedido ao usuário que insira o valor para o qual serão procuradas as colisões 
# da função de espalhamento
        
h = []
k1 = int(input("Entre com um valor para o início do intervalo da chave k: "))
k2 = int(input("Entre com um valor para o final do intervalo da chave k: "))
m = int(input("Entre com um valor para m: "))
e1 = int(input("Entre com um valor para o qual serão testadas as colisões: "))

# estrutura de repetição "for" para percorrer valores de 0 a até m
# o loop itera a função espalhamento
# o valor de h(x) é adicionado ao final de cada iteração dentro do vetor h
# Uma mensagem de imprimir com o valor de k e seu respectivo espalhamento 
# é exibida

#criado um vetor para armazenar o valor da chave k na primeira posição e o valor de h(k) na segunda

espalha = []

for i in range(k1, k2):
    if espalhamento_div(i, m) == e1:
        print("Para k = {} o espalhamento é: {}".format(i, espalhamento_div(i, m)))
        espalha.append((i, espalhamento_div(i, m)))

# Opcional, o usuário pode imprimir o vetor com todas as saídas    
# print(espalha)


# Criando um vetor numpy de uma lista de lista
np_dis = np.array(espalha)


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
plt.ylabel("Valor da colisão")
plt.scatter(x,y)
plt.show()