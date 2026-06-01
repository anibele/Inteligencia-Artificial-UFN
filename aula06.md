# Aula 06 - Revisão dos Métodos de Busca e Introdução ao Prolog

---

# Revisão Geral

Até este ponto da disciplina foram estudados os principais conceitos da Inteligência Artificial Clássica:

- Modelagem de problemas;
- Métodos de busca;
- Busca cega;
- Busca heurística;
- Representação do conhecimento.

O objetivo principal da IA clássica é:

```text
Encontrar soluções para problemas.
```

---

# Métodos de Busca

Um método de busca procura encontrar:

- Um estado desejado;
- Uma solução aproximada;
- Uma sequência de passos até a solução.

---

## Objetivo de uma Busca

```text
Estado Inicial
      ↓
Estados Intermediários
      ↓
Estado Final (Meta)
```

Exemplo:

```text
Labirinto

Entrada
   ↓
Movimentos
   ↓
Saída
```

---

# Tipos de Problemas em IA

De forma geral, os problemas estudados podem ser divididos em duas categorias.

---

## 1. Problemas de Diagnóstico

Objetivo:

```text
Reconhecer padrões.
```

São resolvidos através de treinamento e aprendizado.

### Exemplos

- Diagnóstico médico;
- Reconhecimento facial;
- Classificação de documentos;
- Reconhecimento de voz;
- Detecção de fraudes.

---

## Característica Principal

Não é necessário descobrir uma sequência de passos.

O sistema precisa apenas identificar corretamente um padrão.

```text
Entrada
    ↓
Reconhecimento
    ↓
Classificação
```

---

## 2. Problemas de Busca

Objetivo:

```text
Descobrir uma sequência de ações
até atingir um estado desejado.
```

### Exemplos

- Labirintos;
- Sudoku;
- Torres de Hanói;
- Problema das Jarras;
- Planejamento de rotas.

---

## Característica Principal

Não sabemos previamente quais passos levarão à solução.

A IA precisa descobrir o caminho.

```text
Estado Inicial
      ↓
Busca
      ↓
Estado Final
```

---

# Motores de Raciocínio

Os métodos de busca são considerados motores de raciocínio.

Eles utilizam o conhecimento disponível para deduzir soluções.

---

## Raciocínio Dedutivo

Parte de informações conhecidas para chegar a uma conclusão.

```text
Conhecimento
      ↓
Inferência
      ↓
Conclusão
```

---

## Busca por Força Bruta

A forma mais simples de dedução é explorar sistematicamente todas as possibilidades.

Normalmente associada à:

```text
Busca em Profundidade (DFS)
```

---

# Componentes de um Sistema Inteligente

Todo sistema inteligente possui três componentes fundamentais.

---

# 1. Base de Conhecimento

Responsável por armazenar:

- Fatos;
- Regras;
- Experiências;
- Conhecimento do domínio.

### Exemplos

- Banco de dados;
- Base de fatos do Prolog;
- Sistemas especialistas.

---

# 2. Motores de Raciocínio

Responsáveis por utilizar o conhecimento armazenado para resolver problemas.

---

## Fontes de Informação

As "dicas" utilizadas pelo motor podem vir de:

- Conhecimento matemático;
- Especialistas humanos;
- Experiências anteriores;
- Heurísticas.

---

## Custos Utilizados

### Custo Real

Representa o que já foi gasto.

```text
g(n)
```

---

### Custo Estimado

Representa o que ainda falta para atingir a meta.

```text
h(n)
```

---

# Classificação dos Motores de Busca

---

## 2.1 Métodos Cegos (Força Bruta)

Não utilizam conhecimento adicional.

Exploram os estados sistematicamente.

---

### Busca em Profundidade (DFS)

```text
Profundidade
```

Características:

- Segue um caminho até o fim;
- Pouca memória;
- Motor utilizado pelo Prolog.

---

### Busca em Amplitude (BFS)

```text
Largura / Amplitude
```

Características:

- Explora nível por nível;
- Encontra o menor caminho (quando os custos são iguais);
- Maior consumo de memória.

---

## 2.2 Métodos Heurísticos (Informados)

Utilizam informações extras para guiar a busca.

---

### Subida de Encosta (Hill Climbing)

Baseado em:

```text
Busca em Profundidade
```

Utiliza:

```text
g(n)
```

Procura sempre o melhor vizinho local.

---

### Busca Gulosa (Greedy)

Baseada em:

```text
Busca em Amplitude
```

Utiliza:

```text
h(n)
```

Escolhe o estado aparentemente mais próximo da meta.

---

### Busca A*

Baseada em:

```text
Busca em Amplitude
```

Utiliza:

:contentReference[oaicite:0]{index=0}

Onde:

- `g(n)` = custo real;
- `h(n)` = custo estimado;
- `f(n)` = custo total.

---

# 3. Aprendizado de Máquina

Também conhecido como:

```text
Machine Learning
```

---

## Objetivo

Reconhecer padrões através de exemplos.

O sistema aprende observando amostras.

```text
Dados
    ↓
Treinamento
    ↓
Modelo
    ↓
Predição
```

---

## Exemplos

- Redes Neurais;
- Classificadores;
- Sistemas de recomendação;
- Reconhecimento de imagens.

---

# Introdução ao Prolog

---

# O que é Prolog?

Prolog significa:

```text
PROgramming in LOGic
```

É uma linguagem baseada em lógica matemática.

Diferente das linguagens tradicionais, em Prolog o programador descreve:

- Fatos;
- Regras;
- Relações.

O mecanismo de inferência descobre as respostas automaticamente.

---

# Ambiente Online

Pode ser utilizado diretamente no navegador:

https://swish.swi-prolog.org/

---

# Como o Prolog Funciona?

O Prolog utiliza:

```text
Base de Conhecimento
+
Motor de Inferência
```

para responder perguntas.

---

# Motor do Prolog

O motor do Prolog utiliza:

```text
Raciocínio Dedutivo
```

e

```text
Busca em Profundidade (DFS)
```

para encontrar soluções.

---

# Estrutura Básica

Um predicado possui a forma:

```prolog
nome(argumentos).
```

Exemplo:

```prolog
estado(luz, ligado).
```

Leitura:

```text
A luz está ligada.
```

---

# Tipos de Argumentos

---

## 1. Átomos (Objetos)

Começam com letra minúscula.

Exemplos:

```prolog
alex
professor
aluno
ligado
desligado
```

---

## 2. Literais (Strings)

Representam textos.

Exemplo:

```prolog
"Matheus dos Reis"
```

---

## 3. Variáveis

Começam com letra maiúscula.

Exemplos:

```prolog
X
Pessoa
Aluno
Professor
```

As variáveis são utilizadas nas consultas.

---

# Fatos

Um fato representa uma afirmação considerada verdadeira.

Também pode ser chamado de:

- Sentença;
- Predicado;
- Assertiva.

---

## Exemplo

```prolog
papel(alex, professor).
```

Leitura:

```text
Alex possui o papel de professor.
```

---

# Exemplos de Fatos

```prolog
papel(alex, professor).

papel(joao, aluno).

papel(gustavo, aluno).

papel(gustavo, monitor).

estado(luz, ligado).

estado(ar_condicionado, desligado).

matriculado(matheus, jogos, ia).

matriculado(matheus, jogos, design).

progenitor(jura, alex).

progenitor(jura, tina).

progenitor(alex, dante).

progenitor(simone, dante).
```

---

# Predicados

Um predicado é definido por:

```text
Nome + Quantidade de Argumentos
```

---

## Predicados do Exemplo

### papel/2

Possui:

```text
2 argumentos
```

```prolog
papel(alex, professor).
```

---

### estado/2

Possui:

```text
2 argumentos
```

```prolog
estado(luz, ligado).
```

---

### matriculado/3

Possui:

```text
3 argumentos
```

```prolog
matriculado(matheus, jogos, ia).
```

---

### progenitor/2

Possui:

```text
2 argumentos
```

```prolog
progenitor(jura, alex).
```

---

## Quantos Predicados Existem?

Neste exemplo existem:

| Predicado | Aridade |
|------------|----------|
| papel | 2 |
| estado | 2 |
| matriculado | 3 |
| progenitor | 2 |

Portanto:

```text
4 predicados diferentes
```

Mesmo que existam várias linhas para cada um deles.

---

# Consultas em Prolog

Após definir os fatos, podemos fazer perguntas.

---

## Exemplo 1

Consulta:

```prolog
?- papel(gustavo, aluno).
```

Resposta:

```text
true.
```

---

## Exemplo 2

Consulta:

```prolog
?- papel(gustavo, professor).
```

Resposta:

```text
false.
```

---

## Exemplo 3

Consulta:

```prolog
?- papel(gustavo, X).
```

Resposta:

```text
X = aluno
X = monitor
```

O Prolog procura todos os fatos compatíveis.

---

# Resumo Visual

```text
                 Sistema Inteligente
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
 Base de          Motor de Raciocínio   Aprendizado
 Conhecimento            │              de Máquina
                          │
            ┌─────────────┼─────────────┐
            ▼                           ▼
      Busca Cega                Busca Heurística
            │                           │
      DFS / BFS          Hill Climbing / Greedy / A*
                          │
                          ▼
                       Prolog
               (DFS + Dedução)
```

---

# Conceitos-Chave para Memorizar

| Conceito | Definição |
|-----------|------------|
| Base de Conhecimento | Armazena fatos e regras |
| Motor de Raciocínio | Resolve problemas usando o conhecimento |
| DFS | Busca em Profundidade |
| BFS | Busca em Amplitude |
| g(n) | Custo real |
| h(n) | Custo estimado |
| A* | Utiliza g(n) + h(n) |
| Machine Learning | Aprendizado por exemplos |
| Prolog | Linguagem baseada em lógica |
| Fato | Informação considerada verdadeira |
| Predicado | Relação lógica |
| Variável | Argumento iniciado por letra maiúscula |
| Átomo | Argumento iniciado por letra minúscula |
| Aridade | Quantidade de argumentos de um predicado |
|

---

# Resumo Geral

Nesta aula foi realizada uma revisão dos principais conceitos de IA estudados até o momento e iniciada a introdução ao Prolog.

O Prolog utiliza uma **base de fatos**, um **motor dedutivo baseado em busca em profundidade** e permite representar conhecimento através de **predicados**, tornando-se uma das linguagens clássicas para implementação de sistemas especialistas e raciocínio lógico.