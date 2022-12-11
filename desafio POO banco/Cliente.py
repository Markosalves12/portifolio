#importando o modulo que conta as cédulas do saque
from Ativos_do_banco import disp_cedulas


class Cliente:
    def __init__(self, nome, sexo, cpf, senha):
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__senha = senha
        #a partir do momento que a conta é criada os saldos sõa iniciados em zero
        self.__saldo_corrente = 0
        self.__saldo_poupanca = 0

    #criar os getters e os setters para ter acesso posterior
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def saldo_corrente(self):
        return self.__saldo_corrente

    @saldo_corrente.setter
    def saldo_corrente(self, saldo_corrente):
        self.__saldo_corrente = saldo_corrente

    def ver_saldo_corrente(self):
        print(self.__saldo_corrente)

    def ver_saldo_poupanca(self):
        print(self.__saldo_poupanca)

    #função para fazer depoistos no banco
    #o deposito e feito em conta corrente
    def fazer_deposito_corrente(self):
        deposito = input("Qual o valor será depositado: ")
        #verificando se o valor e numerico
        try:
            deposito = float(deposito)
        except:
            print("Digite um valor corretamente")
            return False
        #se o valor for confirmado o valor em conta e atualizado
        self.__saldo_corrente = self.__saldo_corrente + deposito
    #função que execulta os saques em conta corrente
    def fazer_saque_conta_corrente(self):
        #entrada do saque que o cliente ira execultar
        saque = input("Qual o valor será sacado: ").strip()
        #tratando a entrada do usuario
        try:
            saque = float(saque)
        except:
            print("Digite um valor corretamente")
            return False
        #verificando se o valor em saque é compativel com o valor em conta
        if saque > self.__saldo_corrente:
            print("Valor maior que o saldo em conta")
            return
        #contando as cedulas do cliente
        disp_cedulas.Contar_celulas(saque)
        self.__saldo_corrente = self.__saldo_corrente - saque
    #funcao que transfere da conta corrente para a poupança
    def fazer_transferencia_corrente_poupana(self):
        #entrada do cliente
        transf_pou = input("Quanto deseja transferir para poupança: ").strip()
        #entrada do usuario
        try:
            transf_pou = float(transf_pou)
        except:
            print("Digite um valor corretamente")
            return False
        #verificando se o valor de transferencia e compativel com a conta corrente
        if transf_pou > self.__saldo_corrente:
            print("O valor para ser transferido é maior que o saldo na poupança")
            return False
        #atualizando ambos os saldos
        self.__saldo_corrente = self.__saldo_corrente - transf_pou
        self.__saldo_poupanca = self.__saldo_poupanca + transf_pou
    #função que transfere da poupança para a conta corrente
    def fazer_transferencia_poupanca_corrente(self):
        #entrada do cliente
        transf_corr = input("Quanto deseja transferir para a conta corrente: ").strip()
        #tratamento da entrada do usuario
        try:
            transf_corr = float(transf_corr)
        except:
            print("Digite um valor corretamente")
            return False
        #verificando se o valor para ser transferido é compativel com a poupança
        if transf_corr > self.__saldo_poupanca:
            print("O valor para ser transferido é maior que o saldo em conta")
            return False
        #atualizando os saldos nas duas contas
        self.__saldo_corrente = self.__saldo_corrente + transf_corr
        self.__saldo_poupanca = self.__saldo_poupanca - transf_corr

