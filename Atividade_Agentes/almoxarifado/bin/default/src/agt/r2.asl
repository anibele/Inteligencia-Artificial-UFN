viagens(3). 

!start.

+!start : true  
    <- .print("guardo peças médias").

+peca(med) : viagens(V) & V > 0
    <- .print("percebi uma peça media e vou guarda-la. Viagens restantes: ", V);
       guardar(med);
       viagens(Qtd);
       novaQtd = Qtd - 1;
       -viagens(Qtd);
       +viagens(novaQtd).

+peca(med) : viagens(0)
    <- .print("Vi uma peça média, mas minhas viagens acabaram!").

// r2 recebe o pedido de ajuda, checa se tem viagens abertas, ajuda a guardar e avisa o ambiente.
+!vamosGuardar(grd)[source(Agt)] : viagens(viagens) & V > 0  
    <- .print(Agt, " me chamou para guardar a peça grande. Viagens restantes r2: ", viagens);
       guardar(grd);   
       viagens(Qtd);
       novaQtd = Qtd - 1;
       -viagens(Qtd);
       +viagens(novaQtd).

+!vamosGuardar(grd)[source(Agt)] : viagens(0)
    <- .print("Não posso ajudar ", Agt, " com a peça grande porque minhas viagens acabaram.").