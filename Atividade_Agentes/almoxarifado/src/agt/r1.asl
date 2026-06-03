
// Quantidade de viagens disponíveis para guardar peças pequenas
viagens(10).

!start.

// Mensagem inicial do agente
+!start : true
    <- .print("guardo peças pequenas").

// Quando perceber uma peça pequena e ainda tiver viagens disponíveis
+peca(Tamanho) : Tamanho = peq & viagens(Viagens) & Viagens > 0
    <- .print("percebi uma peça ", Tamanho,
              " e vou guarda-la. Viagens restantes: ", Viagens);

       // Solicita ao ambiente guardar a peça
       guardar(Tamanho);

       // Atualiza o número de viagens restantes
       NovaQtd = Viagens - 1;
       -viagens(Viagens);
       +viagens(NovaQtd).

// Caso apareça uma peça pequena e não existam mais viagens
+peca(peq) : viagens(0)
    <- .print("Vi uma peça pequena, mas minhas viagens acabaram!").

// Sempre que aparecer uma peça grande, solicita ajuda ao r2
+peca(grd)
    <- .print("percebi uma peça grande e vou pedir ajuda para o r2");
       .send(r2, achieve, vamosGuardar(grd)).
