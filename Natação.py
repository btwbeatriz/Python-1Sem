# Leia a  idade de um nadador e apresente sua categoria
# 5 - 7   - infantil A
# 8 - 10  - infantil b
# 11 - 13 - juvenil a
# 14 - 17 - juvenil b
# maiores de 18 - senior


idade = int(input("Digite a idade: "))

while idade < 5:  # Garantindo um valor válido
    print("Inválido, só aceitamos crianças a partir de 5 anos.")
    idade = int(input("Digite a idade: "))

if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10:
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Sênior"

print(f"Obrigado(a)! Sua categoria é {categoria}")
