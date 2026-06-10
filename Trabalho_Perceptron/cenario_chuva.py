import sys
import random
import csv
import matplotlib.pyplot as plt

class Perceptron:
    ## Primeira função de uma classe (método construtor de objetos)
    ## self é um parâmetro obrigatório que receberá a instância criada
    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, geracoes=1000, limiar=1):
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.geracoes = geracoes
        self.limiar = limiar
        self.n_amostras = len(amostras) # número de linhas (amostras)
        self.n_atributos = len(amostras[0]) # número de colunas (atributos)
        self.pesos = []
 
    ## Realizar o treinamento com conjunto de amostras fornecidas: relação entrada x saída
    def treinar(self):
        # Inserir o valor do limiar na posição "0" para cada amostra da lista "amostras"
        for amostra in self.amostras:
            amostra.insert(0, self.limiar)
        # Gerar valores aleatórios entre 0 e 1 (pesos) conforme o número de atributos
        for i in range(self.n_atributos):
            self.pesos.append(random.random())
        # Inserir o valor do limiar na posição "0" do vetor de pesos
        self.pesos.insert(0, self.limiar)
        # Inicializar contador de gerações
        geracoes = 0
        while True:
            aprendeu = True 
            # Para cada amostra
            for i in range(self.n_amostras):
                # Inicializar potencial de ativação
                soma = 0
                # Para cada atributo
                for j in range(self.n_atributos + 1):
                    # Multiplicar amostra e seu peso e também somar com o potencial que já tinha
                    soma += self.pesos[j] * self.amostras[i][j]
                # Obter a saída da rede considerando a função sinal
                saida_gerada = self.funcao_ativacao_signal(soma)
                # Verificar se a saída da rede é diferente da saída desejada
                if saida_gerada != self.saidas[i]:
                    # Calcular o erro
                    erro = self.saidas[i] - saida_gerada
                    # Fazer o ajuste dos pesos para cada elemento da amostra
                    for j in range(self.n_atributos + 1):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro * self.amostras[i][j]
                    
                    # se entrou no if é porque ainda não aprendeu
                    aprendeu = False
            geracoes += 1
            if aprendeu or geracoes > self.geracoes:
                print('Quantidade de gerações para aprender: %d\n' % geracoes)
                break

    ## Método para plotar o gráfico de separação linear
    def plotar_grafico(self):
        chuva_x, chuva_y = [], []
        sol_x, sol_y = [], []

        # Separar os pontos pelas classes
        for i in range(self.n_amostras):
            # Como o método treinar() insere o limiar na posição 0,
            # os atributos reais passam para os índices 1 (x) e 2 (y)
            x = self.amostras[i][1]
            y = self.amostras[i][2]
            
            if self.saidas[i] == 1:
                chuva_x.append(x)
                chuva_y.append(y)
            else:
                sol_x.append(x)
                sol_y.append(y)

        # Plotar os pontos simulando a imagem (Losangos vermelhos e Quadrados azuis)
        plt.scatter(sol_x, sol_y, color='#ff4000', marker='D', label='Sol (-1)')
        plt.scatter(chuva_x, chuva_y, color='#004080', marker='s', label='Chuva (1)')

        # Calcular e plotar a reta da Fronteira de Decisão
        # Equação: w0*limiar + w1*x + w2*y = 0  =>  y = (-w0*limiar - w1*x) / w2
        x_reta = [0, 1]
        y_reta = []
        for x in x_reta:
            y = (-self.pesos[0] * self.limiar - self.pesos[1] * x) / self.pesos[2]
            y_reta.append(y)
        
        plt.plot(x_reta, y_reta, color='darkgreen', linewidth=3, label='Fronteira de Decisão')

        # Configurar exibição do gráfico
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.1, 1.1)
        plt.title('Separação Linear - Chuva vs Sol')
        plt.xlabel('Umidade do Ar (Normalizada)')
        plt.ylabel('Pressão Atmosférica (Normalizada)')
        plt.legend(loc='best')
        plt.grid(True)
        
        # Exibe a janela gráfica
        plt.show()
 
    ## Testes para "novas" amostras
    def teste(self, amostra):
        amostra.insert(0, self.limiar)
        soma = 0
        for i in range(self.n_atributos + 1):
            soma += self.pesos[i] * amostra[i]
        saida_gerada = self.funcao_ativacao_signal(soma)

        if saida_gerada == 1:
            print('Classe: %d. Chuva' % saida_gerada)
        else:
            print('Classe: %d. Sol' % saida_gerada)
 
    ## Função funcao_ativacao_signal
    def funcao_ativacao_signal(self, soma):
        if soma >= 0:
            return 1
        return -1
 
# Leitura de dados do arquivo CSV
amostras = []
saidas = []

with open('dadosClimaticos.csv', 'r') as arquivo:
    linhas = csv.reader(arquivo)
    for linha in linhas:
        amostras.append([float(linha[0]), float(linha[1])])
        saidas.append(int(linha[2]))
 
# Chamar classe e fazer treinamento
rede = Perceptron(amostras, saidas)
rede.treinar()

# Execução ou produção
while (True):
    entrada = input('\nValor da Umidade (0 a 1) ou digite -1 para encerrar: ')
    
    if entrada == '-1':
        print('Encerrando a aplicação...')
        rede.plotar_grafico()
        break
        
    umidade = float(entrada)
    pressao = float(input('Valor da Pressão (0 a 1): '))
    print('Dados: Umidade', umidade , '| Pressão', pressao)
    rede.teste([umidade, pressao])