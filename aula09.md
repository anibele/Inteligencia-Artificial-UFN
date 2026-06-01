# Aula 09 - Sistemas Multiagentes com Jason

---

# Introdução

Nesta aula é apresentada uma das principais plataformas para desenvolvimento de Sistemas Multiagentes (SMA):

```text
Jason
```

O foco deixa de ser apenas o conceito de agente e passa a ser sua implementação prática.

---

# Sistemas Multiagentes (SMA)

Um Sistema Multiagente é composto por vários agentes inteligentes cooperando para atingir objetivos.

---

## O Foco do SMA

O elemento principal de um SMA é o:

```text
Agente
```

---

# O que é um Agente?

Um agente é uma entidade de software ou hardware capaz de:

- Perceber o ambiente;
- Tomar decisões;
- Executar ações;
- Comunicar-se com outros agentes;
- Adaptar-se às mudanças.

---

## Definição

```text
Agente =
Entidade autônoma
+
Proativa
+
Flexível
+
Capaz de comunicação
```

---

# Características Fundamentais dos Agentes

---

## 1. Autonomia

O agente executa suas atividades sem depender de intervenção constante.

### Exemplo

```text
Sensor detecta movimento
        ↓
Agente reage automaticamente
```

---

## 2. Proatividade

O agente toma iniciativa.

Não espera receber comandos o tempo todo.

### Exemplo

```text
Temperatura elevada
        ↓
Agente liga ventilação
```

---

## 3. Flexibilidade

Capacidade de adaptar-se a situações inesperadas.

### Exemplo

```java
try{
    executarAcao();
}
catch(Exception e){
    adaptarComportamento();
}
```

Caso ocorra erro:

```text
Agente tenta outra estratégia.
```

---

## 4. Comunicação

Agentes podem trocar mensagens entre si.

```text
Agente A
    ↔
Agente B
```

---

# Engine (Motor do Agente)

O comportamento inteligente do agente é sustentado por alguns componentes fundamentais.

---

## Thread

Permite que o agente execute continuamente.

```java
while(true){
    perceber();
    decidir();
    agir();
}
```

---

## Try-Catch

Permite tratamento de falhas.

```java
try{
    executar();
}
catch(Exception e){
    recuperar();
}
```

---

## Sobrecarga (Overloading)

Possibilita diferentes formas de executar uma ação.

Exemplo:

```java
mover();
mover(int velocidade);
mover(int velocidade,
      String direcao);
```

---

## Comunicação em Rede

Os agentes podem comunicar-se através de protocolos de rede.

---

### Componentes

```text
IP
+
Porta
+
Protocolo
+
Socket
```

---

### Exemplo

```text
192.168.0.10
```

Porta:

```text
8080
```

Protocolo:

```text
TCP
```

---

# Jason

Jason é uma plataforma para desenvolvimento de Sistemas Multiagentes.

Foi criada para implementar agentes baseados na arquitetura BDI.

---

# Arquitetura BDI

BDI significa:

```text
Belief
Desire
Intention
```

---

## Beliefs (Crenças)

Representam o que o agente sabe.

Exemplo:

```text
temperatura(30).
porta(aberta).
```

---

## Desires (Desejos)

Representam objetivos.

Exemplo:

```text
manter_temperatura_agradavel.
```

---

## Intentions (Intenções)

Representam as ações escolhidas.

Exemplo:

```text
ligar_ar_condicionado.
```

---

# Organização de um Projeto Jason

Um projeto Jason normalmente é composto por:

```text
.mas2j
.agentes (.asl)
.environment (Java)
```

---

# Arquivo .mas2j

É o arquivo principal do projeto.

Define a configuração do sistema multiagente.

---

## Responsabilidades

1. Definir o ambiente;
2. Definir os agentes;
3. Definir a arquitetura.

---

## Estrutura Geral

```text
Projeto
    │
    ├── Environment
    ├── Agente 1
    ├── Agente 2
    └── Arquitetura
```

---

# Arquitetura Centralizada

Na arquitetura centralizada:

```text
            Ambiente
                │
    ┌───────────┼───────────┐
    ▼           ▼           ▼
 Agente1    Agente2    Agente3
```

Todos os agentes interagem através do mesmo ambiente.

---

## Vantagens

- Simplicidade;
- Fácil implementação;
- Fácil monitoramento.

---

## Desvantagens

- Ponto único de falha;
- Menor escalabilidade.

---

# Arquivos ASL

ASL significa:

```text
AgentSpeak Language
```

É a linguagem utilizada para programar os agentes no Jason.

---

## Função

Descrever:

- Crenças;
- Objetivos;
- Planos;
- Regras de comportamento.

---

## Exemplo Conceitual

```asl
temperatura(30).

+!controlar_temperatura
    <- ligar_ar.
```

Leitura:

```text
Se o objetivo for controlar a temperatura,
então ligar o ar-condicionado.
```

---

# Exemplo com Dois Agentes

```text
hw(agente1)
hw(agente2)
```

Cada agente possui:

- Crenças próprias;
- Objetivos próprios;
- Planos próprios.

---

# Ambiente em Java

O ambiente representa o mundo onde os agentes atuam.

---

## Responsabilidades

- Receber ações dos agentes;
- Atualizar o estado do mundo;
- Enviar percepções aos agentes.

---

# Classe Environment

No Jason, o ambiente normalmente herda da classe:

```java
Environment
```

---

# Método init()

Executado quando o sistema inicia.

Responsável pela configuração inicial.

---

## Exemplo

```java
public void init(String[] args){
    ...
}
```

---

# Função

```text
Criar objetos
Inicializar variáveis
Configurar cenário
```

---

# Método addPercept()

Adiciona uma percepção ao agente.

---

## Exemplo

```java
addPercept(
    Literal.parseLiteral(
        "temperatura(30)"
    )
);
```

---

## Resultado

O agente passa a acreditar que:

```text
temperatura(30)
```

é verdadeira.

---

# Método removePercept()

Remove uma percepção existente.

---

## Exemplo

```java
removePercept(
    Literal.parseLiteral(
        "temperatura(30)"
    )
);
```

---

## Resultado

O agente deixa de possuir essa crença.

---

# Método executeAction()

Executa uma ação enviada por um agente.

---

## Fluxo

```text
Agente
    ↓
Executa ação
    ↓
Environment
    ↓
Atualiza mundo
```

---

## Exemplo

```java
public boolean executeAction(
    String ag,
    Structure action
)
{
    ...
}
```

---

# Fluxo Geral de Execução

```text
Agente percebe ambiente
           ↓
      addPercept()
           ↓
      Atualiza crenças
           ↓
      Decide ação
           ↓
      executeAction()
           ↓
      Ambiente reage
           ↓
      Nova percepção
```

---

# Estrutura Completa de um Projeto Jason

```text
Projeto
│
├── sistema.mas2j
│
├── agente1.asl
│
├── agente2.asl
│
└── Environment.java
```

---

# Resumo Visual

```text
                   Jason
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
   .mas2j          .asl            Java
 Configuração     Agentes      Environment
                      │
                      ▼
             Beliefs / Desires
                / Intentions
```

---

# Comparação: Prolog x Jason

| Característica | Prolog | Jason |
|----------------|---------|---------|
| Paradigma | Lógico | Multiagente |
| Baseado em fatos | Sim | Sim |
| Baseado em regras | Sim | Sim |
| Motor dedutivo | Sim | Sim |
| Comunicação entre agentes | Não | Sim |
| Ambiente dinâmico | Limitado | Sim |
| Agentes autônomos | Não | Sim |

---

# Conceitos-Chave para Memorizar

| Conceito | Definição |
|-----------|------------|
| Agente | Entidade autônoma capaz de perceber e agir |
| SMA | Sistema Multiagente |
| Jason | Plataforma para desenvolvimento de SMA |
| BDI | Beliefs, Desires e Intentions |
| Belief | Conhecimento do agente |
| Desire | Objetivo do agente |
| Intention | Plano escolhido |
| ASL | Linguagem AgentSpeak |
| .mas2j | Arquivo de configuração do projeto |
| Environment | Ambiente compartilhado pelos agentes |
| init() | Inicialização do ambiente |
| addPercept() | Adiciona percepção |
| removePercept() | Remove percepção |
| executeAction() | Executa ação do agente |
| Socket | Canal de comunicação em rede |
|

---

# Resumo Geral

Nesta aula foi apresentada a plataforma **Jason**, utilizada para implementação de **Sistemas Multiagentes (SMA)**.

Foi estudada a estrutura de um projeto Jason:

```text
.mas2j
+
Agentes (.asl)
+
Environment (Java)
```

Além disso, foram apresentados os conceitos de:

- Agentes autônomos;
- Comunicação entre agentes;
- Arquitetura BDI;
- Percepções;
- Ações;
- Ambiente compartilhado.

Esses conceitos permitem desenvolver sistemas distribuídos compostos por múltiplos agentes inteligentes capazes de cooperar para resolver problemas complexos.