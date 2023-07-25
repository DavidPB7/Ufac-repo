class Cliente:
    def __init__(self, nome, endereco, cpf, email, senha):
        self.__nome = nome
        self.__endereco = endereco
        self.__CPF = cpf
        self.__email = email
        self.__senha = senha

    # Métodos getters para acessar os atributos privados
    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_CPF(self):
        return self.__CPF

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha