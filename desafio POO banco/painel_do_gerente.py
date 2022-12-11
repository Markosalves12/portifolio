#definicação da função do painel do gerente
#a função recebe como paramtro um objeto da classe Agencia
def painel_do_gerente(agencia_gerente):
    #variavel que permite o gerente acessar as função reservadas
    acao_do_ger = input("O que o gerente deseja fazer:\n"
                        "1 - criar Um novo cliente:\n"
                        "2 - Ver ralatório da agencia:\n"
                        "3 - sair:\n")
    #verificando e tratando a entrada do gerente
    try:
        acao_do_ger = int(acao_do_ger)
    except:
        print("Comando invalido")

    if acao_do_ger == 1:
        #dando ao gerente acesso a função de criar novos clientes
        agencia_gerente.criar_cliente()
        return True

    elif acao_do_ger == 2:
        #dando ao gerente acesso a função de ver dados da agencias
        agencia_gerente.relatorio_da_agencia()
        return True

    elif acao_do_ger == 3:
        #saindo do painel do gerente
        return False

    else:
        pass




