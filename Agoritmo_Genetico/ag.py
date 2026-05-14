import random
from cromossomo import Cromossomo
from util import Util

class AG:
    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao):
        # Cria vários cromossomos usando a função de embaralhar do Util
        for i in range(tamanho_populacao):
            populacao.append(Cromossomo(Util.gerar_rota_inicial()))

    @staticmethod
    def selecionar_por_torneio(populacao, nova_populacao, taxa_selecao):
        # Descobre quantos indivíduos devem ser selecionados
        qtd = int(taxa_selecao * len(populacao) / 100)
        
        # Usa o elitismo, ou seja, garante que o melhor de todos (índice 0) passe para a próxima geração
        nova_populacao.append(populacao[0])
        
        # Faz o torneio para preencher o restante da cota de seleção
        for _ in range(1, qtd):
            # Escolhe 3 candidatos aleatórios
            candidatos = [random.choice(populacao) for _ in range(3)]
            # Ordena os 3 e pega o que tiver a menor penalidade
            candidatos.sort()
            nova_populacao.append(candidatos[0])

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao):
        # Descobre quantos filhos devem ser gerados
        qtd = int(taxa_reproducao * len(populacao) / 100)
        
        for _ in range(0, qtd, 2):
            # Escolhe dois pais aleatórios da população antiga
            pai = random.choice(populacao)
            mae = random.choice(populacao)
            
            # Define o ponto de corte (metade)
            meio = len(pai.valor) // 2
            
            # Cria os valores dos filhos misturando as metades
            v_filho1 = pai.valor[:meio] + mae.valor[meio:]
            v_filho2 = mae.valor[:meio] + pai.valor[meio:]
            
            # Adiciona os novos cromossomos à lista
            nova_populacao.append(Cromossomo(v_filho1))
            nova_populacao.append(Cromossomo(v_filho2))

    @staticmethod
    def mutar(populacao):
        # Escolhe um indivíduo qualquer da lista para sofrer mutação
        alvo = random.choice(populacao)
        
        # Transforma em lista para conseguir trocar as letras de lugar
        letras = list(alvo.valor)
        
        # Sorteia duas posições e faz o SWAP
        a = random.randrange(len(letras))
        b = random.randrange(len(letras))
        letras[a], letras[b] = letras[b], letras[a]
        
        # Atualiza o valor do cromossomo na população com a nova ordem
        indice = populacao.index(alvo)
        populacao[indice] = Cromossomo("".join(letras))

    @staticmethod
    def exibir(populacao):
        for p in populacao:
            print(p)