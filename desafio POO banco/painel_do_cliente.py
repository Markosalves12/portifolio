#função que delimita o painel do administrador
#a função rece como parametro um objeto do tipo Cliente com sua conta e dados da conta
def painel_do_cliente(conta_cliente):
    #variavel que permite o cliente acessar as funções reservadas
    acao_do_cliente = input("O que o cliente deseja fazer:\n"
                            "1 - Ver saldo corrente:\n"
                            "2 - Ver saldo poupança:\n"
                            "3 - fazer um deposito:\n"
                            "4 - transeferir para poupança:\n"
                            "5 - transferir da poupança para a conta corrente:\n"
                            "6 - sacar um valor:\n"
                            "7 - sair:---")
    #verificando a entrada do cliente
    try:
        acao_do_cliente = int(acao_do_cliente)
    except:
        print("Comando invalido")

    if acao_do_cliente == 1:
        #acessando a função dentro do objeto da classe Cliente
        conta_cliente.ver_saldo_corrente()
        return True

    elif acao_do_cliente == 2:
        # acessando a função dentro do objeto da classe Cliente
        conta_cliente.ver_saldo_poupanca()
        return True

    elif acao_do_cliente == 3:
        # acessando a função dentro do objeto da classe Cliente
        conta_cliente.fazer_deposito_corrente()
        return True

    elif acao_do_cliente == 4:
        # acessando a função dentro do objeto da classe Cliente
        conta_cliente.fazer_transferencia_corrente_poupana()
        return True

    elif acao_do_cliente == 5:
        # acessando a função dentro do objeto da classe Cliente
        conta_cliente.fazer_transferencia_poupanca_corrente()
        return True

    elif acao_do_cliente == 6:
        #função que permite o usuario realizar um saque
        conta_cliente.fazer_saque_conta_corrente()
        return True

    elif acao_do_cliente == 7:
        #saida do painel do cliente
        return False

    else:
        pass
