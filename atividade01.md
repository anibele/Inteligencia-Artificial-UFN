Problema dos Missionários e Canibais

Há 3 missionários e 3 canibais. Há também um barco que vai da margem esquerda para a margem direita e vice-versa, sempre levando uma ou duas pessoas. Todas as pessoas estão na margem esquerda e precisam ir para a margem direita. Porém, há restrições: em momento algum pode ficar mais canibais do que missionários em uma das margens.

Estado inicial:
CE = 3
ME = 3
CD = 0
MD = 0

Estado Final:
CE = 0
ME = 0
CD = 3
MD = 3

Regras de transição:
levar um missonário ou 2 missionários por vez
o barco não pode estar vazio

os CE e o CD nunca podem ser maiores que ME e MD
o barco tem que estar no lado esquerdo ou dieito
podemos guardar numa string como ME "0033"

Resolução:

1) Estados do Problema
Cada estado representa a quantidade de pessoas em cada margem e a posição do barco.
ME (Missionários Esquerda) → int (0 a 3)
CE (Canibais Esquerda) → int (0 a 3)
MD (Missionários Direita) → int (0 a 3)
CD (Canibais Direita) → int (0 a 3)
Barco → char (E esquerda / D direita)

Estado Inicial
ME = 3
CE = 3
MD = 0
CD = 0
Barco = E

Estado Final
ME == 0
CE == 0
MD == 3
CD == 3
Barco == D

2) Regras de Transição
-transporta 1 ou 2 pessoas
-nunca pode ir vazio
-sempre muda de lado

Movimentos possíveis:
1 missionário
2 missionários
1 canibal
2 canibais
1 missionário + 1 canibal

3) Restrições
-Nunca pode haver mais canibais que missionários em uma margem (se houver missionários);
-Barco não pode ir vazio
-Limite do barco são 2 pessoas

4) Visitados
Representação do estado em String:
Exemplo:
"33E" que significa:

3 missionários esquerda
3 canibais esquerda
barco esquerda

Guardar isso em uma lista:
visitados = ["33E", "31D", "32E"]

5) Função Objetivo / Meta
O objetivo é levar todos para a direita:
if (ME == 0 && CE == 0 && MD == 3 && CD == 3) {
    return true;
}



