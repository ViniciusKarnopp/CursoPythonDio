import time
total_saques = 3
limite_saque = 500.0
deposito = 0.0
saque = 0.0
depositos = []
saques = []
escolha = 0
valor_conta = 0.0
contador = 1


while escolha != 4:
    escolha = int(input("Menu:\n1 - Depositar\n2 - Sacar\n3 - Visualizar o extrato\n4 - Sair\n\n"))
    time.sleep(1)

    if escolha == 1:
        print("Você escolheu a opção de depósito.\n")
        deposito = float(input("Digite o valor do depósito que você deseja realizar.\n")) 
        time.sleep(1)
        if deposito <= 0:
            print("Digite outro valor. O valor digitado é inválido. Retornando ao menu\n")
            time.sleep(1)

        else:
            valor_conta += deposito
            depositos.append(deposito)
            print("Depósito realizado com sucesso.\n")
            time.sleep(1)


    elif escolha == 2:
        if total_saques > 0 and valor_conta > 0:
            print("Você escolheu a opção de saque.\n")
            saque = float(input("Digite o valor do saque que você deseja realizar.\n"))
            time.sleep(1)

            if saque <= 0:
                print("Digite outro valor. O valor digitado é inválido. Retornando ao menu...\n")
                time.sleep(1)
            
            elif saque > valor_conta:
                print("O valor digitado é maior do que o seu saldo atual. Por favor, tente novamente.\nRetornando ao menu...\n")
                time.sleep(1)
            
            elif saque > 500:
                print("O limite de saque é de R$500,00. Retornando ao menu...\n")
                time.sleep(1)

            else:
                valor_conta -= saque
                saques.append(saque)
                print("Saque realizado com sucesso.\n")
                total_saques -= 1
                time.sleep(1)

        elif valor_conta <= 0:
            print("Conta sem saldo. Retornando ao menu...\n")
            time.sleep(1)

        else:
            print("Você excedeu o limite de saques diários. Retornando ao menu...\n")
            time.sleep(1)

    elif escolha == 3:
        print("\n---------------------------")
        print("\n\nVocê escolheu a opção de visualizar o extrato.\n\n")
        print(f"Saldo total da conta: {valor_conta}\n")

        for i in depositos: #iterando através do vetor de depositos
            print(f"Depósito {contador}: R${i}") 
            contador += 1
            
        contador = 1

        print(" ") #pular linha (com o \n ele pulava 2 linhas)

        for i in saques: #iterando o vetor de saques
            print(f"Saque {contador}: R${i}")
            contador += 1

        print(f"\nTotal de saques disponíveis: {total_saques}")
        time.sleep(3)
        print("\nRetornando ao menu...\n")
        

        