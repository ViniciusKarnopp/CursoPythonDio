escolha = ""
saldo = 0
numero_de_pessoas_cadastradas = 0
contas = {}
contas_criadas = []
pessoas_cadastradas = []
limite_saques = 0 #limite é 3
saque_maximo = 500
extrato_deposito = []
extrato_saque = []
cpfs = []
extrato_por_cpf = []
extrato = []
conta_cpf = {}
saldo_clientes = []
saldo_teste = 0

def main():
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


class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def cadastrar_pessoa(self):
        pessoa = {
            "Nome:": self._nome,
            "CPF:": self._cpf,
            "Data de Nascimento:": self._data_nascimento
        }
        return pessoa

    def __str__(self):
        return f"{self.__class__.__name__}: {' '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class VerificarCPF:
    def __init__(self, cpf):
        self._cpf = cpf
    def filtro_cpf(self):
        for i in cpfs:
            if self._cpf == i:
                return True
        return False


class Cliente(PessoaFisica):
    def __init__(self, endereco, cpf, **kw):
        self._endereco = endereco
        self._contas = contas
        super().__init__(cpf=cpf, **kw)
        
    def criar_conta(self, numero_de_pessoas_cadastradas):
        self.numero_de_pessoas_cadastradas = numero_de_pessoas_cadastradas
        conta = Conta(saldo=saldo, numero=numero_de_pessoas_cadastradas, agencia="0001", cliente=nome, cpf=self._cpf)
        criar_conta = conta.criar_conta()
        numero_de_pessoas_cadastradas += 1

        return criar_conta, numero_de_pessoas_cadastradas


class Transacao:
    def __init__(self, deposito=None, saque=None, saldo=None):
        self._deposito = deposito
        self._saque = saque
        self.saldo = saldo

    def Deposito(self):
        self.saldo += self._deposito
        extrato_deposito.append(self._deposito)
        return self.saldo

    def Saque(self):
        self.saldo -= self._saque
        extrato_saque.append(self._saque)
        return self.saldo

    def registrar_transacao(self, conta, tipo, cpf, valor):
        self._conta = conta_cpf
        self.tipo = tipo
        self.cpf = cpf
        self.valor = valor
        if self.tipo == "Deposito":
            conta.registrar_transacao(self, tipo=self.tipo, valor=self.valor, cpf2=cpf)
            self._conta = {"CPF": cpf, 
                           "Tipo": tipo,
                           "Valor": self.valor}
            self.saldo += self.valor
        elif self.tipo == "Saque":
            conta.registrar_transacao(self, tipo=self.tipo, valor=self.valor, cpf2=cpf)
            self._conta = {"CPF": self.cpf,
                           "Tipo": self.tipo,
                           "Valor": self.valor}
            self.saldo -= self.valor
        return self._conta, self.saldo


class Conta:
    def __init__(self, saldo, numero, agencia, cliente, cpf):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._cpf = cpf
    
    def criar_conta(self):
        contas = {"Agência:": self._agencia,
                    "Numero:": self._numero+1,
                    "Cliente:": self._cliente,
                    "CPF: ": self._cpf
                    }
        return contas


    def registrar_transacao(self, tipo, valor, cpf2):
        transacao = {"CPF": cpf2, "Tipo:": tipo, "Valor:": valor}
        extrato.append(transacao)
        return extrato, transacao

    
    def __str__(self):
        return f"{self.__class__.__name__}: {' '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Listar_Usuarios:
    def __init__(self, pessoa, contas):
        self.pessoa = pessoa
        self.contas = contas
    
    def listar(self):
        for dicionario in self.contas:
            for chave, valor in dicionario.items():
                print(f"{chave} {valor}")
            print("---------------------")  
        #for dicionario_pessoas in self.pessoa:
            #for chave, valor in dicionario_pessoas.items():    comentado pq acho q n vou mostrar pessoa. Somente mostrarei as contas
                #print(f"{chave} {valor}")
            #print("---------------------") 


while(escolha.lower() != "q"):
    escolha = main()

    match escolha.lower():

        case "nu":
            cpf = input("Digite seu CPF. Sem traços ou pontos. Somente números. ")
            verificarcpf = VerificarCPF(cpf)
            filtrocpf = verificarcpf.filtro_cpf()
            if filtrocpf == False:
                cpfs.append(cpf)
                nome = input("\nQual o seu nome? ")
                data_nascimento = input("Qual sua data de nascimento? Digite neste formato: dd/mm/aaaa ")
                endereco = input("Qual o seu endereço? ")
                saldo_clientes.append(0)

                pessoa = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento)
                cadastrar_pessoa = pessoa.cadastrar_pessoa()
                pessoas_cadastradas.append(cadastrar_pessoa)

                cliente = Cliente(endereco=endereco, cpf=cpf, nome=nome, data_nascimento=data_nascimento)
                criar_conta = cliente.criar_conta(numero_de_pessoas_cadastradas=numero_de_pessoas_cadastradas)

                numero_de_pessoas_cadastradas = criar_conta[1]
                contas_criadas.append(criar_conta[0])
            else:
                print("CPF já registrado em nossa base. Tente novamente.")
        
        case "lu":
            listar_usuarios = Listar_Usuarios(pessoa=pessoas_cadastradas, contas=contas_criadas)
            listar_usuarios.listar()

        case "d":
            if numero_de_pessoas_cadastradas > 0:
                cpf_cliente = input("Digite o CPF do cliente: ")
                conta_encontrada = None
                for conta in contas_criadas:
                    if conta["CPF: "] == cpf_cliente:
                        conta_encontrada = conta
                        break
                if conta_encontrada is not None:
                    posicao_cpf = cpfs.index(cpf_cliente)
                    valor_deposito = float(input("""
        Você escolheu a opção de depósito.
        Digite o valor do depósito:
                ==> R$"""))
                    if valor_deposito > 0:
                        saldo = saldo_clientes[posicao_cpf]
                        deposito = Transacao(deposito=valor_deposito, saque=None, saldo=saldo)
                        armazenar_transacao = deposito.registrar_transacao(conta=Conta, tipo="Deposito", cpf=cpf_cliente, valor=valor_deposito)
                        extrato_por_cpf.append(armazenar_transacao[0])
                        saldo = armazenar_transacao[1]
                        saldo_clientes[posicao_cpf] = saldo
                        print("Depósito realizado com sucesso.\nObrigado pela preferência.")
                        print("--------------------------------")
                    else:
                        print("Valor não pode ser processado. Tente novamente.")
                else:
                    print("Não encontramos clientes em nossa base de dados. Tente novamente.")

        case "s":
            if numero_de_pessoas_cadastradas > 0:
                cpf_cliente = input("Digite o cpf do cliente: ")
                conta_encontrada = None
                for conta in contas_criadas:
                    if conta["CPF: "] == cpf_cliente:
                        conta_encontrada = conta
                        break
                if conta_encontrada is not None:
                    valor_saque = float(input("""
    Você escolheu a opção de saque.
    Digite o valor do saque:
            ==> R$"""))
                    posicao_cpf = cpfs.index(cpf_cliente)
                
                    if valor_saque <= 0:
                        print("Valor não pode ser processado. Tente novamente.")
                    elif limite_saques > 2:
                        print("Você excedeu o máximo de saques diários. Tente novamente amanhã.")
                    elif valor_saque > saque_maximo:
                        print("O seu limite para saques é de R$500,00. Tente novamente com um valor menor que o seu limite.")
                    elif valor_saque > saldo:
                        print("Saldo insuficiente. Tente novamente.")
                    else:
                        saldo = saldo_clientes[posicao_cpf]
                        saque = Transacao(deposito=None, saque=valor_saque, saldo=saldo)
                        armazenar_transacao = saque.registrar_transacao(conta=Conta, tipo="Saque", cpf=cpf_cliente, valor=valor_saque)
                        extrato_por_cpf.append(armazenar_transacao[0])
                        saldo = armazenar_transacao[1]
                        limite_saques += 1
                        saldo_clientes[posicao_cpf] = saldo
                        print("""
    ----------------------------
    Saque realizado com sucesso!
    ----------------------------
""")
                        
                else:
                    print("CPF não encontrado. Tente novamente.")
            else:
                print("Não encontramos clientes em nossa base de dados. Tente novamente.")

        case "e":
            if numero_de_pessoas_cadastradas > 0:
                cpf_cliente = input("Digite o cpf do cliente: ")
                verificarcpf = VerificarCPF(cpf_cliente)
                filtrocpf = verificarcpf.filtro_cpf()
                if filtrocpf:
                    contador = 1
                    print(f"CPF: {cpf_cliente}")
                    posicao_cpf = cpfs.index(cpf_cliente)
                    for i in extrato_por_cpf:
                            if i["CPF"] == cpf_cliente:
                                if i["Tipo"] == "Deposito":
                                    print(f"Transação {contador}: Depósito de R${i['Valor']}")
                        
                                elif i["Tipo"] == "Saque":
                                    print(f"Transação {contador}: Saque de R${i['Valor']}")
                                contador +=1
                    print(f"Saldo: {saldo_clientes[posicao_cpf]}")
                else:
                    print("Não foi encontrada nenhuma conta associada a esse CPF.")
            else:
                print("Não encontramos clientes em nossa base de dados. Tente novamente.")

