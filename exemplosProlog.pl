%base.pl
%fatos
	%sentenças ou predicados ou assinaturas de funções

%regras

jogo("CS","Counter Strike",16,"FPS").
jogo("LOL","League of Legends",18,"MOBA").
jogo("AID","Alone in the dark",16, "SU").
jogo("GTA","Grand Thief Auto",18, "SB").
jogo("MC","Minecraft",0,"SB").

tipo("SB","Sandbox").
tipo("FPS","First person shooter").
tipo("MOBA","Multiplayer online battle arena").
tipo("SU","Survivor").

% Ex de pesquisa: 
% jogo(Sigla,Nome,Idade,"SB").

%Regras são sentenças com variáveis acompanhadas por :- (Se somente se)

indicacaolivre(NomeJogo) :-
    jogo(_,NomeJogo,Idade,_),
    Idade == 0.

progenitor(herbert,cleber).
progenitor(herbert,homer).
progenitor(homer,bart).
progenitor(homer,lisa).
progenitor(homer,meg).
progenitor(marge,bart).
progenitor(marge,lisa).
progenitor(marge,meg).
progenitor(bart,alex).
progenitor(bart,tina).

avo(A,N) :-
    progenitor(A,P),
    progenitor(P,N).
% Ex de pesquisa: 
% avo(herbert,N).

irmaos(A,B) :-  progenitor(P,A),
    			progenitor(P,B),
    			A \= B.

tio(T,S) :-
    irmaos(I,T),
    progenitor(I,S).