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