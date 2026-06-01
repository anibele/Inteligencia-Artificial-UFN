# Aula 08 - Algoritmos Genéticos e Complexidade de Problemas

---

# Revisão dos Conceitos Fundamentais de IA

A Inteligência Artificial pode ser vista como a combinação de três componentes principais:

```text
            Inteligência Artificial
                     │
     ┌───────────────┼───────────────┐
     ▼               ▼               ▼
 Base de      Motor de Raciocínio  Aprendizado
 Conhecimento                     de Máquina
```

---

## 1. Base de Conhecimento

Responsável por armazenar informações sobre o domínio do problema.

Pode conter:

- Fatos;
- Regras;
- Experiências;
- Conhecimento especializado.

---

## 2. Motor de Raciocínio

Responsável por utilizar o conhecimento armazenado para resolver problemas.

O motor realiza inferências e toma decisões.

---

### Formas de Raciocínio

#### Dedução

Parte de informações gerais para chegar a conclusões específicas.

```text
Geral → Específico
```

Exemplo:

```text
Todo aluno possui matrícula.
João é aluno.
Logo, João possui matrícula.
```

---

#### Indução

Parte de exemplos específicos para construir uma regra geral.

```text
Específico → Geral
```

Exemplo:

```text
Aluno A estudou e passou.
Aluno B estudou e passou.
Aluno C estudou e passou.

Logo:
Estudar aumenta a chance de aprovação.
```

---

## 3. Aprendizado de Máquina

Responsável por identificar padrões através de exemplos.

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

# Prolog

O Prolog é uma linguagem baseada em lógica.

Seu funcionamento é baseado em dois componentes principais.

---

## Base de Conhecimento

A base de conhecimento pode conter:

### Fatos

Representam informações consideradas verdadeiras.

Exemplo:

```prolog
aluno(gustavo).
```

---

### Regras

Representam conhecimento derivado.

Exemplo:

```prolog
estudante(X) :-
    aluno(X).
```

Leitura:

```text
X é estudante se X for aluno.
```

---

## Aplicação do Motor de Inferência

O Prolog utiliza:

```text
Busca em Profundidade (DFS)
```

para encontrar soluções.

---

### Fluxo

```text
Pergunta
    ↓
Motor de Inferência
    ↓
Busca em Profundidade
    ↓
Resposta
```

---

# Técnicas de IA

De forma geral, qualquer técnica de IA envolve:

```text
Base de Conhecimento
          +
Motor de Raciocínio
          +
Aprendizado
```

---

## Exemplo

### Sistema Especialista

```text
Base:
    Regras médicas

Motor:
    Inferência lógica

Resultado:
    Diagnóstico
```

---

### Rede Neural

```text
Base:
    Dados de treinamento

Motor:
    Processamento da rede

Resultado:
    Reconhecimento de padrões
```

---

# Categorias de Problemas

Os problemas de IA normalmente são classificados em duas grandes categorias.

---

# 1. Problemas de Diagnóstico

Objetivo:

```text
Reconhecer padrões
```

---

## Características

- Possuem exemplos anteriores;
- Dependem de treinamento;
- Utilizam Machine Learning.

---

## Exemplos

- Diagnóstico médico;
- Reconhecimento facial;
- Reconhecimento de voz;
- Classificação de imagens;
- Detecção de spam.

---

## Fluxo

```text
Entrada
    ↓
Reconhecimento
    ↓
Classificação
```

---

# 2. Problemas de Gerar e Testar (Empacotamento)

Também chamados de:

```text
Problemas de Busca
```

---

## Objetivo

Encontrar uma sequência de passos até a solução.

---

## Fluxo

```text
Gerar Solução
      ↓
Testar
      ↓
Funciona?
      ↓
Sim → Solução

Não → Gerar novamente
```

---

## Exemplos

- Labirintos;
- Sudoku;
- Torres de Hanói;
- Problema das Jarras;
- Planejamento de rotas;
- Problema da Mochila.

---

# Complexidade dos Problemas

A complexidade representa o esforço necessário para resolver um problema.

---

## Quanto maior a complexidade:

```text
Mais memória
+
Mais processamento
+
Mais tempo
```

---

# Fatores que Influenciam a Complexidade

---

## 1. Restrições

As restrições reduzem a quantidade de soluções possíveis.

---

### Sem Restrições

```text
Muitas possibilidades
```

---

### Com Restrições

```text
Menos possibilidades
```

---

## Exemplo

Sudoku:

```text
Número repetido na linha
```

↓

```text
Estado inválido
```

↓

```text
Não precisa ser explorado
```

---

## Benefício

As restrições diminuem o espaço de busca.

---

# 2. Heurísticas

As heurísticas fornecem dicas para o algoritmo.

---

## Objetivo

Direcionar a busca para regiões mais promissoras.

---

## Exemplo

Labirinto:

Sem heurística:

```text
Explorar tudo.
```

Com heurística:

```text
Explorar primeiro
os caminhos mais próximos da saída.
```

---

## Benefício

Redução significativa do número de estados explorados.

---

# Algoritmos Genéticos

Os Algoritmos Genéticos (AG) são métodos de busca heurística inspirados na evolução biológica.

---

## Ideia Principal

Em vez de testar uma única solução por vez, o algoritmo trabalha com uma população de soluções.

---

## Conceito

Pode ser visto como um:

```text
Método Heurístico Turbinado
```

Pois utiliza mecanismos inspirados na seleção natural para encontrar soluções melhores.

---

# Inspiração Biológica

Baseado em:

- Evolução;
- Seleção Natural;
- Reprodução;
- Mutação.

---

# Componentes Principais

---

## Indivíduo

Representa uma solução possível.

---

## População

Conjunto de indivíduos.

```text
Indivíduo 1
Indivíduo 2
Indivíduo 3
...
```

---

## Fitness (Aptidão)

Mede a qualidade da solução.

Quanto maior o fitness:

```text
Melhor a solução
```

---

## Seleção

Escolhe os melhores indivíduos.

---

## Cruzamento (Crossover)

Combina características de duas soluções.

---

## Mutação

Introduz pequenas alterações aleatórias.

---

# Fluxo do Algoritmo Genético

```text
População Inicial
        ↓
Avaliação (Fitness)
        ↓
Seleção
        ↓
Cruzamento
        ↓
Mutação
        ↓
Nova Geração
        ↓
Repetir Processo
```

---

# Vantagens dos Algoritmos Genéticos

- Exploram grandes espaços de busca;
- Encontram boas soluções rapidamente;
- Adaptam-se a problemas complexos;
- Funcionam bem em otimização.

---

# Desvantagens

- Não garantem solução ótima;
- Dependem da função fitness;
- Podem exigir muitas gerações.

---

# Restrições (Constraints)

As restrições definem quais soluções são aceitáveis.

---

# Hard Constraints

São restrições obrigatórias.

Se forem violadas:

```text
Solução inválida
```

---

## Exemplo

Sudoku:

```text
Não repetir números na linha.
```

Se repetir:

```text
Tabuleiro inválido.
```

---

## Característica

```text
Devem ser sempre satisfeitas.
```

---

# Soft Constraints

São restrições desejáveis, mas não obrigatórias.

Se forem violadas:

```text
A solução continua válida,
mas perde qualidade.
```

---

## Exemplo

Problema de horários:

```text
Professor prefere aula pela manhã.
```

Se receber aula à tarde:

```text
Solução ainda é válida.
```

Porém:

```text
Menos desejável.
```

---

## Característica

```text
Afetam a qualidade da solução.
```

Mas não a invalidam.

---

# Comparação: Hard x Soft Constraints

| Tipo | Obrigatória? | Violação |
|--------|-------------|-----------|
| Hard Constraint | Sim | Solução inválida |
| Soft Constraint | Não | Solução pior, mas válida |

---

# Exemplo Aplicado

## Escala de Horários

### Hard Constraints

- Professor não pode estar em duas salas ao mesmo tempo;
- Sala não pode ter duas turmas simultaneamente.

Violação:

```text
Solução impossível.
```

---

### Soft Constraints

- Evitar aulas no último horário;
- Preferir dias consecutivos.

Violação:

```text
Solução continua funcionando.
```

---

# Resumo Visual

```text
                   IA
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼
 Base         Motor de         Aprendizado
Conhecimento  Raciocínio

                    │
        ┌───────────┼───────────┐
        ▼                       ▼
     Dedução                Indução

                    │
        ┌───────────┼───────────┐
        ▼                       ▼
      Busca               Diagnóstico

                    │
                    ▼
          Algoritmos Genéticos
          (Busca Heurística)
```

---

# Conceitos-Chave para Memorizar

| Conceito | Definição |
|-----------|------------|
| Base de Conhecimento | Armazena fatos e regras |
| Motor de Raciocínio | Resolve problemas usando inferência |
| Dedução | Geral → Específico |
| Indução | Específico → Geral |
| Diagnóstico | Reconhecimento de padrões |
| Gerar e Testar | Busca por soluções |
| Heurística | Informação que orienta a busca |
| Complexidade | Esforço necessário para resolver um problema |
| Algoritmo Genético | Busca inspirada na evolução biológica |
| Fitness | Qualidade da solução |
| População | Conjunto de soluções |
| Hard Constraint | Restrição obrigatória |
| Soft Constraint | Restrição desejável |
|

---

# Resumo Geral

Nesta aula foi realizada uma revisão dos conceitos fundamentais de IA e introduzido o conceito de **Algoritmos Genéticos**, considerados uma forma avançada de busca heurística.

Também foi apresentado o conceito de **restrições (constraints)**, divididas em:

### Hard Constraints

```text
Obrigatórias.
Violação = solução inválida.
```

### Soft Constraints

```text
Desejáveis.
Violação = solução pior,
mas ainda válida.
```

Esses conceitos são fundamentais para problemas de otimização, planejamento, escalonamento e algoritmos genéticos, que serão estudados nas próximas aulas.