credito = float(input('Digite seu crédito: '))
total = 0

quero_comprar = input('Gostaria de comprar? (s/n)')
while(quero_comprar == 's'):
    preco = float(input('Preço do Produto: '))
    if preco <= credito:
        print('Compra Aprovada')
        total += preco
        credito -= preco
        print(f'Crédito Restatante: {credito:.2f}')
        quero_comprar = input('Continuar? (s/n)')
        if quero_comprar != 's':
            break
    else:
        print('Compra não autorizada')
        print(f'Crédito restante: R$ {credito:.2f}')

if total > 0:
    print(f'Total: R$ {total:.2f}')

print('=====================')
print('Tudo bem... Obrigado!')
print(f'Crédito: R$ {credito:.2f}')
print('=====================')