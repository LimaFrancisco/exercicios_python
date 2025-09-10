valor = float(input("Informe um valor inicial: "))
taxa_de_juros = float(input("Informe o percentual do juros: "))
tempo = float(input("Informe o tempo em meses: "))

juros = valor * (taxa_de_juros / 100) * tempo

print(f"O valor do juros acrecentado ser R$ {juros:.2f}")