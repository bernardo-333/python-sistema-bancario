def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Validações
    if valor > saldo:
        return saldo, 0, extrato, "Operação falhou! Saldo insuficiente."

    if valor > limite:
        return saldo, 0, extrato, "Operação falhou! O valor do saque excede o limite."

    if numero_saques >= limite_saques:
        return saldo, 0, extrato, "Operação falhou! Número máximo de saques excedido."

    if valor <= 0:
        return saldo, 0, extrato, "Operação falhou! O valor informado é inválido."

    # Faz o saque
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1

    return saldo, extrato, "Saque realizado com sucesso!"

def deposito(saldo, valor, extrato):
    # Validações
    if valor <= 0:
        return saldo, extrato, "Operação falhou! O valor informado é inválido."

    # Faz o depósito
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"

    return saldo, extrato, "Depósito realizado com sucesso!"

def extrato(saldo, *,  extrato):
    # Formatação do extrato
    extrato_header = "\n================ EXTRATO ================\n"
    extrato_body = extrato if extrato else "Não foram realizadas movimentações."
    extrato_footer = f"\nSaldo: R$ {saldo:.2f}\n=========================================="

    return extrato_header + extrato_body + extrato_footer

usuarios = []

def cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario[cpf] == cpf:
            return "Usuario já cadastrado com o mesmo CPF"
    
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    return "Usuario cadastrado com sucesso!!!"

contas = []

def cadastrar_conta(usuarios, contas, cpf):
    agencia = "0001"
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break
    if not usuario:
        return "Usuário não encontrado. Conta não criada."

    numero_conta = len(contas) + 1  
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    return f"Conta criada com sucesso! Agência: {agencia}, Número: {numero_conta}"

def cadastrar_conta_com_saldo(usuarios, contas, cpf):
    agencia = "0001"
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break
    if not usuario:
        return "Usuário não encontrado. Conta não criada."

    numero_conta = len(contas) + 1
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": ""
    }
    contas.append(conta)
    return f"Conta criada com sucesso! Agência: {agencia}, Número: {numero_conta}"

def buscar_conta(contas, cpf, numero_conta):
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf and conta["numero_conta"] == numero_conta:
            return conta
    return None

def listar_usuarios(usuarios):
    if not usuarios:
        return "Nenhum usuário cadastrado."
    resultado = "\n=== Lista de Usuários ===\n"
    for usuario in usuarios:
        resultado += f"Nome: {usuario['nome']} | CPF: {usuario['cpf']} | Nascimento: {usuario['data_nascimento']}\nEndereço: {usuario['endereco']}\n---\n"
    return resultado

def listar_contas(contas):
    if not contas:
        return "Nenhuma conta cadastrada."
    resultado = "\n=== Lista de Contas ===\n"
    for conta in contas:
        usuario = conta['usuario']
        resultado += f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usuario['nome']} | CPF: {usuario['cpf']}\n"
    return resultado