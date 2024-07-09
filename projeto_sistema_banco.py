class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.transacoes = []
        self.saques_hoje = 0
        self.usuarios = []
        self.contas = []

    def deposito(self, numero_conta, valor, /):
        conta = self.filtrar_conta(numero_conta)
        
        if conta:
            
            if valor > 0:
                conta["saldo"] += valor
                conta["transacoes"].append(f"Depósito: R${valor:.2f}")
                print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            
            else:
                print("Valor de depósito deve ser positivo.")
        
        else:
            print("Conta não encontrada.")
    

    def saque(self, *, numero_conta, valor):
        conta = self.filtrar_conta(numero_conta)
        
        if conta:
            
            if conta["saques_hoje"] >= 3:
                print("Limite de 3 saques diários atingido.")
            
            elif valor > 1000:
                print("Valor máximo por saque é de R$1000,00.")
            
            elif valor > conta["saldo"]:
                print("Saldo insuficiente para realizar o saque.")
            
            else:
                conta["saldo"] -= valor
                conta["saques_hoje"] += 1
                conta["transacoes"].append(f"Saque: R${valor:.2f}")
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
        
        else:
            print("Conta não encontrada.")

    def extrato(self, /, *, numero_conta):
        conta = self.filtrar_conta(numero_conta)
        
        if conta:
            print(f"Extrato de movimentações da Conta #{numero_conta}:")
            
            for transacao in conta["transacoes"]:
                print(transacao)
            print(f"Saldo atual: R${conta['saldo']:.2f}")
        
        else:
            print("Conta não encontrada.")

    def criar_usuario(self):
        cpf = input("Informe o CPF: ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            print("Usuário já cadastrado.")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento: ")
        endereco = input("Informe o endereço completo: ")

        self.usuarios.append({"cpf": cpf, 
                              "nome": nome, 
                              "data_nascimento": data_nascimento, 
                              "endereco": endereco})
        
        print("Usuário cadastrado com sucesso.")

    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario["cpf"] == cpf:
                return usuario
        
        return None

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)

        if not usuario:
            print("Usuário não encontrado.")
            return

        numero_conta = len(self.contas) + 1
        agencia = "0001"
        self.contas.append({"numero_conta": numero_conta, 
                            "agencia": agencia, 
                            "cpf": cpf, 
                            "saldo": 0.0,
                            "transacoes": [],
                            "saques_hoje":0})
        
        print(f"Conta número {numero_conta} criada com sucesso para o usuário {usuario['nome']}.")

    def listar_contas(self):
        if not self.contas:
            print("Não há contas cadastradas.")
        else:
            print("Contas cadastradas:")
            for conta in self.contas:
                usuario = self.filtrar_usuario(conta["cpf"])
                print(f"Nome: {usuario['nome']}, Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}")

    def filtrar_conta(self, numero_conta):
        for conta in self.contas:
            if conta["numero_conta"] == numero_conta:
                return conta
        return None

conta = ContaBancaria()

menu = """
======== Conta Bancária ========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Mostrar Conta
[7] Sair
"""

while True:
    print(menu)
    opcao = input("Escolha uma operação: ")

    if opcao in ["1", "2", "3"] and not conta.contas:
        print("Nenhuma conta encontrada. Por favor, crie uma conta primeiro.")
        continue

    if opcao == "1":
        numero_conta = int(input("Informe o número da conta."))
        valor = float(input("Digite o valor para depósito: "))
        conta.deposito(numero_conta, valor)

    elif opcao == "2":
        numero_conta = int(input("Informe o número da conta."))
        valor = float(input("Digite o valor para saque: "))
        conta.saque(numero_conta=numero_conta, valor=valor)

    elif opcao == "3":
        numero_conta = int(input("Informe o número da conta."))
        conta.extrato(numero_conta=numero_conta)

    elif opcao == "4":
        conta.criar_usuario()

    elif opcao == "5":
        conta.criar_conta()
    
    elif opcao == "6":
        conta.listar_contas()

    elif opcao == "7":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida. Digite uma das funções do menu!")