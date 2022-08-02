# Ler Nome, Sal fixo e vendas efetuadas no mês
# Calcular 15% das vendas totais no mês e add no sal

nome = input("Digite seu nome: ")
sal = float(input("Digite seu salário: R$"))
vendas = float(input("Digite as vendas totais: R$"))

novo_sal = sal + vendas * 0.15

print(f"Bom trabalho {nome}! Você receberá R${novo_sal:.2f} ao invés de R${sal:.2f}."
      f"Um aumento de R${novo_sal - sal:.2f}!")
