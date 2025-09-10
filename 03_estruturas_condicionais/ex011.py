operacao = 1
menu = "########## Operações ##########\n\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n0 - SAIR\n" 

while operacao != 0:
    print(menu)
    operacao = int(input("Insira o valor referente a operação desejada: "))

    match operacao:
        case 0:
            print("Finalizado!")
        case 1:
            value1, value2 = map(int, input("Infome dois valores inteiros: ").split())
            print(f"A soma entre {value1} e {value2} é {value1 + value2}")
        case 2:
            value1, value2 = map(int, input("Infome dois valores inteiros: ").split())
            print(f"A subtração entre {value1} e {value2} é {value1 - value2}")
        case 3:
            value1, value2 = map(int, input("Infome dois valores inteiros: ").split())
            print(f"A multiplicação entre {value1} e {value2} é {value1 * value2}")
        case 4:
            value1, value2 = map(int, input("Infome dois valores inteiros: ").split())
            print(f"A divisão entre {value1} e {value2} é {value1 / value2}")
        case _:
            print("Operação invalida!")