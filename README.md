# Projeto: Sistema de Conta Bancária em Python
Descrição
Este projeto implementa um sistema básico de conta bancária em Python, permitindo a criação de usuários e contas bancárias, além de realizar operações de depósito, saque e consulta de extrato. O sistema é gerenciado através de um menu interativo que fornece diferentes funcionalidades para o usuário.

# Funcionalidades
1. Criar Usuário
Permite a criação de um novo usuário, solicitando CPF, nome completo, data de nascimento e endereço completo.

2. Criar Conta
Cria uma nova conta bancária para um usuário já cadastrado, gerando automaticamente o número da conta e vinculando ao CPF do usuário.

3. Depósito
Realiza um depósito em uma conta existente. O número da conta e o valor do depósito são solicitados ao usuário. Somente valores positivos são permitidos.

4. Saque
Realiza um saque de uma conta existente. O número da conta e o valor do saque são solicitados ao usuário. O saque possui as seguintes restrições:

# Máximo de 3 saques por dia.
Valor máximo de R$1000,00 por saque.
O saldo da conta deve ser suficiente para realizar o saque.
5. Extrato
Exibe o extrato de uma conta, listando todas as transações realizadas e o saldo atual.

6. Listar Contas
Lista todas as contas cadastradas, exibindo o nome do usuário, a agência e o número da conta.

7. Sair
Encerra o sistema.

# Implementação
A implementação é baseada em uma classe ContaBancaria que gerencia as operações bancárias e a interação com os usuários e contas. As principais funcionalidades estão encapsuladas em métodos específicos dentro da classe.

# Classe ContaBancaria
Atributos:

saldo: Mantém o saldo atual da conta.
transacoes: Lista de transações realizadas na conta.
saques_hoje: Contador de saques realizados no dia.
usuarios: Lista de usuários cadastrados.
contas: Lista de contas bancárias criadas.
Métodos:

deposito: Realiza um depósito em uma conta.
saque: Realiza um saque de uma conta.
extrato: Exibe o extrato de uma conta.
criar_usuario: Cadastra um novo usuário.
filtrar_usuario: Busca um usuário pelo CPF.
criar_conta: Cria uma nova conta bancária.
listar_contas: Lista todas as contas cadastradas.
filtrar_conta: Busca uma conta pelo número da conta.
Menu Interativo
Um loop infinito exibe um menu com as opções disponíveis para o usuário. A cada iteração, o usuário escolhe uma operação a ser realizada. O menu permite realizar depósitos, saques, consultas de extrato, criação de usuários, criação de contas, listagem de contas e sair do sistema.

# Uso
Para usar o sistema, basta executar o script. O menu será exibido e o usuário pode escolher a operação desejada. O sistema continuará em execução até que o usuário escolha a opção de sair.

# Requisitos
Python 3.6 ou superior

# Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.