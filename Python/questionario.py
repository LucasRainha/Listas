
nome = input("Qual o seu nome?")
idade = input("Qual a sua idade?")
curso = input("Já fez algum curso superior? Qual?")
escolha = input("Por que escolheu TI?")
trabalho = input("Em qual área gostaria de trabalhar?")
hobbies = input("Quais são seus hobbies?")

arq = open("dados.txt", "w")
arq.write(f"{nome}|{idade}|{curso}|{escolha}|{trabalho}|{hobbies}")
arq.close()
