salario_bruto = float(input('Digite o salário bruto: '))

if salario_bruto < 1257.12:
    imposto = salario_bruto * 0
elif 1.2357 < salario_bruto < 2.510:
    imposto = salario_bruto * 0.17
else:
    imposto = salario_bruto * 0.28

salario_liquido = salario_bruto - imposto

print(f'Seu salário bruto é de: {salario_bruto:.2f}')
print(f'Seu salário liquido é de {salario_liquido:.2f}')
print(f'O valor do imposto é de: {imposto:.2f}')