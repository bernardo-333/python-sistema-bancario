from banco import deposito, saque, extrato, cadastrar_usuario, cadastrar_conta, listar_usuarios, listar_contas, usuarios, contas, cadastrar_conta_com_saldo, buscar_conta

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[cu] Cadastrar Usuário
[cc] Cadastrar Conta
[ccs] Cadastrar Conta (com saldo)
[lu] Listar Usuários
[lc] Listar Contas
[q] Sair

=> """

limite = 500
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        cpf = input("CPF do titular: ")
        numero_conta = int(input("Número da conta: "))
        conta = buscar_conta(contas, cpf, numero_conta)
        if not conta:
            print("Conta não encontrada.")
            continue
        valor = float(input("Informe o valor do depósito: "))
        conta["saldo"], conta["extrato"], mensagem = deposito(conta["saldo"], valor, conta["extrato"])
        print(mensagem)

    elif opcao == "s":
        cpf = input("CPF do titular: ")
        numero_conta = int(input("Número da conta: "))
        conta = buscar_conta(contas, cpf, numero_conta)
        if not conta:
            print("Conta não encontrada.")
            continue
        if "numero_saques" not in conta:
            conta["numero_saques"] = 0
        valor = float(input("Informe o valor do saque: "))
        conta["saldo"], conta["extrato"], mensagem = saque(
            saldo=conta["saldo"],
            valor=valor,
            extrato=conta["extrato"],
            limite=limite,
            numero_saques=conta["numero_saques"],
            limite_saques=LIMITE_SAQUES
        )
        if mensagem == "Saque realizado com sucesso!":
            conta["numero_saques"] += 1
        print(mensagem)

    elif opcao == "e":
        cpf = input("CPF do titular: ")
        numero_conta = int(input("Número da conta: "))
        conta = buscar_conta(contas, cpf, numero_conta)
        if not conta:
            print("Conta não encontrada.")
            continue
        print(extrato(conta["saldo"], extrato=conta["extrato"]))

    elif opcao == "cu":
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF (apenas números): ")
        endereco = input("Endereço (logradouro, nro bairro --cidade/sigla estado): ")
        print(cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco))

    elif opcao == "cc":
        cpf = input("CPF do titular da conta: ")
        print(cadastrar_conta(usuarios, contas, cpf))

    elif opcao == "ccs":
        cpf = input("CPF do titular da conta: ")
        print(cadastrar_conta_com_saldo(usuarios, contas, cpf))

    elif opcao == "lu":
        print(listar_usuarios(usuarios))

    elif opcao == "lc":
        print(listar_contas(contas))

    elif opcao == "q":
        print("Obrigado por usar o sistema bancário!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
