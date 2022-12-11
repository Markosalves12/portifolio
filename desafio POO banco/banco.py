#importando toda a classe agencia, ela vai permitir criar varias agencias para o banco
from Administração import Agencia
#a base de codigos gera um codigo para agencia para não haver ambiguidades
#a base de codigos tambem armazena as siglas dos estados
from Ativos_do_banco import Base_de_codigos
#para sair patra o painel do gerente após as verificações
from Administrador_Banco import painel_do_gerente

class Banco:
    def __init__(self):
        #vetor reservado para armazenar os objetos da classe(tipo) agencia
        self.agencias = []
    #função reservada a criação de novas agencias para o banco
    def cria_agencia(self):
        print(f'Codigo definido automaticamente para agencia: {Base_de_codigos.codigos_de_agencia_start}')
        while True:
            #as agencias precisam estar posicionadas em algum estado da federação, estabelecidos em outro arquivo
            uf = input("Em que estado da federação a agencia será posicionada?[SIGLA]: ").upper()
            #tratando a variavel uf, ela não poder ser numerica
            try:
                uf = float(uf)
            except:
                #verificações
                if len(uf) > 2:
                    print(f"Digite apenas siglas [dois caracteres]")
                elif uf not in Base_de_codigos.UFs:
                    print(f"A uf {uf} não existe na federação")
                elif type(uf) == float:
                    print(f"Digite apenas letras")
                else:
                    break
        #definindo a cidade da agencia
        cidade = input("Em que cidade a agencia será posicionada: ")

        codigo = Base_de_codigos.codigos_de_agencia_start
        #incrementando a base de codigos em +1
        Base_de_codigos.codigos_de_agencia_start += 1

        #variavel de instancia da classe agencia
        nova_agencia = Agencia.Agencia(codigo, uf, cidade)
        #salvando a agencia no vetor agencias
        self.agencias.append(nova_agencia)
    #buscar a agencia para alguma verificação do administrador
    def buscar_agencia(self):
        if len(self.agencias) == 0:
            print("Ainda não existem agencias no banco")
            return

        codigo = input("Qual o codigo da agencia: ")
        try:
            codigo = int(codigo)
        except:
            print("Codigo não reconhecido")
            return
        #printando todas as propriedades da agencia
        for agencia in self.agencias:
            if agencia.codigo == codigo:
                print(f"Codigo da agencia: {agencia.codigo}\n"
                      f"UF da egencia: {agencia.UF}\n"
                      f"Cidade em que está posicionada: {agencia.cidade}\n"
                      f"volume de clientes: {len(agencia.clientes)}")
                print("\n\n")
    #listando todas as agencias criadas independente da verificação
    def lista_agencias(self):
        if len(self.agencias) == 0:
            print("Ainda não existem agencias no banco")
            return None
        else:
            for agencia in self.agencias:
                print(f"Codigo da agencia: {agencia.codigo}\n"
                      f"UF da egencia: {agencia.UF}\n"
                      f"Cidade em que está posicionada: {agencia.cidade}\n"
                      f"volume de clientes: {len(agencia.clientes)}")
                print("\n\n")
    #função para criar os gerentes que irao trabalhar nas agencias
    def criar_gerente(self):
        #verificar o volume de agencias na estrutura do banco
        if len(self.agencias) == 0:
            print("Ainda não existem agencias no banco")
            return
        #O administrador deve informar o codigo da agencia do gerente
        codigo = input("Qual o codigo da agencia de trabalho do gerente: ").strip()#eliminar espaços extras
        #verificando se o codigo é inteiro ou não
        try:
            codigo = int(codigo)
        except:
            print("Codigo não reconhecido")
            return

        #verificando se existe alguma agencia com esse codigo no vetor agencia
        for agencia in self.agencias:
            if agencia.codigo == codigo:
                #criando o gerente para essa agencia especifica
                nome = input("Nome do gerente: ")
                senha = input("Senha do gerente: ")
                agencia.criar_gerente(nome, senha)
                print("gerente criado")

        print("codigo de agencia não encontrado")

    #buscar agencias para as verificações do gerente
    def busca_agencia(self):
        #verificando o volume de agencias no vetor agencia
        if len(self.agencias) == 0:
            print("Ainda não existem agencias")
            return False
        #entrada do código pelo gerenre
        codigo = input("Qual agencia você trabalha(codigo): ").strip()
        try:
            codigo = int(codigo)
        except:
            print("Codigo não reconhecido")
            return False
        #verificando se a agencia alegada pelo gerente realmente existe
        for agencia in self.agencias:
            if agencia.codigo == codigo:
                #apos buscar a agencia pelo código é preciso verificar se o gerente existe dentro
                #daquela agencia
                if agencia.busca_gerente():
                    #se o gerente existe ou se os dados se confirmam, abre se o painel do gerente
                    painel_do_gerente.painel_do_gerente(agencia)
                else:
                    return False

        print("codigo de agencia não encontrado")
        return False
    #buscando a agencia do cliente
    def busca_agencia_cliente(self):
        #verificando o volume de agencias no banco
        if len(self.agencias) == 0:
            print("Ainda não existem agencias")
            return
        #entrada do codigo da agencia pelo usuario
        codigo = input("De qual agencia voce e cliente: ").strip()#eliminando os espaços dessa entrada
        #verificando a natureza do codigo
        try:
            codigo = int(codigo)
        except:
            print("Codigo não reconhecido")
            return
        #buscando a gencia no vetor
        for agencia in self.agencias:
            #caso a agencia exista (pelo codigo)
            if agencia.codigo == codigo:
                #apos verificar agencia é preciso buscar o cliente
                agencia.busca_cliente()

        print("codigo de agencia não encontrado")

#Objeto da classe banco criado para operar os demais objetos e dados
banco_teste = Banco()
