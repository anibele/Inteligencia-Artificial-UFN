# Aula 01 - Conceitos Básicos e Introdução à IA

**Material da disciplina:**  
https://github.com/alexandrezamberlan/tecnicasIA

---

# O que é Inteligência Artificial?

A Inteligência Artificial (IA) é uma área da Computação que busca desenvolver sistemas capazes de realizar tarefas que normalmente exigiriam inteligência humana, como:

- Aprender;
- Raciocinar;
- Tomar decisões;
- Resolver problemas;
- Reconhecer padrões;
- Interpretar informações;
- Adaptar-se a novas situações.

---

# Aspectos de um Sistema

Todo sistema pode ser analisado sob dois aspectos principais:

## Aspecto Estrutural

Refere-se à constituição do sistema.

Exemplos:

- Componentes;
- Organização interna;
- Estruturas de dados utilizadas;
- Forma de armazenamento do conhecimento.

**Pergunta:** *Como o sistema é construído?*

## Aspecto Funcional

Refere-se ao comportamento do sistema.

Exemplos:

- Objetivos;
- Funções executadas;
- Resultados produzidos.

**Pergunta:** *Para que o sistema serve?*

---

# Características que Definem um Comportamento Inteligente

## 1. Base de Conhecimento / Experiência

Um sistema inteligente deve ser capaz de armazenar conhecimento adquirido.

Esse conhecimento pode ser:

### Estruturado

Organizado segundo regras ou formatos definidos.

Exemplos:

- Bancos de dados;
- Regras lógicas;
- Ontologias;
- Sistemas especialistas.

### Não Estruturado

Informações sem organização rígida.

Exemplos:

- Textos;
- Imagens;
- Áudios;
- Vídeos.

### Tecnologias Relacionadas

- Prolog;
- Sistemas Multiagentes (SMA);
- Redes Neurais Artificiais (RNA).

---

## 2. Capacidade de Raciocínio (Deliberação)

Consiste na habilidade de utilizar o conhecimento armazenado para tomar decisões.

O sistema analisa informações e escolhe uma ação ou solução.

### Tecnologias Relacionadas

- Métodos de Busca;
- Prolog;
- Algoritmos Genéticos;
- Sistemas Multiagentes (SMA);
- Redes Neurais Artificiais (RNA).

### Raciocínio Dedutivo

Parte de regras gerais para chegar a conclusões específicas.

**Exemplo:**

- Todos os mamíferos possuem pulmões;
- Cachorros são mamíferos;
- Portanto, cachorros possuem pulmões.

**Fluxo:**

```text
Geral → Específico
```

### Raciocínio Indutivo

Parte de exemplos específicos para formular uma regra geral.

**Exemplo:**

- Cachorro A possui quatro patas;
- Cachorro B possui quatro patas;
- Cachorro C possui quatro patas;
- Logo, cachorros possuem quatro patas.

**Fluxo:**

```text
Específico → Geral
```

> O Aprendizado de Máquina é fortemente baseado em processos indutivos.

---

## 3. Reconhecimento de Padrões

Capacidade de identificar regularidades em dados.

### Exemplos

- Reconhecimento facial;
- Diagnóstico médico;
- Detecção de fraudes;
- Classificação de e-mails;
- Reconhecimento de voz.

### Tecnologias Relacionadas

- Aprendizado de Máquina (Machine Learning);
- Redes Neurais Artificiais (RNA);
- Deep Learning.

---

# Formas de Utilização da IA para Resolver Problemas

## Problemas de Diagnóstico

A IA analisa características observadas para determinar uma causa ou classificação.

### Exemplos

- Diagnóstico médico;
- Detecção de falhas em equipamentos;
- Classificação de documentos.

### Técnicas Comuns

- Reconhecimento de padrões;
- Classificação;
- Inferência.

---

## Problemas de Caminho ou Empacotamento

A IA busca uma sequência de ações que leve à solução.

### Exemplos

- Encontrar o menor caminho entre cidades;
- Resolver labirintos;
- Planejamento de rotas;
- Problema da mochila;
- Quebra-cabeças.

### Técnicas Comuns

- Busca;
- Planejamento;
- Otimização;
- Tentativa e erro guiada.

---

# Conceitos Fundamentais em Problemas de Busca

Grande parte das técnicas clássicas de IA modela problemas utilizando estados e transições.

---

## Estado

Representa uma situação possível do problema em determinado momento.

Um estado é composto pelos valores dos atributos relevantes do problema.

### Exemplo

**Problema do Labirinto**

```text
Posição atual = (3,4)
```

**Problema do Quebra-Cabeça**

```text
1 2 3
4 5 6
7 _ 8
```

---

## Regras de Transição

Definem como passar de um estado para outro.

Na implementação, geralmente correspondem às operações ou métodos disponíveis.

### Exemplo

No problema do labirinto:

- Mover para cima;
- Mover para baixo;
- Mover para esquerda;
- Mover para direita.

---

## Restrições

São condições que limitam as transições possíveis.

Normalmente implementadas por verificações lógicas.

### Exemplos

- Não atravessar paredes;
- Não sair do tabuleiro;
- Não realizar movimentos inválidos;
- Respeitar regras do problema.

### Exemplo em Código

```python
if movimento_valido:
    executar_movimento()
```

---

## Lista de Visitados

Estrutura utilizada para armazenar estados já explorados.

### Objetivos

- Evitar ciclos;
- Evitar processamento repetido;
- Melhorar desempenho da busca.

### Exemplo

```text
A → B → C → A
```

Sem uma lista de visitados, o algoritmo pode entrar em loop infinito.

---

## Função Objetivo

Define quando o problema foi resolvido.

É o critério de sucesso da busca.

### Exemplos

**Labirinto**

```text
Posição atual == saída
```

**Quebra-Cabeça**

```text
Estado atual == estado desejado
```

---

# Resumo Geral

Um sistema inteligente normalmente possui:

1. **Conhecimento** (Base de Conhecimento);
2. **Capacidade de raciocínio** (Deliberação);
3. **Reconhecimento de padrões** (Aprendizado);
4. **Representação de estados**;
5. **Regras de transição**;
6. **Restrições**;
7. **Controle de estados visitados**;
8. **Função objetivo para encontrar a solução**.

---

# Mapa Conceitual da IA Clássica

```text
                    Inteligência Artificial
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
  Conhecimento           Raciocínio           Reconhecimento
(Base de Dados)         (Deliberação)          de Padrões
        │                      │                      │
        ▼                      ▼                      ▼
   Estruturado          Busca e Inferência     Machine Learning
 ou Não Estruturado        Dedução/Indução      Redes Neurais

                               │
                               ▼
                     Resolução de Problemas
                               │
              ┌────────────────┴────────────────┐
              ▼                                 ▼
       Diagnóstico                      Caminho/Otimização
              │                                 │
              ▼                                 ▼
    Classificação e                  Busca por Soluções
 Reconhecimento de Padrões             e Planejamento
```

---

# Conceitos-Chave para Memorizar

| Conceito | Definição |
|-----------|------------|
| Estado | Situação atual do problema |
| Transição | Mudança de um estado para outro |
| Restrição | Regra que limita ações possíveis |
| Visitados | Estados já explorados |
| Objetivo | Estado desejado da solução |
| Dedução | Geral → Específico |
| Indução | Específico → Geral |
| Base de Conhecimento | Informações armazenadas pelo sistema |
| Reconhecimento de Padrões | Identificação de regularidades nos dados |
| Deliberação | Processo de tomada de decisão |
|

Esses conceitos formam a base para praticamente todas as técnicas clássicas de Inteligência Artificial estudadas posteriormente, como busca em grafos, sistemas especialistas, algoritmos genéticos, sistemas multiagentes e redes neurais artificiais.