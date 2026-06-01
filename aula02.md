# Aula 02 - Técnicas e Metodologias de Inteligência Artificial

---

# Sistemas de Comportamento Inteligente

A Inteligência Artificial pode ser vista como a combinação de três grandes componentes:

```text
                Sistema Inteligente
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Base de          Motor de         Aprendizado
 Conhecimento     Raciocínio       de Máquina
```

---

# 1. Base de Conhecimento

Responsável por armazenar informações, fatos, regras e experiências acumuladas pelo sistema.

É a memória do sistema inteligente.

## Funções

- Armazenar conhecimento;
- Representar experiências anteriores;
- Permitir consultas e inferências;
- Fornecer dados para o processo de tomada de decisão.

## Tecnologias Relacionadas

- Prolog;
- Sistemas Multiagentes (SMA);
- Sistemas Especialistas;
- Bancos de Conhecimento.

---

# 2. Motor de Raciocínio

Responsável por utilizar o conhecimento armazenado para gerar conclusões e tomar decisões.

Também é chamado de:

- Raciocínio Automatizado;
- Mecanismo de Inferência;
- Motor de Inferência.

---

## Tipos de Raciocínio

### Dedução

Parte de regras gerais para obter conclusões específicas.

```text
Geral → Específico
```

### Indução

Parte de exemplos específicos para construir uma regra geral.

```text
Específico → Geral
```

---

# Métodos de Busca

Os métodos de busca são utilizados para encontrar soluções em espaços de estados.

A solução é obtida através da exploração de estados possíveis até encontrar a meta.

---

## Buscas Cegas (Não Informadas)

Não possuem conhecimento adicional sobre o problema.

Apenas exploram os estados disponíveis.

### Busca em Amplitude (BFS)

Explora todos os estados de um nível antes de avançar para o próximo.

#### Características

- Completa;
- Garante o menor caminho (quando os custos são iguais);
- Consome muita memória.

```text
Nível 0
   A
  / \
 B   C
/ \ / \
D E F G
```

Ordem:

```text
A → B → C → D → E → F → G
```

---

### Busca em Profundidade (DFS)

Explora um caminho até o máximo possível antes de retornar.

#### Características

- Baixo consumo de memória;
- Pode encontrar soluções rapidamente;
- Não garante o menor caminho;
- Pode entrar em caminhos muito longos.

```text
A → B → D
```

Somente após retornar:

```text
A → B → E → C ...
```

---

## Buscas Heurísticas (Informadas)

Utilizam informações adicionais para direcionar a busca.

O objetivo é reduzir a quantidade de estados explorados.

---

### Subida de Encosta (Hill Climbing)

Sempre escolhe o vizinho que parece melhor.

#### Vantagem

- Simples;
- Rápida.

#### Desvantagem

- Pode ficar presa em máximos locais.

```text
Estado Atual
      ↓
 Melhor Vizinho
      ↓
 Melhor Vizinho
      ↓
 Solução (ou máximo local)
```

---

### Busca Gulosa (Greedy Search)

Escolhe o estado que parece mais próximo da solução.

Utiliza uma função heurística:

```text
h(n)
```

Onde:

- `h(n)` = estimativa da distância até a meta.

---

### Busca A*

Uma das técnicas mais importantes da IA clássica.

Utiliza:

```text
f(n) = g(n) + h(n)
```

Onde:

- `g(n)` = custo real percorrido;
- `h(n)` = estimativa até a meta;
- `f(n)` = custo total estimado.

:contentReference[oaicite:0]{index=0}

### Vantagens

- Completa;
- Ótima (encontra a melhor solução quando a heurística é admissível);
- Muito utilizada em jogos e planejamento de rotas.

---

### Algoritmos Genéticos

Inspirados na evolução biológica.

Baseiam-se em:

- População;
- Seleção;
- Cruzamento;
- Mutação;
- Aptidão (Fitness).

Fluxo básico:

```text
População Inicial
        ↓
 Avaliação
        ↓
 Seleção
        ↓
 Cruzamento
        ↓
 Mutação
        ↓
 Nova Geração
```

---

# 3. Aprendizado de Máquina

Permite que sistemas aprendam padrões a partir de exemplos.

Em vez de programar explicitamente todas as regras, o sistema aprende observando dados.

---

## Objetivos

- Classificar;
- Prever;
- Reconhecer padrões;
- Detectar anomalias;
- Tomar decisões.

---

## Redes Neurais Artificiais (RNA)

Modelo inspirado no funcionamento dos neurônios biológicos.

São amplamente utilizadas para:

- Reconhecimento facial;
- Reconhecimento de voz;
- Processamento de linguagem natural;
- Visão computacional;
- Sistemas de recomendação.

---

# Modelagem de Problemas para Busca

Independentemente do problema, a modelagem geralmente segue os mesmos componentes.

---

## 1. Estados

Representam todas as situações possíveis do problema.

### Tipos de Estado

#### Estado Inicial

Ponto de partida.

#### Estados Intermediários

Situações geradas durante a busca.

#### Estado Final (Meta)

Objetivo que deve ser alcançado.

---

## 2. Regras de Transição

Definem as operações permitidas.

São responsáveis por gerar novos estados.

Na implementação normalmente correspondem a métodos.

---

## 3. Restrições

Definem estados inválidos.

Impedem que o algoritmo gere soluções impossíveis.

---

## 4. Estrutura de Visitados

Armazena estados já explorados.

Pode ser implementada com:

- Lista;
- Árvore;
- HashMap;
- HashSet.

Objetivos:

- Evitar ciclos;
- Evitar processamento repetido;
- Melhorar desempenho.

---

## 5. Função Objetivo (Meta)

Determina quando a solução foi encontrada.

---

# Problema das Torres de Hanói

Um dos problemas clássicos de IA e Recursão.

---

## Objetivo

Mover todos os discos da torre inicial para outra torre.

---

## Regras

1. Apenas um disco pode ser movido por vez;
2. Nunca colocar um disco maior sobre um menor;
3. Utilizar as torres auxiliares quando necessário.

---

## Representação dos Estados

```java
Stack t1 = new Stack();
Stack t2 = new Stack();
Stack t3 = new Stack();
```

Cada pilha representa uma torre.

---

## Estado Inicial

```java
t1.push(3);
t1.push(2);
t1.push(1);
```

Representação:

```text
T1: 3 2 1
T2:
T3:
```

---

## Estado Meta

Todos os discos devem estar em outra torre.

Exemplo:

```java
t1.empty() && t2.empty()
```

Representação:

```text
T1:
T2:
T3: 3 2 1
```

---

## Regras de Transição

Movimentos possíveis:

```text
T1 → T2
T1 → T3
T2 → T1
T2 → T3
T3 → T1
T3 → T2
```

Cada movimento gera um novo estado.

---

## Restrição

Movimentos inválidos não podem ocorrer.

```java
public boolean ehValido(Stack origem,
                        Stack destino)
{
    if(origem.empty())
        return false;

    if(!destino.empty() &&
       (int)origem.peek() >
       (int)destino.peek())
        return false;

    return true;
}
```

### Exemplo Inválido

```text
  1
  2
  3
```

Mover:

```text
3 → 1
```

Não permitido.

---

## Visitados

Podem ser armazenados em:

- Lista;
- Árvore;
- HashMap;
- HashSet.

Evita revisitar estados já explorados.

---

# Problema das Jarras

Outro problema clássico de busca.

---

## Situação

Existem:

- Uma jarra de 4 litros;
- Uma jarra de 3 litros;
- Uma fonte infinita de água.

---

## Objetivo

Obter exatamente:

```text
2 litros
```

em uma das jarras.

---

## Representação do Estado

```java
class Estado{
    int j1;
    int j2;

    public Estado(int j1, int j2){
        this.j1 = j1;
        this.j2 = j2;
    }
}
```

---

## Estado Inicial

```text
(0,0)
```

Ambas as jarras vazias.

---

## Estado Meta

```java
public boolean ehMeta(){
    return (
        (j1 == 2 && j2 == 0) ||
        (j1 == 0 && j2 == 2)
    );
}
```

---

## Operadores (Regras de Transição)

### Encher Jarra 1

```java
encherJ1()
```

Resultado:

```text
(4, j2)
```

---

### Encher Jarra 2

```java
encherJ2()
```

Resultado:

```text
(j1, 3)
```

---

### Esvaziar Jarra 1

```java
esvaziarJ1()
```

Resultado:

```text
(0, j2)
```

---

### Esvaziar Jarra 2

```java
esvaziarJ2()
```

Resultado:

```text
(j1, 0)
```

---

### Despejar Jarra 2 em Jarra 1

Transfere água até:

- J1 ficar cheia; ou
- J2 ficar vazia.

```java
despejarJ2_J1()
```

---

## Exemplo de Solução

```text
(0,0)
↓
(0,3)
↓
(3,0)
↓
(3,3)
↓
(4,2)
↓
(0,2)
```

Meta alcançada.

---

# Resumo Geral

Todo problema clássico de busca em IA pode ser modelado utilizando:

1. Estado Inicial;
2. Estados Intermediários;
3. Estado Meta;
4. Regras de Transição;
5. Restrições;
6. Estrutura de Visitados;
7. Algoritmo de Busca.

---

# Conceitos-Chave para Memorizar

| Conceito | Definição |
|-----------|------------|
| Estado | Situação atual do problema |
| Estado Inicial | Ponto de partida |
| Estado Meta | Objetivo desejado |
| Transição | Mudança entre estados |
| Restrição | Regra que impede estados inválidos |
| Visitados | Estados já explorados |
| BFS | Busca em Amplitude |
| DFS | Busca em Profundidade |
| Busca Gulosa | Escolhe o estado aparentemente mais promissor |
| A* | Usa custo real + heurística |
| Hill Climbing | Sempre sobe para o melhor vizinho |
| Algoritmo Genético | Busca baseada na evolução biológica |
| RNA | Rede Neural Artificial |
| Heurística | Informação utilizada para guiar a busca |
|