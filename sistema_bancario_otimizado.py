menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuário
[r] Criar Conta Corrente
[l] Listar Contas Corrente
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = "Extrato: \n\n"
clientes = []
contas = []
numero_conta = 1

def sacar(*, saldo, valor, extrato, limite, limite_saques):
    global numero_saques
    if numero_saques < limite_saques:    
        if valor > 0:
            if valor > limite:
                print("Valor acima do limite!")
            else: 
                if saldo < valor:
                    print("Você não possui saldo suficiente!")
                else:
                    print("Valor de R$ " + str("{:.2f}".format(valor)) + " sacado com sucesso!")
                    extrato += "Valor de R$ " + str("{:.2f}".format(valor)) + " sacado\n"
                    saldo -= valor
                    numero_saques += 1
        else:
            print("Valor inválido!")
    else:
            print("Você atingiu sua quantidades de saques diárias!")

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Valor inválido!")
    else:
        saldo += valor
        extrato += "Valor de R$ " + str("{:.2f}".format(valor)) + " depositado\n"
    
    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):
    print(extrato + "Saldo atual: R$ "+str("{:.2f}".format(saldo)))

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário: ")
    cpf = input("Digite o número de CPF do usuário (apenas números): ")
    logradouro = input("Digite o logradouro do usuário: ")
    numero_residencia = input("Digite o número da residência do usuário: ")
    bairro = input("Digite o bairro do usuário: ")
    cidade = input("Digite a cidade do usuário: ")
    sigla_estado = input("Digite a sigla do estado do usuário: ")
    endereco = logradouro+", "+numero_residencia+" - "+bairro+" - "+cidade+"/"+sigla_estado
    usuario = [nome, data_nascimento, cpf, endereco]
    clientes.append(usuario)
    return clientes

def conta_corrente(cpf):
    global numero_conta
    usuario = filter(lambda x: x[2]==cpf, clientes)
    numero_agencia = "0001"
    conta = [numero_agencia, numero_conta, list(usuario)[0]]
    contas.append(conta)
    numero_conta += 1
    return contas

def listar_contas():
    for conta in contas:
        print(conta)

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor que deseja depositar: R$ "))
        saldo, extrato = depositar(saldo, deposito, extrato)
            

    elif opcao == "s":
        saque = float(input("Digite o valor que deseja sacar: "))
        saldo, extrato = sacar(saldo=saldo, valor=saque, extrato=extrato, limite=limite, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        ver_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        clientes = criar_usuario()

    elif opcao == "r":
        cpf_vincular = input("Digite o CPF do usuário que deseja vincular a conta: ")
        contas = conta_corrente(cpf_vincular)

    elif opcao == "l":
        listar_contas()

    elif opcao == "q":
        break

    else:
        print("Comando inválido!")