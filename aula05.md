# Aula 05 - Métodos de Busca Heurística

---

# Introdução

Nas aulas anteriores foram estudados os métodos de busca cegos (não informados), como:

- Busca em Amplitude (BFS);
- Busca em Profundidade (DFS).

Esses algoritmos exploram os estados sem possuir conhecimento sobre qual caminho é mais promissor.

Já os **métodos de busca heurística** utilizam informações adicionais para orientar a busca, tornando-a mais eficiente.

---

# O que é uma Heurística?

Uma heurística é uma estratégia ou estimativa utilizada para indicar quais estados parecem mais próximos da solução.

Ela não garante encontrar a solução ótima, mas normalmente reduz significativamente o número de estados explorados.

---

## Exemplo

Imagine que você deseja chegar a uma cidade.

Sem heurística:

```text
Testar todas as estradas possíveis.
```

Com heurística:

```text
Escolher as estradas que parecem levar mais rapidamente ao destino.
```

---

# Custos Utilizados em Busca Heurística

Os algoritmos heurísticos normalmente trabalham com dois tipos de custo.

---

## Custo Real - g(n)

Representa o custo efetivamente percorrido até o estado atual.

Pode representar:

- Distância percorrida;
- Quantidade de movimentos;
- Tempo gasto;
- Energia consumida.

### Exemplo

```text
Origem → A → B → C

g(C) = 3
```

Pois foram realizados três movimentos.

---

## Custo Estimado - h(n)

Representa uma estimativa do custo necessário para alcançar a solução.

É fornecido pela heurística.

### Exemplo

```text
Estado Atual → Objetivo

h(n) = 5
```

Significa que o algoritmo estima que faltam aproximadamente 5 passos para atingir a meta.

---

# Comparação dos Custos

| Custo | Significado |
|---------|-------------|
| g(n) | Custo real acumulado |
| h(n) | Custo estimado até a meta |
| f(n) | Custo total utilizado pelo algoritmo |

---

# Busca por Subida de Encosta (Hill Climbing)

Também chamada de:

```text
Hill Climbing
```

ou

```text
Subida de Encosta
```

---

## Ideia Principal

Sempre escolher o próximo estado que apresenta a melhor melhoria local.

O algoritmo tenta "subir a montanha" até atingir o topo.

---

## Funcionamento

1. Avalia os estados vizinhos;
2. Escolhe o melhor deles;
3. Move-se para esse estado;
4. Repete o processo.

---

## Características

### Utiliza

```text
Custo Real → g(n)
```

ou uma função de avaliação local.

### Tipo de Exploração

```text
Busca em Profundidade
```

Pois segue um único caminho por vez.

---

## Exemplo

```text
       10
      /  \
     8    9
    / \
   7   6
```

O algoritmo sobe sempre para o maior valor encontrado.

---

## Vantagens

- Simples;
- Pouco consumo de memória;
- Fácil implementação.

---

## Desvantagens

### Máximo Local

Pode parar em uma solução que parece boa, mas não é a melhor.

```text
          100
         /
        /
       /
      50
     /
    40

Algoritmo para em 50
sem descobrir o 100.
```

---

### Planaltos

Pode ficar preso em regiões onde todos os vizinhos possuem o mesmo valor.

---

# Busca Gulosa (Greedy Search)

Também chamada de:

```text
Greedy Search
```

---

## Ideia Principal

Escolher sempre o estado que parece mais próximo da solução.

Não considera o caminho já percorrido.

---

## Utiliza

```text
h(n)
```

Apenas o custo estimado.

---

## Tipo de Exploração

```text
Busca em Amplitude
```

Expandindo primeiro os estados considerados mais promissores.

---

## Critério

Escolher o menor valor de:

```text
h(n)
```

---

## Exemplo

```text
Estado A

B → h = 10
C → h = 3
D → h = 7
```

Escolha:

```text
C
```

Porque possui o menor custo estimado.

---

## Vantagens

- Muito rápida;
- Costuma encontrar soluções rapidamente;
- Explora menos estados.

---

## Desvantagens

- Não garante a melhor solução;
- Pode escolher caminhos aparentemente bons que se tornam ruins posteriormente.

---

## Exemplo de Problema

```text
Início
  |
  A
 / \
B   C

h(B)=1
h(C)=2
```

O algoritmo escolhe B imediatamente, mesmo que C possa levar a uma solução melhor.

---

# Busca A*

A* é considerado um dos algoritmos mais importantes da Inteligência Artificial clássica.

Ele combina as vantagens da Busca Gulosa e da Busca de Custo Uniforme.

---

# Ideia Principal

Em vez de considerar apenas:

```text
g(n)
```

ou apenas:

```text
h(n)
```

ele utiliza ambos.

---

## Função de Avaliação

:contentReference[oaicite:0]{index=0}

Onde:

| Função | Significado |
|----------|-------------|
| g(n) | Custo real acumulado |
| h(n) | Custo estimado até a meta |
| f(n) | Custo total estimado |

---

## Interpretação

```text
f(n)
=
o que já foi gasto
+
o que ainda falta gastar
```

---

## Exemplo

Estado A:

```text
g(n) = 4
h(n) = 6

f(n) = 10
```

Estado B:

```text
g(n) = 8
h(n) = 1

f(n) = 9
```

Escolha:

```text
Estado B
```

Porque possui menor valor de:

```text
f(n)
```

---

## Tipo de Exploração

Normalmente implementado utilizando:

```text
Busca em Amplitude Priorizada
```

Ou seja, os estados são organizados em uma fila de prioridade.

---

## Vantagens

### Solução Ótima

Quando a heurística é admissível, o A* encontra a melhor solução.

---

### Menos Exploração

Explora menos estados que métodos cegos.

---

### Considera Caminho Percorrido

Evita decisões precipitadas da busca gulosa.

---

## Desvantagens

### Consumo de Memória

Pode armazenar muitos estados.

---

### Dependência da Heurística

Uma heurística ruim reduz significativamente o desempenho.

---

# Comparação dos Métodos

| Algoritmo | Utiliza g(n) | Utiliza h(n) | Garante Melhor Solução |
|------------|-------------|-------------|------------------------|
| DFS | Sim | Não | Não |
| Hill Climbing | Sim | Não | Não |
| Greedy | Não | Sim | Não |
| A* | Sim | Sim | Sim* |

\* Quando a heurística é admissível.

---

# Resumo Visual

```text
BUSCAS HEURÍSTICAS

                Busca Heurística
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   Hill Climbing      Greedy           A*
        │               │               │
        ▼               ▼               ▼
     Usa g(n)        Usa h(n)     Usa g(n)+h(n)
        │               │               │
        ▼               ▼               ▼
 Profundidade      Amplitude      Amplitude
                                      +
                              Correção Heurística
```

---

# Exemplo Aplicado ao Labirinto

Imagine um labirinto.

### Hill Climbing

```text
Segue sempre a direção que parece melhorar imediatamente.
```

Pode ficar preso.

---

### Greedy

```text
Escolhe a posição aparentemente mais próxima da saída.
```

Pode tomar atalhos ruins.

---

### A*

```text
Considera:
- Distância já percorrida;
- Distância estimada até a saída.
```

Normalmente encontra o melhor caminho.

---

# Conceitos-Chave para Memorizar

| Conceito | Definição |
|-----------|------------|
| Heurística | Informação utilizada para orientar a busca |
| g(n) | Custo real acumulado |
| h(n) | Custo estimado até a meta |
| f(n) | Soma de g(n) e h(n) |
| Hill Climbing | Escolhe a melhor melhoria local |
| Greedy | Escolhe o estado aparentemente mais próximo da meta |
| A* | Combina custo real e custo estimado |
| Máximo Local | Solução aparentemente boa mas não ótima |
| Heurística Admissível | Nunca superestima o custo real |
| Fila de Prioridade | Estrutura usada pelo A* |
|

---

# Resumo Geral

Os métodos de busca heurística utilizam informações adicionais para tornar a busca mais eficiente.

### Hill Climbing

```text
Utiliza g(n)
Busca em Profundidade
Escolhe o melhor vizinho local
```

### Greedy

```text
Utiliza h(n)
Busca em Amplitude
Escolhe o estado aparentemente mais próximo da meta
```

### A*

```text
Utiliza g(n) + h(n)
Busca em Amplitude Priorizada
Combina custo real e custo estimado
```

Entre os três métodos, o **A\*** é geralmente considerado o mais poderoso, pois consegue equilibrar eficiência e qualidade da solução encontrada.