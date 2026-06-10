import random
import csv
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, geracoes=1000, limiar=1):
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.geracoes = geracoes
        self.limiar = limiar
        self.n_amostras = len(amostras)
        self.n_atributos = len(amostras[0])
        self.pesos = []
 
    def treinar(self):
        for amostra in self.amostras:
            amostra.insert(0, self.limiar)
        
        for i in range(self.n_atributos):
            self.pesos.append(random.random())
        self.pesos.insert(0, self.limiar)
        
        geracoes = 0
        while True:
            aprendeu = True 
            for i in range(self.n_amostras):
                soma = 0
                for j in range(self.n_atributos + 1):
                    soma += self.pesos[j] * self.amostras[i][j]
                
                saida_gerada = self.funcao_ativacao_signal(soma)
                
                if saida_gerada != self.saidas[i]:
                    erro = self.saidas[i] - saida_gerada
                    for j in range(self.n_atributos + 1):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro * self.amostras[i][j]
                    aprendeu = False
            geracoes += 1
            if aprendeu or geracoes > self.geracoes:
                print('Quantidade de gerações para aprender: %d\n' % geracoes)
                break

    def plotar_grafico(self):
        aprovado_x, aprovado_y = [], []
        recusado_x, recusado_y = [], []

        for i in range(self.n_amostras):
            x = self.amostras[i][1]
            y = self.amostras[i][2]
            
            if self.saidas[i] == 1:
                aprovado_x.append(x)
                aprovado_y.append(y)
            else:
                recusado_x.append(x)
                recusado_y.append(y)

        plt.scatter(recusado_x, recusado_y, color='red', marker='D', label='Alto Risco (Recusado)')
        plt.scatter(aprovado_x, aprovado_y, color='blue', marker='s', label='Baixo Risco (Aprovado)')

        x_reta = [0, 1]
        y_reta = []
        for x in x_reta:
            y = (-self.pesos[0] * self.limiar - self.pesos[1] * x) / self.pesos[2]
            y_reta.append(y)
        
        plt.plot(x_reta, y_reta, color='darkgreen', linewidth=3, label='Fronteira de Decisão')

        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.title('Análise de Risco de Crédito')
        plt.xlabel('Histórico de Crédito')
        plt.ylabel('Renda Mensal')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()
 
    def teste(self, amostra):
        amostra.insert(0, self.limiar)
        soma = 0
        for i in range(self.n_atributos + 1):
            soma += self.pesos[i] * amostra[i]
        saida_gerada = self.funcao_ativacao_signal(soma)

        if saida_gerada == 1:
            print('Resultado: Aprovado (Baixo Risco)')
        else:
            print('Resultado: Recusado (Alto Risco)')
 
    def funcao_ativacao_signal(self, soma):
        return 1 if soma >= 0 else -1
 
# Leitura de dados
amostras = []
saidas = []

with open('dadosFinanceiros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        amostras.append([float(linha[0]), float(linha[1])])
        saidas.append(int(linha[2]))
 
rede = Perceptron(amostras, saidas)
rede.treinar()

while True:
    entrada = input('\nHistórico de Crédito (0 a 1) ou digite -1 para encerrar: ')
    
    if entrada.lower() == '-1':
        rede.plotar_grafico()
        print('Encerrando a aplicação...')
        break
        
    hist = float(entrada)
    renda = float(input('Renda Mensal (0 a 1): '))
    print('Dados: Histórico', hist, '| Renda', renda)
    rede.teste([hist, renda])