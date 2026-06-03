# Almoxarifado Inteligente com Jason

Projeto desenvolvido utilizando a linguagem de programação orientada a agentes inteligentes: **Jason** para a disciplina de **Inteligência Artificial**.

O sistema simula um almoxarifado onde dois robôs trabalham de forma autônoma para armazenar peças de diferentes tamanhos. Os agentes percebem o ambiente, tomam decisões com base em suas crenças e colaboram quando necessário.

---

# Objetivo

Simular um cenário de armazenamento de peças em um almoxarifado utilizando agentes inteligentes.

As peças podem possuir três tamanhos:

* Pequena (`peq`)
* Média (`med`)
* Grande (`grd`)

Cada agente possui responsabilidades específicas e uma quantidade limitada de viagens que pode realizar.

---

# Agentes

## r1 - Robô de Peças Pequenas

O agente `r1` é responsável por armazenar peças pequenas.

### Responsabilidades

* Detectar peças pequenas.
* Guardar peças pequenas.
* Controlar sua quantidade de viagens disponíveis.
* Solicitar ajuda ao agente `r2` quando uma peça grande é detectada.

### Crenças iniciais

```asl
viagens(10).
```

O agente inicia com 10 viagens disponíveis.

---

## r2 - Robô de Peças Médias

O agente `r2` é responsável por armazenar peças médias e auxiliar no armazenamento de peças grandes.

### Responsabilidades

* Detectar peças médias.
* Guardar peças médias.
* Receber pedidos de ajuda enviados por `r1`.
* Guardar peças grandes quando possui viagens disponíveis.
* Controlar sua quantidade de viagens restantes.

### Crenças iniciais

```asl
viagens(15).
```

O agente inicia com 15 viagens disponíveis.

---

# Cooperação entre Agentes

Quando uma peça grande aparece no ambiente:

1. O agente `r1` detecta a peça.
2. O agente `r1` envia uma mensagem para o agente `r2`.
3. O agente `r2` verifica se ainda possui viagens disponíveis.
4. Caso possua viagens, a peça grande é armazenada.
5. Caso não possua viagens, o agente informa que não pode ajudar.

Exemplo de comunicação:

```asl
.send(r2, achieve, vamosGuardar(grd))
```

---

# Funcionamento do Ambiente

O ambiente é implementado na classe:

```java
Env.java
```

Sua função é simular o almoxarifado.

## Responsabilidades do ambiente

### Sorteio de peças

O ambiente sorteia aleatoriamente uma das seguintes percepções:

```text
peca(peq)
peca(med)
peca(grd)
```

### Disponibilização da peça

A peça sorteada é adicionada ao ambiente como uma percepção para os agentes.

### Processamento das ações

Quando um agente executa uma ação:

```asl
guardar(peq)
guardar(med)
guardar(grd)
```

o ambiente:

1. Registra a ação no console.
2. Remove a peça atual do ambiente.
3. Aguarda 4 segundos.
4. Sorteia uma nova peça.
5. Disponibiliza a nova peça aos agentes.

---

# Tecnologias Utilizadas

* Java
* Jason
* VS Code
* Bash

---

# Como Executar

## Pré-requisitos

* Java instalado e configurado.
* Jason instalado e configurado no sistema.
* VS Code (opcional).

---

## Executando o projeto

Abra um terminal na pasta raiz do projeto e execute:

```bash
jason almoxarifado.mas2j
```

---

# Exemplo de Saída

```text
[r1] guardo peças pequenas
[r2] guardo peças médias

[r1] percebi uma peça grande e vou pedir ajuda para o r2

[r2] r1 me chamou para guardar a peça grande. Viagens restantes r2: 3

[Env] Os agentes r1 e r2 estão guardando a peça grande!

[Env] Uma nova peça está sendo colocada no almoxarifado...
```

---

# Conceitos de Sistemas Multiagentes Utilizados

Este projeto demonstra conceitos fundamentais de Sistemas Multiagentes:

* Agentes autônomos
* Percepção do ambiente
* Crenças
* Planos
* Comunicação entre agentes
* Cooperação
* Tomada de decisão baseada em contexto
* Interação agente-ambiente

---

# Atividade

Projeto desenvolvido como atividade acadêmica da disciplina de Inteligência Artificial - Sistemas de informação - UFN - 2026.
