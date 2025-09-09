valor_produto = float(input("Informe o valor do produto: "))
desconto = float(input("Informe o valor do desconto em %: "))

produto_com_desconto = valor_produto - (valor_produto * (desconto / 100))

print(f"O valor do produto com o desconto é R${produto_com_desconto:.2f}")