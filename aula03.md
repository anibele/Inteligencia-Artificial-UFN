# Aula 03 - Resolvendo Jogos com Força Bruta em IA

---

# Introdução

Muitos problemas clássicos de Inteligência Artificial podem ser resolvidos utilizando **métodos de busca por força bruta**, explorando sistematicamente todas as possibilidades até encontrar uma solução.

A técnica mais comum é a **Busca em Profundidade (DFS - Depth First Search)**, frequentemente implementada de forma recursiva.

A ideia geral é:

```text
Estado Atual
      ↓
Gerar Próximo Estado
      ↓
Verificar Restrições
      ↓
Se válido:
    continuar busca
Senão:
    voltar (Backtracking)
```

---

# Backtracking

O Backtracking é uma estratégia utilizada quando uma decisão leva a um estado inválido.

Nesse caso:

1. Desfaz-se a última ação;
2. Tenta-se uma alternativa diferente;
3. Continua-se a busca.

```text
Escolha
   ↓
Válida?
   ↓ Sim
Continua

   ↓ Não
Volta e tenta outra opção
```

Essa técnica é amplamente utilizada em:

- Sudoku;
- Labirintos;
- Quebra-cabeças;
- Jogos de tabuleiro;
- Problemas de otimização.

---

# Problema do Sudoku

O Sudoku é um problema clássico de busca com restrições.

---

## Objetivo

Preencher todas as posições vazias da matriz respeitando as regras do jogo.

---

## Regras do Sudoku

Cada número deve aparecer apenas uma vez:

- Em cada linha;
- Em cada coluna;
- Em cada box 3x3.

---

## Modelagem do Problema

### Estados

Representam a situação atual do tabuleiro.

```java
int qtdCasasVazias;
int dimensao = 9;

int matriz[9][9];
```

Exemplo:

```text
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
```

Onde:

```text
0 = posição vazia
```

---

## Estado Inicial

Tabuleiro parcialmente preenchido.

```text
Números fornecidos pelo problema.
```

---

## Estado Meta

Não existem mais posições vazias.

```java
qtdCasasVazias == 0
```

---

## Regras de Transição

Selecionar a primeira célula vazia.

Tentar inserir:

```text
1
2
3
...
9
```

Sequencialmente.

Exemplo:

```text
Posição vazia:

[5][3][ ]

Tentativas:

1
2
3
...
9
```

---

## Restrições

Antes de inserir um número é necessário verificar:

### Linha

O número já existe na linha?

```java
verificarLinha()
```

---

### Coluna

O número já existe na coluna?

```java
verificarColuna()
```

---

### Box 3x3

O número já existe no quadrante?

```java
verificarBox()
```

---

## Visitados

Uma estratégia eficiente consiste em transformar a matriz em uma String.

Exemplo:

```text
530070000
600195000
098000060
...
```

Ou:

```text
530070000600195000...
```

Casas vazias:

```text
0
```

---

### Vantagem

Comparar Strings é muito mais eficiente do que comparar matrizes inteiras.

```java
HashSet<String> visitados
```

---

## Função Objetivo

```java
qtdCasasVazias == 0
```

Ou seja:

```text
Todas as células preenchidas
e
Nenhuma restrição violada
```

---

## Estratégia Geral

```text
Encontrar posição vazia
        ↓
Testar 1
        ↓
Válido?
        ↓
Sim → Continua
Não → Próximo número
        ↓
Sem opções?
        ↓
Backtracking
```

---

# Problema do Maze Runner (Labirinto)

Outro problema clássico de IA.

O objetivo é encontrar um caminho entre uma entrada e uma saída.

---

# Construção do Cenário

Utiliza-se uma matriz quadrada:

```java
char matriz[n][n];
```

---

## Elementos da Matriz

### Obstáculo

```text
#
```

Representa parede.

---

### Entrada

```text
E
```

Ponto inicial.

---

### Saída

```text
S
```

Objetivo.

---

### Espaço Livre

```text
' '
```

Posição por onde o agente pode andar.

---

## Exemplo

```text
E . . #
# . . #
# . # .
# . . S
```

---

# Geração do Labirinto

## 1. Gerar Obstáculos

Distribuir obstáculos aleatoriamente.

```java
'#'
```

A quantidade pode ser definida pelo usuário.

Exemplo:

```text
20% das células
30% das células
40% das células
```

---

## 2. Sortear Entrada

```java
'E'
```

Posição aleatória.

---

## 3. Sortear Saída

```java
'S'
```

Posição aleatória diferente da entrada.

---

# Objetivo do Problema

Encontrar:

```text
Um caminho entre E e S
```

Além disso:

```text
Relatar os movimentos realizados.
```

---

# Modelagem do Problema

---

## 1. Estados

Representam a posição atual do agente.

```java
char matriz[n][n];

int linhaEntrada;
int colunaEntrada;

int linhaSaida;
int colunaSaida;
```

---

## Estado Inicial

Posições sorteadas.

```text
E → posição inicial
S → posição final
```

---

## Estado Meta

Quando o agente alcança a saída.

```java
if(
   linhaEntrada == linhaSaida &&
   colunaEntrada == colunaSaida
)
```

---

## 2. Regras de Transição

Movimentos permitidos:

### Cima

```java
linhaEntrada--;
```

---

### Baixo

```java
linhaEntrada++;
```

---

### Esquerda

```java
colunaEntrada--;
```

---

### Direita

```java
colunaEntrada++;
```

---

## Representação

```text
       ↑
       |
← ---- X ---- →
       |
       ↓
```

---

## 3. Restrições

Impedem movimentos inválidos.

---

### Limite Superior

```java
linhaEntrada == 0
```

---

### Limite Inferior

```java
linhaEntrada == n - 1
```

---

### Limite Esquerdo

```java
colunaEntrada == 0
```

---

### Limite Direito

```java
colunaEntrada == n - 1
```

---

### Obstáculos

Não pode entrar em:

```text
#
```

Exemplo:

```java
if(matriz[l][c] == '#')
{
    // movimento inválido
}
```

---

### Espaços Permitidos

```java
if(
   matriz[l][c] == ' ' ||
   matriz[l][c] == 'S'
)
{
   // pode andar
}
```

---

## 4. Visitados

Necessários para evitar ciclos.

Exemplo:

```text
(2,3)
(2,4)
(3,4)
```

---

### Forma Simples

Concatenar linha e coluna.

```java
String chave =
       linhaEntrada +
       "," +
       colunaEntrada;
```

Exemplo:

```text
"2,3"
```

---

### Estrutura Recomendada

```java
HashSet<String> visitados;
```

---

## 5. Função Objetivo

A busca termina quando:

```java
linhaEntrada == linhaSaida &&
colunaEntrada == colunaSaida
```

Ou seja:

```text
O agente chegou à saída.
```

---

# Busca em Profundidade no Labirinto

Fluxo geral:

```text
Posição Atual
       ↓
Pode mover para cima?
       ↓
Sim
       ↓
Nova posição
       ↓
É a saída?
       ↓
Sim → Encerrar

Não
       ↓
Continuar busca
```

Caso fique preso:

```text
Sem movimentos válidos
       ↓
Backtracking
       ↓
Retorna para posição anterior
```

---

# Comparação dos Problemas

| Conceito | Sudoku | Labirinto |
|-----------|---------|-----------|
| Estado | Tabuleiro atual | Posição atual |
| Estado Inicial | Sudoku incompleto | Entrada (E) |
| Estado Meta | Tabuleiro completo | Chegar à saída |
| Transições | Inserir números | Mover-se |
| Restrições | Linha, coluna e box | Limites e obstáculos |
| Visitados | Matrizes já exploradas | Coordenadas visitadas |
| Busca Utilizada | Profundidade + Backtracking | Profundidade ou Amplitude |

---

# Conceitos-Chave para Memorizar

| Conceito | Definição |
|-----------|------------|
| Força Bruta | Exploração sistemática das possibilidades |
| DFS | Busca em Profundidade |
| Backtracking | Voltar quando uma escolha falha |
| Estado | Situação atual do problema |
| Restrição | Regra que impede estados inválidos |
| Visitados | Estados já explorados |
| Sudoku | Problema de preenchimento com restrições |
| Maze Runner | Problema de busca de caminho |
| Coordenada | Posição na matriz |
| Função Objetivo | Critério de sucesso da busca |
|

---

# Resumo Geral

Nesta aula foram apresentados dois problemas clássicos resolvidos através de busca:

### Sudoku

```text
Estado → Tabuleiro
Transição → Inserir número
Restrição → Linha, coluna e box
Meta → Não existir células vazias
```

### Maze Runner

```text
Estado → Posição atual
Transição → Movimentação
Restrição → Limites e obstáculos
Meta → Chegar à saída
```

Ambos utilizam os conceitos fundamentais da IA clássica:

- Estados;
- Regras de transição;
- Restrições;
- Visitados;
- Função objetivo;
- Busca em profundidade;
- Backtracking.