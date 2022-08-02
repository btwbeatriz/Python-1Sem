#Variável contadora, utilizada para contar quantas vezes o bloco de instruções do laço foi executado e/ou controlar quantas vezes ele será executado

executa = input('Executar o bloco: ')
contador = 0 
while executa == 'sim':    
    contador += 1   
    executa = input('Executar o bloco: ')
print(f'O bloco foi executado {contador} vezes') 


contador = 10
while contador > 0:
   print(contador)   
   contador -= 1
print('Lançar!')


qtde_num = int(input('Qtde: '))
cont = 1
soma = 0
while cont <= qtde_num:
    num = int(input('Número: ')) #Entrada de dados pelo teclado
    soma += num #acumulando valor em soma
    cont += 1  #ou qtde_num -= 1
print(f'Soma: {soma}')    

#Variável acumuladora, utilizada para acumular valores que, em geral, não são constantes, ou seja, o incremento ou decremento pode ser variável. Crie um programa que receba como entrada os preços de itens comprados em um supermercado por um cliente, no final o programa deverá exibir o total da compra. Para informar que não há mais itens a serem comprados, o cliente digitar o valor -1.

total = 0
preco = float(input('Preço do item: '))  
while preco != -1:    
    total += preco     
    preco = float(input('Preço do item: '))
print(f'Total da compra: R$ {total:.2f}')

#Variável flag booleana - sinaliza com um valor booleano se o laço deve ou não ser encerrado

total = 0
quero_comprar = True
while quero_comprar:    
    preco = float(input('Preço: '))    
    total += preco    
    opcao = input('Continuar comprando (s/n)')    
    if opcao != 's':        
        quero_comprar = False
print(f'Total da compra: R$ {total:.2f}')

#Crie um programa que receba como entrada o crédito e depois o preço de itens comprados por esse cliente. O programa deverá parar de solicitar novos preços quando o crédito disponível for insuficiente para pagar por um deles. Ao final exiba o total da compra e o crédito restante

credito = float(input('Seu crédito: ')) 
total = 0 #variável acumuladora
preco = float(input('Preço do item: '))
while credito >= preco:    
    total += preco    
    credito -= preco    
    preco = float(input('Preço do item: '))
print(f'Total da compra: R$ {total:.2f}')
print(f'Crédito restante: R$ {credito:.2f}')

#Laço infinito é uma estrutura de repetição que "nunca" é encerrada, ou interrompido por um comando externo
n = 0
while n <= 10:
    print(n)
print('Fora do while')
