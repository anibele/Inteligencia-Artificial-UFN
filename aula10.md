# Aula 10 - Redes Neurais Artificiais e Aprendizado de Máquina

---

# Introdução

Até este ponto da disciplina foram estudadas técnicas de IA voltadas principalmente para:

- Representação do conhecimento;
- Motores de raciocínio;
- Métodos de busca;
- Sistemas Multiagentes.

Nesta aula é introduzida uma das áreas mais importantes da Inteligência Artificial moderna:

```text
Redes Neurais Artificiais (RNA)
```

As Redes Neurais são a base de grande parte dos sistemas atuais de:

- Reconhecimento facial;
- Reconhecimento de voz;
- Tradução automática;
- Visão computacional;
- Veículos autônomos;
- Inteligência Artificial Generativa.

---

# Sistemas de Comportamento Inteligente

Um sistema inteligente normalmente é construído utilizando técnicas de IA divididas em três pilares.

```text
Sistema Inteligente
        │
 ┌──────┼──────┐
 ▼      ▼      ▼
Base   Motor  Aprendizado
```

---

## 1. Base de Conhecimento

Responsável por armazenar informações.

### Tecnologias estudadas

- Prolog;
- Sistemas Multiagentes (SMA).

---

## Função

```text
Armazenar conhecimento
sobre o problema.
```

---

## 2. Motor de Raciocínio

Responsável por tomar decisões.

### Tecnologias estudadas

- Métodos de Busca;
- Sistemas Multiagentes.

---

## Função

```text
Utilizar o conhecimento
para resolver problemas.
```

---

## 3. Aprendizado de Máquina

Responsável por aprender padrões a partir de dados.

### Tecnologias estudadas

- Redes Neurais;
- Sistemas Multiagentes adaptativos.

---

## Função

```text
Aprender com exemplos.
```

---

# Redes Neurais Artificiais (RNA)

---

## O que são?

Redes Neurais Artificiais são modelos computacionais inspirados no funcionamento do cérebro humano.

---

## Objetivo

Aprender padrões existentes nos dados para realizar previsões ou classificações.

---

## Inspiração Biológica

No cérebro humano:

```text
Neurônios
      ↓
Conexões
      ↓
Processamento
      ↓
Aprendizado
```

---

## Na Computação

```text
Neurônios Artificiais
         ↓
Conexões
         ↓
Processamento
         ↓
Aprendizado
```

---

# Características das Redes Neurais

---

## 1. Inspiradas no Cérebro Humano

Buscam reproduzir o funcionamento simplificado dos neurônios biológicos.

---

## 2. Formadas por Neurônios Artificiais

Cada neurônio recebe informações, realiza cálculos e produz uma saída.

---

## 3. Interconectadas

Os neurônios trabalham em conjunto.

```text
Entrada
   ↓
Neurônios
   ↓
Saída
```

---

## 4. Capacidade de Aprender

Não precisam receber regras prontas.

Aprendem observando exemplos.

---

## 5. Capacidade de Generalização

Após aprender com exemplos conhecidos, conseguem responder corretamente a novos exemplos nunca vistos.

---

# Estrutura de uma Rede Neural

Uma rede neural normalmente possui três tipos de camadas.

```text
Camada de Entrada
         ↓
Camada Oculta
         ↓
Camada de Saída
```

---

## Camada de Entrada

Recebe os dados.

Exemplo:

```text
Imagem
Texto
Áudio
Sensores
```

---

## Camadas Ocultas

Realizam o processamento interno.

São responsáveis pela descoberta dos padrões.

---

## Camada de Saída

Produz o resultado final.

Exemplo:

```text
Gato
Cachorro
Pessoa
```

---

# Treinamento de um Sistema Computadorizado

Para que uma rede neural aprenda, é necessário realizar treinamento.

---

# Conjunto de Dados

O treinamento utiliza exemplos previamente conhecidos.

---

## Amostras Positivas

Representam exemplos corretos do padrão desejado.

### Exemplo

Treinamento para reconhecer gatos:

```text
Imagem de gato
Imagem de gato
Imagem de gato
```

---

## Amostras Negativas

Representam exemplos que não pertencem ao padrão.

### Exemplo

```text
Imagem de cachorro
Imagem de carro
Imagem de pessoa
```

---

# Etapa 1 - Organização das Amostras

Primeira fase do treinamento.

---

## Objetivo

Carregar as amostras na memória.

```text
Disco
   ↓
RAM
   ↓
Processamento
```

---

## O que acontece?

O sistema procura identificar padrões repetidos.

---

### Exemplo

Reconhecimento de gatos:

```text
Orelhas
Olhos
Bigodes
Formato do rosto
```

---

## Resultado

Construção de um modelo interno.

---

# Aprendizado Supervisionado

---

## Conceito

Os exemplos possuem respostas conhecidas.

```text
Imagem
     ↓
"Gato"
```

```text
Imagem
     ↓
"Cachorro"
```

---

## Características

### Vantagens

- Maior precisão;
- Maior acurácia;
- Melhor controle do treinamento.

---

### Desvantagens

- Maior processamento;
- Maior tempo de treinamento;
- Necessidade de dados rotulados.

---

## Resumo

```text
+ Processamento
+ Tempo
+ Acurácia
```

---

# Aprendizado Não Supervisionado

---

## Conceito

Os dados não possuem respostas conhecidas.

O algoritmo tenta descobrir padrões sozinho.

---

## Exemplo

Agrupar clientes por comportamento de compra.

---

## Características

### Vantagens

- Menos trabalho de preparação;
- Não exige rótulos.

---

### Desvantagens

- Menor precisão;
- Menor acurácia;
- Resultados menos controlados.

---

## Resumo

```text
++ Processamento
++ Tempo
- Acurácia
```

---

# Etapa 2 - Validação

Após o treinamento, ocorre a validação.

---

## Objetivo

Comparar exemplos conhecidos com novos exemplos.

---

## Processo

```text
Amostras Positivas
        ↓
Modelo Treinado
        ↓
Comparação
        ↓
Validação
```

---

## O que é avaliado?

A capacidade da rede de reconhecer corretamente os padrões.

---

# Exemplo

Treinamento:

```text
100 imagens de gatos
```

Validação:

```text
Novas imagens
```

Objetivo:

```text
Verificar se a rede
continua reconhecendo gatos.
```

---

# Etapa 3 - Testes

Última fase do processo.

---

## Objetivo

Medir o desempenho da rede neural.

---

## Processo

Uma parte das amostras é separada exclusivamente para testes.

Essas amostras não participaram do treinamento.

---

## Exemplo

```text
1000 imagens
```

Distribuição:

```text
70% Treinamento

15% Validação

15% Testes
```

---

# Medindo a Taxa de Acerto

A principal métrica utilizada é a acurácia.

---

## Fórmula

:contentReference[oaicite:0]{index=0}

---

## Exemplo

```text
100 testes realizados
```

```text
92 acertos
```

Resultado:

```text
92% de acurácia
```

---

# Fluxo Completo de Treinamento

```text
Amostras Positivas
          +
Amostras Negativas
          ↓
Organização dos Dados
          ↓
Treinamento
          ↓
Identificação de Padrões
          ↓
Validação
          ↓
Testes
          ↓
Acurácia Final
```

---

# Aplicações das Redes Neurais

---

## Reconhecimento Facial

```text
Pessoa A
Pessoa B
Pessoa C
```

---

## Reconhecimento de Voz

```text
Transformar fala em texto
```

---

## Diagnóstico Médico

```text
Exames
    ↓
Classificação
```

---

## Visão Computacional

```text
Reconhecimento de objetos
```

---

## Inteligência Artificial Generativa

```text
Texto
Imagem
Áudio
Vídeo
```

---

# Comparação dos Métodos de IA Estudados

| Técnica | Objetivo Principal |
|----------|-------------------|
| Prolog | Representação de conhecimento |
| Métodos de Busca | Resolver problemas através de estados |
| Sistemas Multiagentes | Cooperação entre agentes |
| Redes Neurais | Reconhecimento de padrões |
| Machine Learning | Aprendizado através de exemplos |

---

# Resumo Visual

```text
             Inteligência Artificial
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
 Base de          Motor de         Aprendizado
Conhecimento      Raciocínio        de Máquina
      │                │                │
      ▼                ▼                ▼
   Prolog      Métodos de Busca   Redes Neurais
      │                │                │
      ▼                ▼                ▼
 Conhecimento      Soluções       Reconhecimento
                                  de Padrões
```

---

# Conceitos-Chave para Memorizar

| Conceito | Definição |
|-----------|------------|
| Rede Neural Artificial | Modelo inspirado no cérebro humano |
| Neurônio Artificial | Unidade básica de processamento |
| Aprendizado Supervisionado | Dados possuem respostas conhecidas |
| Aprendizado Não Supervisionado | Dados não possuem respostas conhecidas |
| Amostra Positiva | Exemplo do padrão desejado |
| Amostra Negativa | Exemplo fora do padrão |
| Treinamento | Processo de aprendizado |
| Validação | Verificação do modelo |
| Testes | Avaliação final do desempenho |
| Acurácia | Percentual de acertos |
| Generalização | Capacidade de responder a novos exemplos |
| Machine Learning | Aprendizado por meio de dados |
|

---

# Resumo Geral

Nesta aula foi introduzido o conceito de **Redes Neurais Artificiais (RNA)**, uma das principais técnicas de **Aprendizado de Máquina**.

As redes neurais são inspiradas no cérebro humano e possuem a capacidade de aprender padrões através de exemplos, utilizando amostras positivas e negativas durante o treinamento.

O processo de construção de uma rede neural envolve três etapas principais:

```text
Treinamento
      ↓
Validação
      ↓
Testes
```

Ao final, a qualidade do modelo é medida através de métricas como a **acurácia**, indicando o percentual de acertos obtidos pelo sistema em dados que ele nunca viu anteriormente.