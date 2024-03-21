# Exercício 1

# nome = input("Qual é o seu nome? ")
# sobrenome = input("E seu sobrenome? ")

# print(sobrenome , nome)

#------------------------------------------------------------------

# Exercício 2

# nome = input("Qual o seu nome? ")
# data = int(input("Qual o ano de seu nascimento? "))

# calc = 2024 - data

# print(nome , calc)

#------------------------------------------------------------------

# Exercício 3

# num1 = int(input('Fale um número: '))
# num2 = int(input('Fale outro: '))

# calc = num1 + num2
# valor = print("Soma:" , calc)

# calc = num1 * num2
# valor = print("Multiplicação:" , calc)

# calc = num1 // num2
# valor = print("Divisão:" , calc)

# calc = num1 % num2
# valor = print("Resto:" , calc)

#------------------------------------------------------------------

# Exercicío 4

# num1 = int(input('Fale um número: '))
# num2 = int(input('Fale outro: '))

# calc = num1 ** num2

# print(calc)

#------------------------------------------------------------------

# Exercicío 5

# pi = 3.141592 

# raio = float(input("Raio do círculo: "))

# calc = pi * (raio ** 2)

# print(calc)

#------------------------------------------------------------------

# Exercício 6

# num1 = int(input('Fale um número: '))

# calc = num1 // 10
# valor = print("Dezena:" calc)

# calc = (num1 % 10) 
# valor = print("Unidade:" calc)

#------------------------------------------------------------------

# Exercício 7

# num1 = int(input("Quantos camisas você tem em seu guarda-roupas?"))
# num2 = int(input("Quantas calças?"))
# num3 = int(input("E quantos pares de sapatos?"))

# calc = num1 * num2 * num3
# print(calc)

#------------------------------------------------------------------

# Exercicío 8

# while True:
    
#     resposta = input("Escolha: desconto ou aumento? ")

#     if resposta == "desconto":
#         valor = float(input("Valor  do produto: "))
#         desconto = float(input("Valor do desconto, em %: "))
        
#         calculo = valor * (desconto / 100)
#         calculo = valor - calculo  

#         print("Seu valor com o desconto é:" , calculo)
#         break    

#     if resposta == "aumento":

#         valor = float(input("Valor do produto: "))
#         aumento = float(input("Valor do desconto, em %: "))

#         calculo = valor * (aumento / 100)
#         calculo = valor + calculo  

#         print("Seu valor com o aumento é:" , calculo)
#         break

#     else:
#         print("ERRO!!! A resposta deve ser: 'aumento' ou 'desconto'")
#         continue

#------------------------------------------------------------------

# Exercício 9

# space = float(input("Distântia em metros: "))
# time = float(input("Tempo em segundos: "))

# speed = space / time
# print(speed , "m/s")

# speed = speed * 3.6
# print(speed , "Km/h")

#------------------------------------------------------------------

# Exercício 10

# salario1 = float(input("Salário antes do aumento: "))
# salario2 = float(input("Salário depois do aumento: "))

# calc = salario2 - salario1
# calc = (calc * 100) / salario1
# aumento = int(calc)

# print(aumento , "%")

#------------------------------------------------------------------

# Exercício 11

# while True:
#     rm = input("Escreva seu RM: ")
#     if len(rm) == 5:
#         rm = int(rm)
#         num5 = rm % 10
#         soma5 = num5 
#         num5 = rm // 10
#         num4 = num5 % 10
#         soma4 = num4
#         num4 = rm // 100
#         num3 = num4 % 10
#         soma3 = num3
#         num3 = rm // 1000
#         num2 = num3 % 10
#         soma2 = num2
#         num2 = rm // 10000
#         num1 = num2 % 10
#         soma1 = num1
#         calc = soma1 + soma2 + soma3 + soma4 + soma5
#         print(calc) 
#         break

#     else: 
#         print("ERRO!!! O seu RM deve ter 5 caracteres ")
#         continue

#------------------------------------------------------------------

# Exercício 12

# nac = float(input("Sua nota NAC: "))
# am = float(input("Sua nota AM: "))
# ps = float(input("Sua nota PS: "))

# media = ((2 * nac) + (3 * am) + (5 * ps)) / 10
# print("Sua média é: " , media)

#------------------------------------------------------------------

# Exercício 13