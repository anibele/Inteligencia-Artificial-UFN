import random

class Util:
    @staticmethod
    def gerar_rota_inicial():
        # Cria uma lista de 1 a 9
        cidades = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # Embaralha a lista
        random.shuffle(cidades)
        # Transforma a lista em string (ex: "312456789")
        return "".join(cidades)

    @staticmethod
    def gerar_caractere_aleatorio():
        # Usado na mutação para trocar uma cidade por outra de 1 a 9
        return str(random.randint(1, 9))