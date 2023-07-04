import time

escolha = ""
lista_de_usuarios = []
conta_corrente = {"Agencia": "0001", "Conta": "", "Usuário": ""}
lista_cpf = []
numero_de_usuarios_cadastrados = 0
valor_conta = 0
numero_saques = 0
limite_saques = 500
lista_saques = []
lista_depositos = []
lista_cc = {}
lista_de_contas = []

def menu():
    escolha = input("""
    ===============MENU===============
    | [NU] - Novo Usuário            |
    | [LU] - Listar Usuários         |
    | [D]  - Depositar               |
    | [S]  - Sacar                   |
    | [E]  - Visualizar o Extrato    |
    | [Q]  - Sair do Programa        |
    ==================================
    => """)
    return escolha.lower()

def criar_usuario(lista, numero_de_usuarios_cadastrados):
    cpf = input("Qual o seu CPF?\nDigite somente números.\n")
    cpf_ex = cpf_existe(cpf, lista_cpf)
    if cpf_ex:
        usuario = {}
        numero_de_usuarios_cadastrados += 1
        nome = input("\nDigite o nome do usuário: \n")
        data = input(f"\n{nome}, qual a sua data de nascimento?\nDigite neste formato: dd/mm/aaaa\n")
        logradouro = input(f"\n{nome}, qual o seu endereço?\nDigite neste formato: Logradouro, numero - bairro - cidade/sigla\n")
        usuario["Nome"] = nome
        usuario["Data"] = data
        usuario["CPF"] = cpf
        usuario["Logradouro"] = logradouro
        lista.append(usuario)
        lista_cpf.append(cpf)
        
        #lista.append(teste)
        return usuario, numero_de_usuarios_cadastrados
    else:
        return None

def cpf_existe(cpf, lista_de_cpf):
    if len(lista_de_cpf) == 0:
        print("""
            ===CPF Verificado com sucesso===
            """)
    for cpf_verifica in lista_de_cpf:
        print(cpf_verifica)
        if cpf == cpf_verifica:
            print("""
            ====Falha. CPF já cadastrado em nossa base====
            ================Tente Novamente===============
            """)
            return False
        else:
            print("""
            ===CPF Verificado com sucesso===
            """)

    return cpf

def exibir_usuarios(lista, numero_de_usuarios_cadastrados, lista_cc):
    if numero_de_usuarios_cadastrados > 0:
        for usuario in lista:
            print("Usuário:")
            for chave, valor in usuario.items():
                print(f"{chave}: {valor}")
            print("-------------------------")
        for dicionario in lista_cc:
            print("Informações Bancárias: ")
            for chave, valor in dicionario.items():
                print(f"{chave}: {valor}")
            print("-------------------------")
            

def sacar(saldo, numero_de_saques, limite_saque, lista_de_saques):
    print("Você escolheu a opção de saque.\n")
    if saldo <= 0:
        print("Saldo insuficiente. Tente novamente.\n")
    elif numero_de_saques > 2:
        print("Você excedeu o limite de saques diários. Tente novamente amanhã.\n")
    else:
        valor = float(input("""
        Digite o valor desejado para sacar:
        ==> R$"""))
        if valor > saldo:
            print("Saldo insuficiente. Tente Novamente.")
        elif valor > limite_saque:
            print("O seu limite de saque é de R$500,00. Tente Novamente.\n")
        else:
            lista_de_saques.append(valor)
            saldo -= valor
            numero_de_saques += 1
            print("""
            ===Sucesso!===
            """)
    return saldo, numero_de_saques

def criar_conta(nome, lista_cpf):
    nro_conta = len(lista_cpf)
    lista_cc = {
        "Agência": "0001",
        "Conta": f"000{nro_conta}",
        "Usuario": nome,
                }
    lista_de_contas.append(lista_cc)

    return lista_de_contas

def depositar(*, saldo, lista_de_depositos):
    valor = float(input("""
    Você escolheu depósito.
    Digite o valor desejado.
    ==> R$"""))
    if valor > 0:
        lista_de_depositos.append(valor)
        saldo += valor
        print("Sucesso. Em instantes o valor depositado será acrescido na sua conta.\nObrigado pela preferência.\n")
    else:
        print("Não foi possível processar este valor. Tente novamente.\nSó aceitamos depósitos maiores que R$0,00")

    return saldo

def extrato(saldo, *, lista_de_saques, lista_de_depositos, numero_de_usuarios_cadastrados):
    print(f"""
    Você escolheu visualizar o extrato.
    Número de usuários cadastrados no sistema: {numero_de_usuarios_cadastrados}
    """)
    contador = 0
    for i in lista_de_saques:
        print(f"Saque {contador+1}: R${i}")
        contador += 1
    contador2 = 0
    for i in lista_de_depositos:
        print(f"Depósito {contador2+1}: R${i}")
        contador2 += 1
    print(f"Saldo da conta: R${saldo}")

while escolha != "q":
    escolha = menu()
    if escolha.lower() == "nu":
        roda_funcao = criar_usuario(lista_de_usuarios, numero_de_usuarios_cadastrados)
        if roda_funcao:
            pegar_dicionario = roda_funcao[0]
            numero_de_usuarios_cadastrados = roda_funcao[1]
            exibir_conta = criar_conta(pegar_dicionario["Nome"], lista_cpf)

    elif escolha.lower() == "lu":
        if numero_de_usuarios_cadastrados > 0:
            exibir_usuarios(lista_de_usuarios, numero_de_usuarios_cadastrados, exibir_conta)
        else:
            print("Sem usuarios cadastrados. Tente Novamente.")
    
    elif escolha.lower() == "d":
        valor_conta = depositar(saldo=valor_conta, lista_de_depositos=lista_depositos)
    
    elif escolha.lower() == "s":
        roda_func = sacar(valor_conta, numero_saques, limite_saques, lista_saques)
        valor_conta = roda_func[0]
        numero_saques = roda_func[1]
    elif escolha.lower() == "e":
        extrato(valor_conta, lista_de_saques=lista_saques, lista_de_depositos=lista_depositos, numero_de_usuarios_cadastrados=numero_de_usuarios_cadastrados)
