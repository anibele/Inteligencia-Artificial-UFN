package example;

// Ambiente do projeto almoxarifado

import java.util.Random;
import java.util.logging.Logger;

import jason.asSyntax.ASSyntax;
import jason.asSyntax.Structure;
import jason.environment.Environment;

public class Env extends Environment {

    /**
     * Sorteia aleatoriamente qual peça será colocada no almoxarifado.
     * Pode retornar:
     * - peca(peq) : peça pequena
     * - peca(med) : peça média
     * - peca(grd) : peça grande
     */
    String sortearPeca() {
        Random gerador = new Random();
        int sorteado = gerador.nextInt(3);

        if (sorteado == 0) {
            return "peca(peq)";
        }

        if (sorteado == 1) {
            return "peca(med)";
        }

        if (sorteado == 2) {
            return "peca(grd)";
        }

        // nunca deve ocorrer, mas garante um retorno válido
        return "peca(peq)";
    }

    // Utilizado para exibir mensagens no console
    private Logger logger = Logger.getLogger("almoxarifado." + Env.class.getName());

    // Armazena a peça atualmente disponível no ambiente
    String peca_sorteada = sortearPeca();

    /**
     * Executado uma única vez quando o sistema multiagente inicia.
     * Adiciona as percepções iniciais do ambiente.
     */
    @Override
    public void init(String[] args) {
        super.init(args);

        try {
            // adiciona a primeira peça ao ambiente
            addPercept(ASSyntax.parseLiteral(peca_sorteada));

            // percepção adicional de exemplo
            addPercept(ASSyntax.parseLiteral("dia(quarta)"));

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Método executado sempre que um agente realiza uma ação.
     */
    @Override
    public boolean executeAction(String agName, Structure action) {

        // r1 guarda peças pequenas
        if (agName.equals("r1") && action.toString().equals("guardar(peq)")) {

            logger.info(agName + " está guardando peça pequena....");

        }
        // r2 guarda peças médias
        else if (agName.equals("r2") && action.toString().equals("guardar(med)")) {

            logger.info(agName + " está guardando peça média....");

        }
        // tratamento da peça grande
        else if (action.toString().equals("guardar(grd)")) {

            logger.info("Os agentes r1 e r2 estão guardando a peça grande!");

        }
        // qualquer ação não implementada
        else {

            logger.info("executing: " + action + ", but not implemented!");

        }

        try {

            /*
             * Remove do ambiente a peça que acabou de ser guardada.
             * Isso vale para peças pequenas, médias e grandes.
             */
            String pecaAtual = peca_sorteada;
            removePercept(ASSyntax.parseLiteral(pecaAtual));

            /*
             * Sorteia a próxima peça que será disponibilizada
             * após um pequeno intervalo.
             */
            peca_sorteada = sortearPeca();

            // simula o tempo de chegada da próxima peça
            Thread.sleep(4000);

            logger.info("Uma nova peça está sendo colocada no almoxarifado...");

            // adiciona a nova peça ao ambiente
            addPercept(ASSyntax.parseLiteral(peca_sorteada));

        } catch (Exception e) {
            e.printStackTrace();
        }

        return true;
    }

    /**
     * Executado quando o MAS é encerrado.
     */
    @Override
    public void stop() {
        super.stop();
    }
}
