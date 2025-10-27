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

def extrato(*, saldo, extrato):
    # Formata o extrato
    extrato_header = "\n================ EXTRATO ================\n"
    extrato_body = extrato if extrato else "Não foram realizadas movimentações."
    extrato_footer = f"\nSaldo: R$ {saldo:.2f}\n=========================================="

    return extrato_header + extrato_body + extrato_footer
