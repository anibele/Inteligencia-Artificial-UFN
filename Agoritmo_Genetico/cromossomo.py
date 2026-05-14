class Cromossomo:
    def __init__(self, valor):
        self.valor = valor
        # Calcula a penalidade assim que o cromossomo é criado
        self.aptidao = self.calcular_aptidao()
    
    def calcular_aptidao(self):
        nota = 0
        
        # Regra 1: Penalidade por ordem incorreta
        # Compara cada número com todos os números que vêm depois dele
        for i in range(len(self.valor)):
            for j in range(i + 1, len(self.valor)):
                # Se o número da esquerda for maior que o da direita, soma 10
                if int(self.valor[i]) > int(self.valor[j]):
                    nota += 10
        
        # Regra 2: Penalidade por números repetidos
        # Conta quantas vezes cada número de 1 a 9 aparece na rota
        cidades = "123456789"
        for c in cidades:
            contagem = self.valor.count(c)
            if contagem > 1:
                # Se uma cidade aparece mais de uma vez, punimos cada repetição com 20
                nota += (contagem - 1) * 20
                
        return nota

    # Método para verificar se um cromossomo é igual a outro
    def __eq__(self, other):
        return self.valor == other.valor

    # Método para decidir quem é "maior" na hora de ordenar por sort
    # É maior que outro se a penalidade dele for maior.
    def __gt__(self, other):
        return self.aptidao > other.aptidao

    # Transforma o objeto em texto para printar
    def __str__(self):
        return "Rota: " + str(self.valor) + " | Penalidade: " + str(self.aptidao)