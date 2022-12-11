# a função valida cpf sera usado para validar documentos do cliente
from Administração import valida_cpf
# A agencia pode criar objetos do tipo cliente
from Administração import Cliente
# a classe agencia com suas funções tambem podem ir de um painel para outro
from Administrador_Banco import painel_do_cliente
from Administrador_Banco import painel_do_gerente


class Agencia:
    def __init__(self, codigo, uf, cidade):
        self.__codigo = codigo
        self.UF = uf
        self.clientes = []
        self.gerente = {'nome': '', 'senha': ''}
        self.gerentes = []
        self.cidade = cidade

    # criar os setters e os getters de cada um
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    # função que valida algum gerente na agencia
    def busca_gerente(self):
        # verificando o volume de gerentes na agencia
        if len(self.gerentes) == 0:
            print("Não existem gerentes para essa agencia")
            return False
        # entradas do gerente
        nome = input("Nome do gerente: ")
        senha = input("Senha do gerente: ")
        # buscando o possivel gerente no vetor gerentes
        for gerente in self.gerentes:
            # verificando os dados nome e senha
            if gerente['nome'] == nome and gerente['senha'] == senha:
                # sendo verdadeiro os dados o painel do gerente abre e repete ate que o retorno
                # seja falso, apenas um comando no painel do gerente retorna falso
                while True:
                    if painel_do_gerente.painel_do_gerente(self) == True:
                        pass
                    else:
                        return False
            else:
                pass
        return False

    # função que faz a busca do cliente
    def busca_cliente(self):
        # verificando o volume de clientes da agencia
        if len(self.clientes) == 0:
            print("Não existem clientes para essa agencia")
            return
        # entradas do cliente
        nome = input("Nome do cliente: ")
        senha = input("Senha do cliente: ")
        cpf = input("CPF do cliente: ")
        for cliente in self.clientes:
            # verificando os dados do cliente
            if cliente.nome == nome and cliente.senha == senha and cliente.cpf:
                # sendo verdadeiro abre se o painel do cliente em loop infinito
                # ate que o retorno seja falso apenas um comando retorna Falso
                while painel_do_cliente.painel_do_cliente(cliente):
                    pass
                else:
                    return
            else:
                pass
        print("Dados invalidos")
        return False

    # função para criar objetos da classe cliente
    def criar_cliente(self):
        nome = input("Nome do cliente (verificado em documento): ")
        while True:
            # o cpf é um documento importante ele deve ser valido segundo o algoritimo do proprio governo
            cpf = input("CPF do cliente (apenas numeros): ")
            try:
                valida_cpf.valida_cpf(cpf)
            except:
                print("Algo de errado com o cpf")
                return

            else:
                if valida_cpf.valida_cpf(cpf):
                    break
                else:
                    print("CPF invalido")

        while True:
            # apenas dois tipos de sexo serão aceito
            sexo = input("Sexo do cliente [M][F]: ").upper()
            if sexo == 'M' or sexo == 'F':
                break
            else:
                pass

        while True:
            # a senha para que passe segurança deve ser maior que 7 digitos
            senha = input("Defina uma senha para esse usuario [7 digitos ou mais]: ")
            if len(senha) < 6:
                print()
            else:
                break
        # a criação dos objetos da classe cliente
        cliente = Cliente.Cliente(nome, sexo, cpf, senha)
        self.clientes.append(cliente)

    # função para criar gerentes
    def criar_gerente(self, nome, senha):
        gerente = {'nome': '', 'senha': ''}
        gerente['nome'] = nome
        gerente['senha'] = senha
        self.gerentes.append(gerente)

    # relatorios da agencia
    def relatorio_da_agencia(self):
        print(f"UF - onde a agencia está: {self.UF}\n"
              f"cidade onde a agencia está: {self.cidade}\n"
              f"Quantidade de clientes: {len(self.clientes)}")
