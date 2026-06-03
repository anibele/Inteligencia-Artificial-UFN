viagens(5). 

!start.

+!start : true 
    <- .print("guardo peças pequenas").

+peca(Tamanho) : Tamanho = peq & viagens(Viagens) & Viagens > 0
    <- .print("percebi uma peça ", Tamanho, " e vou guarda-la. Viagens restantes: ", Viagens);
       guardar(Tamanho);
       viagens(Qtd);
       novaQtd = Qtd - 1;
       -viagens(Qtd);
       +viagens(novaQtd).

// plano pra quando acabar as viagens
+peca(peq) : viagens(0)
    <- .print("Vi uma peça pequena, mas minhas viagens acabaram!").

+peca(Tamanho) : Tamanho = grd
    <- .print("percebi uma peça grande e vou pedir ajuda para o r2");
       .send(r2,achieve,vamosGuardar(Tamanho)).