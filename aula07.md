# Aula 07 - Sistemas Multiagentes (SMA) e Conceito de Agentes

---

# Introdução

Nesta aula é apresentada a diferença entre um **Objeto**, da Teoria da Orientação a Objetos (OO), e um **Agente**, utilizado na Teoria de Sistemas Multiagentes (SMA).

Embora ambos possuam dados e comportamentos, os agentes possuem características adicionais que lhes permitem agir de forma mais inteligente e independente.

---

# Objeto x Agente

## Objeto (Orientação a Objetos)

Um objeto é uma entidade que representa algo do mundo real.

Ele é composto por:

```text
Objeto
   │
   ├── Propriedades (Atributos)
   └── Serviços (Métodos)
```

---

## Estrutura de um Objeto

### Propriedades (Atributos)

Representam as características do objeto.

Exemplo:

```java
class Pessoa{
    String nome;
    int idade;
}
```

Neste exemplo:

```text
nome
idade
```

são atributos do objeto.

---

### Serviços (Métodos)

Representam as ações que o objeto pode executar.

Exemplo:

```java
public void falar(){
    ...
}
```

```java
private void calcular(){
    ...
}
```

---

## Métodos Públicos e Privados

### Método Público

Pode ser acessado por outros objetos.

```java
public void ligar()
```

---

### Método Privado

Só pode ser utilizado internamente pela própria classe.

```java
private void validar()
```

---

## Execução dos Métodos

Uma característica importante dos objetos é:

```text
Métodos só executam quando são invocados.
```

Exemplo:

```java
Pessoa p = new Pessoa();

p.falar();
```

Sem a chamada:

```java
p.falar();
```

o método nunca será executado.

---

## Invocação Estática

No paradigma tradicional orientado a objetos:

```text
Objeto espera ser chamado.
```

Ou seja:

```text
Não possui iniciativa própria.
```

---

# Agente (Sistemas Multiagentes)

Um agente é uma entidade computacional capaz de perceber o ambiente e agir sobre ele para atingir objetivos.

Diferentemente dos objetos, agentes possuem autonomia e iniciativa.

---

## Estrutura de um Agente

```text
Agente
   │
   ├── Propriedades (Fatos)
   ├── Serviços (Regras)
   └── Características Inteligentes
```

---

## Propriedades (Fatos)

Correspondem ao conhecimento que o agente possui.

Exemplo:

```text
Temperatura = 30°C
Sala = Ocupada
Luz = Ligada
```

Esses fatos representam o estado atual conhecido pelo agente.

---

## Serviços (Regras)

As ações dos agentes normalmente são implementadas através de regras.

Exemplo:

```text
SE temperatura > 28
ENTÃO ligar ar-condicionado
```

---

## Diferença para Métodos

Em objetos:

```text
Método executa quando chamado.
```

Em agentes:

```text
Regra pode executar automaticamente.
```

---

# Agentes e Threads

Uma característica importante dos agentes é que eles normalmente executam dentro de uma thread própria.

```text
Thread = fluxo independente de execução
```

---

## Objeto

```text
Objeto
   ↓
Espera chamada
```

---

## Agente

```text
Agente
   ↓
Executa continuamente
   ↓
Observa ambiente
   ↓
Toma decisões
```

---

# Características de um Agente

Um agente inteligente normalmente apresenta quatro características principais.

---

# 1. Autonomia

Capacidade de agir sem intervenção humana direta.

---

## Como é implementada?

Normalmente através de:

```java
Thread
```

ou

```java
Runnable
```

---

## Exemplo

```java
while(true){
    observarAmbiente();
    decidir();
    agir();
}
```

O agente continua funcionando mesmo sem receber chamadas externas.

---

# 2. Proatividade (Iniciativa)

Capacidade de tomar iniciativa.

---

## Objeto

```text
Espera ser chamado.
```

---

## Agente

```text
Percebe situação
       ↓
Decide agir
       ↓
Executa ação
```

---

## Exemplo

Sistema de monitoramento:

```text
Temperatura aumentou
       ↓
Agente detecta
       ↓
Liga ventilação automaticamente
```

---

# 3. Adaptação (Flexibilidade)

Capacidade de reagir a mudanças inesperadas.

O agente tenta continuar funcionando mesmo quando algo dá errado.

---

## Implementação Comum

Tratamento de exceções.

```java
try{
    executarAcao();
}
catch(Exception e){
    adaptarComportamento();
}
```

---

## Exemplo

```text
Servidor indisponível
       ↓
Agente detecta falha
       ↓
Tenta servidor alternativo
```

---

# 4. Habilidade Social (Comunicação)

Capacidade de interagir com outros agentes.

---

## Comunicação Entre Agentes

```text
Agente A
     ↔
Agente B
```

Os agentes podem:

- Trocar informações;
- Solicitar serviços;
- Cooperar;
- Negociar;
- Compartilhar conhecimento.

---

## Exemplo

```text
Agente Vendas
      ↓
Solicita estoque
      ↓
Agente Estoque
```

---

# Sistemas Multiagentes (SMA)

Um Sistema Multiagente é formado por vários agentes trabalhando juntos.

---

## Estrutura Geral

```text
      Agente A
          │
          │
          ▼
      Agente B
          │
          │
          ▼
      Agente C
```

Todos colaboram para resolver um problema maior.

---

## Aplicações

- Robótica;
- Jogos;
- Sistemas distribuídos;
- Comércio eletrônico;
- Automação industrial;
- Internet das Coisas (IoT).

---

# Comunicação em Sistemas Multiagentes

A comunicação geralmente utiliza conceitos de redes de computadores.

---

# Modelo TCP/IP

Os agentes podem trocar mensagens através da rede.

Para isso normalmente utilizam:

```text
IP
+
Porta
+
Protocolo
```

---

## Endereço IP

Identifica o computador na rede.

Exemplo:

```text
192.168.0.10
```

---

## Porta Lógica

Identifica o processo ou serviço.

Exemplo:

```text
8080
```

---

## Protocolo de Transporte

Responsável pela transmissão.

Exemplos:

```text
TCP
UDP
```

---

# Socket

O mecanismo mais comum de comunicação entre agentes é o socket.

---

## Conceito

Um socket representa um canal de comunicação entre dois processos.

---

## Estrutura

```text
Agente A
(IP + Porta)
       │
       │ Socket
       │
Agente B
(IP + Porta)
```

---

## Exemplo

```java
Socket socket =
    new Socket(
        "192.168.0.10",
        8080
    );
```

---

# Comparação: Objeto x Agente

| Característica | Objeto | Agente |
|----------------|---------|---------|
| Possui atributos | Sim | Sim |
| Possui comportamento | Sim | Sim |
| Executa sozinho | Não | Sim |
| Possui autonomia | Não | Sim |
| Possui iniciativa | Não | Sim |
| Comunica-se com outros | Normalmente não | Sim |
| Executa continuamente | Não | Sim |
| Utiliza threads | Opcional | Frequentemente |
| Toma decisões | Não | Sim |

---

# Exemplo Visual

## Objeto

```text
        Objeto
           │
    ┌──────┴──────┐
    ▼             ▼
Atributos      Métodos

Espera ser chamado
```

---

## Agente

```text
         Agente
            │
    ┌───────┼────────┐
    ▼       ▼        ▼
 Fatos   Regras   Thread
                    │
                    ▼
             Observa Ambiente
                    │
                    ▼
               Decide
                    │
                    ▼
                 Atua
```

---

# Conceitos-Chave para Memorizar

| Conceito | Definição |
|-----------|------------|
| Objeto | Entidade da orientação a objetos |
| Atributo | Característica do objeto |
| Método | Ação executada pelo objeto |
| Agente | Entidade autônoma capaz de agir |
| Fato | Informação conhecida pelo agente |
| Regra | Comportamento do agente |
| Autonomia | Capacidade de agir sozinho |
| Proatividade | Capacidade de tomar iniciativa |
| Adaptação | Capacidade de reagir a mudanças |
| Habilidade Social | Comunicação entre agentes |
| Thread | Fluxo independente de execução |
| Socket | Canal de comunicação entre processos |
| SMA | Sistema Multiagente |
|

---

# Resumo Geral

Nesta aula foi apresentada a principal diferença entre **Objetos** e **Agentes**.

### Objeto

```text
Atributos
+
Métodos

Executa apenas quando invocado.
```

### Agente

```text
Fatos
+
Regras
+
Autonomia
+
Proatividade
+
Adaptação
+
Comunicação
```

Os agentes são a base dos **Sistemas Multiagentes (SMA)**, nos quais diversas entidades inteligentes cooperam através de comunicação em rede para resolver problemas complexos de forma distribuída.