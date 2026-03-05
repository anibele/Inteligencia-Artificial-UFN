Aula 03 - Resolvendo jogos com força bruta de IA

Sudoku - Lógica do algoritmo com profundidade

Estados
    qtdCasasVazias = x(56 por exemplo);
    dimensao = 9;
    matriz[dimensao,dimensao]
Estado inicial
    matriz com numeros sorteados (1 - dimensao);
Estado Final
    qtdCasasVazias == 0;

Regras de transição -> Depositar em sequencia de (1 - dimensao) em sequencia no primeiro slot vazio.

Restrições
    verificar nº na linha
    verificar nº na coluna
    verificar nº no box (3x3)

Visitados
    Transformar matriz em string e comparar com a mudança atual, colocando espaços vazios como 0.
    Basta comparar as linhas de string para comparar as matrizes, tornando a comparação menor no consumo de recursos.

Função objetivo / meta
    qtdCasasVazias == 0;

///

Maze Runner / labirinto - Lógica do algoritmo

Cenário
    Matriz[n,n] do tipo char

1) Definir obstáculos (caractere '#') em células da matriz de forma aleatória (% definida pelo usuário)
2) Sortear a posição linha, coluna da entrada (caractere 'E')
3) Sortear a posição linha, coluna da saída (caractere 'S')

Os espaços vazios da matriz são marcados com [""]
if(matriz[l,c] == "" || matriz[l,c] != "#"){
    //aqui pode andar
}

Problema/objetivo
    Descobrir um caminho entre 'E' e 'S' e relatar os comandos para chegar lá.
    O melhor caminho é o que tem menos passos, ou seja temos que saber todos os caminhos possíveis.

1) Estados = 
    variáveis de Estados contendo: 
    matriz[n,n] do tipo char onde o 'E' marca a entrada, 'S' saída e '#' obstáculo. 
    linhaEntrada - int
    colunaEntrada - int
    linhaSaida - int
    colunaSaida - int
    
Estado inicial: função que faça E, S e # sorteados em linhas e colunas.

Estado Final:
if(linhaEntrada == linhaSaida && colunaEntrada == colunaSaida){
    //condição atendida
}

2) Regras de transição:
    linhaEntrada e colunaEntrada mudam as posições na matriz em cima, baixo, esquerda e direita.
    cima:linhaEntrada--
    baixo:linhaEntrada++
    esquerda:colunaEntrada--
    direita:colunaEntrada++

3) Restrições:
    if (linhaEntrada == (n-1)){
        //não pode andar
    }
    if (linhaEntrada == 0){
        //não pode andar
    }
    if (colunaEntrada == (n-1)){
        //não pode andar
    }
    if (colunaEntrada == 0){
        //não pode andar
    }

4) Visitados:
    Guardar valores de linhaEntrada e colunaEntrada
    String de concatenação de linhaEntrada com colunaEntrada

5) Função Objetivo
    if(linhaEntrada == linhaSaida && colunaEntrada == colunaSaida){
    //condição atendida
    }
    ou seja, Entrada 'E' na mesma célula de Saída 'S'.