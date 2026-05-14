import copy
import os
import random
from ag import AG

print("Problema de Roteamento (AG)")

# Entradas do usuário
tamanho_populacao = int(input("Tamanho da população (ex: 100): "))
taxa_selecao = int(input("Taxa de seleção % (ex: 20 a 40): "))
taxa_mutacao = int(input("Taxa de mutação % (ex: 5 a 20): "))
qtd_geracoes = int(input("Quantidade de gerações (ex: 500): "))

# Cálculo automático da reprodução
taxa_reproducao = 100 - taxa_selecao
populacao = []
nova_populacao = []

# Gerando população inicial
AG.gerar_populacao(populacao, tamanho_populacao)
populacao.sort()

print("\n--- Iniciando Evolução ---")

for g in range(qtd_geracoes):
    # Selecionando por Torneio
    AG.selecionar_por_torneio(populacao, nova_populacao, taxa_selecao)
    
    # Reproduzindo (Crossover)
    AG.reproduzir(populacao, nova_populacao, taxa_reproducao)
    
    # Mutação
    qtd_mutantes = int((taxa_mutacao / 100) * len(nova_populacao))
    for _ in range(qtd_mutantes):
        AG.mutar(nova_populacao)
    
    # Atualizando a população para a próxima geração
    populacao = copy.deepcopy(nova_populacao)
    nova_populacao.clear()
    
    # Ordena para que o melhor fique no topo
    populacao.sort()

    # Exibindo todos os indivíduos da geração atual
    print(f"\nGERAÇÃO {g+1}")
    AG.exibir(populacao)
    print(f"Melhor resultado da geração {g+1}: {populacao[0]}")
    
    # Critério de parada: Rota Perfeita (123456789 == 0 penalidade)
    if populacao[0].aptidao == 0:
        print("\nSUCESSO: ROTA PERFEITA ENCONTRADA! Na geração", g+1)
        break

if populacao[0].aptidao != 0:
    print("\nFim das gerações. O melhor resultado obtido foi:")
    print(f"{populacao[0]}Na geração: {g+1}")

print("\nVariáveis utilizadas:")
print(f"  - Tamanho da população: {tamanho_populacao}")
print(f"  - Taxa de seleção: {taxa_selecao}%")
print(f"  - Taxa de mutação: {taxa_mutacao}%")
print(f"  - Quantidade de gerações: {qtd_geracoes}\n")