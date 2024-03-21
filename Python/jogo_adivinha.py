import random

while True:
    print("Jogo do adivinha, vou escolher um número entre 1 e 1000 e você tem 10 tentativas para acertar.")
    resposta = input("Quer jogar? ")

    if resposta == "sim" or "ss" or "quero":
        num = random.randint(1,1000)

        tentativa = int(input("Em que número eu pensei? "))

        while True:
           if isinstance(tentativa,int):
                chance = 1
                while chance < 10:
                    #Acertou ---------------------------------------------
                    if tentativa == num:
                        print(f"Não acredito que você acertou!!! E na {chance} tentativa, parabéns!!!")
                        break
                    #Menor -----------------------------------------------
                    elif tentativa < num:
                        tentativa = int(input("O número que eu pensei é maior que esse, escreva outro: "))
                    #Maior -----------------------------------------------
                    elif tentativa > num:
                        tentativa = int(input("O número que eu pensei é menor que esse, escreva outro: "))

                chance = chance + 1
                print("Suas tentativas acabaram :( ")
                break
           if isinstance(tentativa,str):
                print("Não entendi, tente novamente")
                continue
    if resposta == "nao" or "nn" or "nao quero" or "nao to afim" or "não" or "não quero":
        print("Ok, fica pra proxima...")
        break

    else:
        print("Erro, tente novamente.")
        continue
