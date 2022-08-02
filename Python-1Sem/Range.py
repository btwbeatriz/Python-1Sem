#Crie um programa que exiba, em ordem crescente os números
#pares de 10 até 100 e, em ordem decrescente os números
#de 100 até 10

for par in range(10, 101, 2):
    print(par)

for impar in range(99, 10, -2):
    print(impar)

#Crie um programa que exiba os dias da semana   
#tupla

dias = ('Domingo', 'Segunda', 'Terça' , 'Quarta', 'Quinta', 'Sexta')

for dia in dias:
    print(dia)

#Crie um programa que leia cinco nomes e exiba a quantidade
#de nomes que começam com vogal  

nomes = [] #Criando uma lista vazia
for _ in range(5):  #iteração com números
    nome = input('Nome: ')
    nomes.append(nome)  #append - adiciona um item no fim da lista

qtd = 0
for nome in nomes: #Iteração com itens da lista
    if(nome[0] == 'A' or nome[0] == 'E' or nome[0] == 'I' or nome[0] == 'O' or nome[0] == 'U'):
        qtd += 1
print(f'{qtd} dos nomes começam com vogal')