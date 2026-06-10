# Perceptron: Implementação de Redes Neurais de Camada Única

Este repositório contém implementações educacionais do algoritmo Perceptron, um modelo clássico de rede neural artificial proposto por Frank Rosenblatt em 1958. O projeto tem como foco a demonstração prática de aprendizado supervisionado para problemas de classificação binária.

## Descrição do Algoritmo

O Perceptron é um classificador linear binário. Ele mapeia um vetor de entrada $x$ para um valor de saída $f(x)$ (neste caso, -1 ou 1) através de uma função de ativação degrau.

### Funcionamento Matemático
O aprendizado ocorre através do ajuste iterativo dos pesos ($w$). Para cada amostra, o modelo calcula:

1. **Potencial de Ativação:** O produto escalar entre o vetor de entrada e o vetor de pesos, somado ao bias (limiar).
   $Soma = \sum_{i=0}^{n} w_i \cdot x_i$
2. **Função de Ativação (Degrau):** Se a soma for maior ou igual a zero, o neurônio dispara (saída 1). Caso contrário, a saída é -1.
3. **Regra de Aprendizado:** Se a saída gerada for diferente da saída esperada, os pesos são atualizados conforme a regra:
   $w_{novo} = w_{atual} + \eta \cdot (erro) \cdot x$
   Onde $\eta$ (taxa de aprendizado) controla o tamanho do passo do ajuste.

## Cenários de Aplicação

O repositório inclui dois casos de uso práticos:

### 1. Previsão Climática
Classificação de condições atmosféricas entre "Sol" e "Chuva".
- **Entradas:** Histórico de umidade e pressão atmosférica (normalizados de 0 a 1).
- **Objetivo:** Criar uma fronteira linear que separa amostras de clima bom e ruim.

### 2. Análise de Risco de Crédito
Classificação de clientes para aprovação de empréstimos bancários.
- **Entradas:** Histórico de crédito e Renda mensal (normalizados).
- **Objetivo:** O modelo aprende a distinguir perfis de "Alto Risco" de "Baixo Risco" com base no histórico de pagamentos e capacidade financeira.

## Estrutura de Dados
Os dados de treinamento devem ser fornecidos em formato CSV sem cabeçalho, com a seguinte estrutura:

`atributo_1, atributo_2, classe_alvo`

Exemplo:
0.10, 0.20, -1
0.70, 0.65, 1

## Requisitos de Sistema

- Python 3.x
- Biblioteca Matplotlib (para visualização dos dados e fronteira de decisão)

Para instalar as dependências, execute:
pip install matplotlib

## Instruções de Execução
Clone o repositório ou baixe os arquivos.
Certifique-se de que os arquivos .csv estejam na mesma pasta do script principal.

## Considerações técnicas
- Linearidade: O Perceptron é um classificador linear. Ele apenas convergir-se-á para uma solução se os dados forem linearmente separáveis (ou seja, se for possível traçar uma linha reta que separe perfeitamente os dois grupos).

- Convergência: Caso os dados não sejam linearmente separáveis, o algoritmo entrará em um ciclo de erro infinito. Para mitigar isso, definimos um limite de geracoes no construtor da classe.

- Normalização: A normalização dos dados (valores entre 0 e 1) é crítica. Sem ela, atributos com escalas muito maiores dominariam o cálculo da soma, impedindo o aprendizado correto.