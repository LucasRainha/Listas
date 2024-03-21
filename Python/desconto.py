valor = float(input("Valor do produto: "))
desconto = float(input("Valor do desconto, em %: "))

calculo = valor * (desconto / 100)
calculo = valor - calculo  

print("Seu valor com desconto é:", calculo)
