idade = int(input("Infome a idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 18:
    print("Adolecente")
elif idade >= 19 and idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")