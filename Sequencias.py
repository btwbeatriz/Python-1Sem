#Textos
texto = 'Adoro Python'
print(texto)
print(len(texto))
print(texto[0])
print(texto[4])
print(texto[7])
print(texto[11])

#Listas
lista = []
print(lista)
lista = [3.14, True, 29, 'Oi']
print(lista)
print(len(lista))
print(lista[3])
lista[3] = 'Tchau'
print(lista)
print(lista[3])

#Tuplas
tupla = ()
tupla = (123,)
print(tupla)
tupla = (3.14, True, 29, 'Oi')
print(tupla)
print(len(tupla))
print(tupla[1])
print(tupla[3])
#tupla[1] = False  #Sequência imutável, não permite alteração

#Range
intervalo = range(5,10,2)
print(intervalo)
lista = list(intervalo)
print(lista)
tupla = tuple(intervalo)
print(tupla)
#intervalo[0] = 77  #Sequência imutável, não permite alteração
#print(intervalo[0])

#Sem sequência
soma = 0
salario_0 = float(input('Salário: '))
soma += salario_0
salario_1 = float(input('Salário: '))
soma += salario_1
salario_2 = float(input('Salário: '))
soma += salario_2
salario_3 = float(input('Salário: '))
soma += salario_3

media = soma/4

if salario_0 < media:
    print(f'Abaixo da média: R$ {salario_0:.2f}')
if salario_1 < media:
    print(f'Abaixo da média: R$ {salario_1:.2f}')
if salario_2 < media:
    print(f'Abaixo da média: R$ {salario_2:.2f}')
if salario_3 < media:
    print(f'Abaixo da média: R$ {salario_3:.2f}')

#Com sequência
salario = [0,0,0,0,]
soma = 0
salario[0] = float(input('Salário: '))
soma += salario[0]
salario[1] = float(input('Salário: '))
soma += salario[1]
salario[2] = float(input('Salário: '))
soma += salario[2]
salario[3] = float(input('Salário: '))
soma += salario[3]

media = soma/4

if salario[0] < media:
    print(f'Abaixo da média: R$ {salario[0]:.2f}')
if salario[1] < media:
    print(f'Abaixo da média: R$ {salario[1]:.2f}')
if salario[2] < media:
    print(f'Abaixo da média: R$ {salario[2]:.2f}')
if salario[3] < media:
    print(f'Abaixo da média: R$ {salario[3]:.2f}')

#Com laço de repetição
salario = [0,0,0,0,]
soma = 0
i = 0
while i < 4: #len(salario)
    salario[i] = float(input('Salário: '))
    soma += salario[i]
    i += 1
media = soma /len(salario)

i = 0
while i < 4:
    if salario[i] < media:
        print(f'Abaixo da média: R$ {salario[i]:.2f}')
    i += 1
