
// Quantidade de viagens disponíveis para guardar peças médias
viagens(15).

!start.

// Mensagem inicial do agente
+!start : true
    <- .print("guardo peças médias").

// Quando perceber uma peça média e ainda possuir viagens disponíveis
+peca(med) : viagens(V) & V > 0
    <- .print("percebi uma peça media e vou guarda-la. Viagens restantes: ", V);

       // Solicita ao ambiente guardar a peça
       guardar(med);

       // Atualiza o contador de viagens
       NovaQtd = V - 1;
       -viagens(V);
       +viagens(NovaQtd).

// Caso apareça uma peça média e não existam mais viagens
+peca(med) : viagens(0)
    <- .print("Vi uma peça média, mas minhas viagens acabaram!").

// Recebe o pedido de ajuda do r1 para guardar uma peça grande
+!vamosGuardar(grd)[source(Agt)] : viagens(V) & V > 0
    <- .print(Agt,
              " me chamou para guardar a peça grande. Viagens restantes r2: ",
              V);

       // Guarda a peça grande
       guardar(grd);

       // Atualiza o contador de viagens
       NovaQtd = V - 1;
       -viagens(V);
       +viagens(NovaQtd).

// Caso não tenha mais viagens disponíveis para ajudar
+!vamosGuardar(grd)[source(Agt)] : viagens(0)
    <- .print("Não posso ajudar ",
              Agt,
              " com a peça grande porque minhas viagens acabaram.").
