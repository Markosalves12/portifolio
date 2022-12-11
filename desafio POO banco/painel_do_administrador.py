#Importando a classe banco o modulo Administrador_banco
from Administrador_Banco import banco
#função do painel do administrador
def painel_do_administrador():
    #variavel que faz o administrador andar pelo painel
    acao_do_adm = input("O que o administrador deseja fazer:\n"
                        "1 - criar nova agencia:\n"
                        "2 - Ver relatório de agencias:\n"
                        "3 - Ver ralatório de uma agencia especifica:\n"
                        "4 - criar um gerente para uma agencia:\n"
                        "5 - sair:  ")
    #verificando se o usurio digitou algum numero valido
    try:
        acao_do_adm = int(acao_do_adm)
    except:
        print("Comando invalido")

    if acao_do_adm == 1:
        #abrindo a função de criar agencia
        banco.banco_teste.cria_agencia()
        print("Agencia Criada")
        return True

    elif acao_do_adm == 2:
        #abrindo a função de listar agencias do banco
        banco.banco_teste.lista_agencias()
        return True
    elif acao_do_adm == 3:
        #abrindo a função para buscar a agencia especifica do banco
        banco.banco_teste.buscar_agencia()
        return True

    elif acao_do_adm == 4:
        #função para criar algum gerente para alguma agencia
        banco.banco_teste.criar_gerente()
        return True

    elif acao_do_adm == 5:
        #saida do painel do painel do administrador
        return False

    else:
        pass




