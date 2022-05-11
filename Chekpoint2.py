continuar = 's'
while continuar == 's':
    n = int(input('Número: '))
    cont = 1
    while cont <= 10:
        print(f'{n} * {cont} = {n*cont}')
        cont += 1
    continuar = input('Continuar? s-n ')
print('Fim!')

#dados armazenados
user = 'Teste123'
pwd = 123

continuar = True

while continuar:
    cont = 1
    while cont <= 3:
        #dados digitados pelo usuário
        login = input('Login: ')
        senha = int(input('Senha: '))
        if login == user and senha == pwd:
            print('Login efetuado com sucesso!')
            continuar = False
            break
        else:
            cont += 1
    if cont > 3:
        print('Número de tentativas excedido!')
        print('redefina sua senha...')
        user = input('Login: ')
        pwd = int(input('Senha: '))

#Calculadora
# 8 + 3 - 2 * 9 = ?
print('(+) Adição')
print('(-) Subtração')
print('(*) Multiplicação')
print('(/) Divisão')
print('(=) Resultado')

n = int(input('Número: '))
op = input('| + | - | * | / | = |')
result = n
maior = n
menor = n

while op != '=':
    n = int(input('Número: '))
    
    #Encontra o maior e menor elemento
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    
    #Encontra o resultado das operações escolhidas pelo usuário
    if op == '+':
        result += n
    elif op == '-':
        result -= n
    elif op == '*':
        result *= n
    elif op == '/':
        result /= n
    
    op = input('| + | - | * | / | = |')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Resultado: {result}')
