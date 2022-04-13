n = int(input('Número: '))
cont = 1

while cont <= n:
  print('cont: ', cont)
  cont+=1




inicio = int(input('Início'))
fim = int(input('Fim: '))

while inicio <= fim:
  print('Contador:', inicio)
  inicio +=1




i = int(input('Digite um número: '))
f = int(input('Digite um número: '))
if i < f:
  print('Erro...')
else:  
  while i >= f:
    print('i: ', i)
  i -= 1


n = int(input('Digite um número: '))
cont = 0

while cont < n*2:
  if cont%2 == 0:
    print('Cont: ', cont)
  cont+=1



n1 = int(input('Digite o primeiro número natural: '))

n2 = int(input('Digite o segundo número natural: '))

r = 0

while n1 >= n2:

    n1 = n1 - n2

    r = r + 1

print(r)