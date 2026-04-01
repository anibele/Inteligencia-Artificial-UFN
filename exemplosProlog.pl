% Fatos de Jogos
% jogo(Sigla, Nome, Idade, Categoria).
jogo(cs, 'Counter Strike', 16, fps).
jogo(lol, 'League of Legends', 18, moba).
jogo(aid, 'Alone in the Dark', 16, su).
jogo(gta, 'Grand Theft Auto', 18, sb).
jogo(mc, 'Minecraft', 0, sb).

% Categorias
tipo(sb, 'Sandbox').
tipo(fps, 'First Person Shooter').

% Regra de indicação livre usando unificação direta
indicacaolivre(Nome) :- jogo(_, Nome, 0, _).

% Árvore Genealógica
progenitor(herbert, cleber).
progenitor(herbert, homer).
progenitor(homer, bart).
progenitor(homer, lisa).
progenitor(homer, meg).
progenitor(marge, bart).
progenitor(marge, lisa).
progenitor(marge, meg).
progenitor(bart, alex).
progenitor(bart, tina).

% Regras de Parentesco
avo(A, N) :- 
    progenitor(A, P), 
    progenitor(P, N).

irmaos(A, B) :- 
    progenitor(P, A), 
    progenitor(P, B), 
    A \= B.

tio(T, S) :- 
    progenitor(P, S), 
    irmaos(P, T).

sobrinho(S, T) :- 
    tio(T, S).

primo(X, Y) :- 
    progenitor(P1, X),
    progenitor(P2, Y),
    irmaos(P1, P2).

cunhado(C, P) :- 
    casal(P, Conjuge), irmaos(Conjuge, C).

cunhado(C, P) :- 
    irmaos(P, Irmao), casal(Irmao, C).
	
neto(N, A) :- 
    avo(A, N).
