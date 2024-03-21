#1

# num1 = int(input("Digite um número: "))
# if num1 > 10:
#     print("Seu número é maior que dez ")
# elif num1 == 10:
#     print("Esse número é igual a dez ")
# else:
#     print("Esse número é menor q dez ")

#2

# num2 = int(input("Digite outro número: "))
#
# if num1 > num2:
#     print("O primeiro número é o maior ")
# elif num1 < num2:
#     print("O segundo número é o maior ")
# else:
#     print("Houve um empate, os dois númro são iguais ")

#3

# nome1 = str(input("Digite o nome do primeiro time: "))
# nome2 = str(input("Digite o nome do segundo time"))
#
# gol1 = int(input("Digite quantos gols o primeiro time fez"))
# gol2 = int(input("Digite quantos gols o segundo time fez"))
#
# if gol1 > gol2:
#     print(nome1, "ganhou")
# elif gol2 > gol1:
#     print(nome2, "ganhou")
# else:
#     print("EMPATE")

#4'

# dias = int(input("Quantos dias úteis houveram nesse mês? "))
# horas = int(input("Quantas horas foram trabalhadas no total? "))
# salario = float(input("Quanto vale a sua hora? "))
#
# extra = (horas - dias * 8) * salario * 1.5
# if horas > dias * 8:
#     print("Horas extras: R${:.2f}".format(extra))
#
# final = (salario * horas) + extra
# print("Seu salário final é de: R${:.2f}".format(final))

#5

# a = float(input("Digite um numero (A): "))
# b = float(input("Digite outro (B): "))
#
# c = a % b
# if c > 0:
#     print("A não é divisivel por B")
# else:
#     print("A é divisivel por B")

#6

import math

# numero = int(input("Digite um número: "))
# if numero < 0:
#     print("O número nn pode ser negativo")
# else:
#     raiz = math.sqrt(numero)
#     print("A raiz quadrada de {:.0f}".format(numero), "é igual a {:.2f}".format(raiz))

#7

# idade = int(input("Digite a idade do nadador: "))
#
# if 5 <= idade <= 7:
#     print("Infantil")
# elif 7 < idade <= 10:
#     print("Juvenil")
# elif 10 < idade <= 15:
#     print("Adolescente")
# elif 15 < idade <= 30:
#     print("Adulto")
# elif idade < 5:
#     print("Prodigio")
# else:
#     print("Senior")

#13

# dia = int(input('Digite o dia: '))
# mes = int(input('Digite o mes: '))
#
# if mes % 2 == 0:
#     if 1 <= dia <= 30 and mes != 2:
#         print("Valido")
#     elif mes == 2 and 1 <= dia <= 28 :
#         print("Valido")
#     else:
#         print("Invalido")
# else:
#     if 1 <= dia <= 31:
#         print("Valido")
#     else:
#         print("Invalido")
#
# #14
#
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

if mes == 2 and dia == 29:
    if ano % 400 == 0 and ano % 100 != 0:
          if ano % 4 == 0:
            print("Válido")
          else:
            print("Invalido")
    else:
        print("Inválido")
elif mes % 2 == 0 and mes != 2:
    print("Válido")
else:
    if 1 <= dia <= 31:
        print("Valido")
    else:
        print("Invalido")