Revisão:
Métodos de Busca (Soluções)
    -> Chegar em um estado desejado final(ou aproximado)
    -> Conjunto de passos até o estado desejado
Tipos de problemas
    -> Diagnóstico (Reconhecer padrões) através de treinamento (repetição)
    -> Quando não se sabe os passos até o Estado Final
Métodos de busca são motores de raciocínio
    -> Deduzir = Método de força bruta = Profundidade

Sistemas inteligentes tem:
    1. Base de conhecimento
    2. Motores de Raciocínio
        Dicas vem de matemática ou especialistas 
        Custo real g(n)
        Estimado h(n)
        2.1 Cegos ou força bruta
            -profundidade(motor do prolog)
            -largura(amplitude)
        2.2 Heurísticos ou informados
            -subida de encosta(baseado no profundidade) - usa g(n)
            -guloso(baseado na largura) - usa h(n)
            -A* - Largura g(n) + h(n)
    3. Aprendizado de máquina (Machine learning) -> Reconhecer padrões por amostras

Prolog
Motor do prolog é dedutivo com profundidade
Argumentos ou parâmetros
    -> objeto (minuscula)
    -> literal ("Matheus dos Reis")
    -> variável(primeira letra maiúscula)
Acesso em: https://swish.swi-prolog.org/
Fato -> senteça ou predicado ou assertiva
fato(argumentos)
ex:
papel(Alex, professor). -> O Alex tem papel de professor
papel(João, aluno). -> O joão tem papel de aluno
papel(Gustavo, aluno). -> O Gustavo tem o papel de aluno
papel(Gustavo, monitor). -> O Gustavo tem o papel de monitor
estado(luz,ligado). -> A luz está ligada.
estado(ar-condicionado,desligado). -> O ar-condicionado está desligado.
matriculado(Matheus, jogos, ia)
matriculado(Matheus, jogos, design)
progenitor(jura, alex)
progenitor(jura, tina)
progenitor(alex, dante)
progenitor(simone, dante)

nesse exemplo tenho 4 predicados
