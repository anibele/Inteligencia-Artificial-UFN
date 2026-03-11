package com.mycompany.barcocanibais;

import java.util.ArrayList;
import java.util.List;

public class BarcoCanibais {

    // Lista de estados já visitados
    static List<String> visitados = new ArrayList<>();

    // Lista que guarda os movimentos realizados
    static List<String> movimentos = new ArrayList<>();

    /**
     * Método principal que inicia a execução do algoritmo.
     */
    public static void main(String[] args) {

        // Estado inicial: 3 missionários, 3 canibais e barco na esquerda
        String estadoInicial = "33E";

        boolean encontrou = buscaSolucao(estadoInicial);

        if (encontrou) {

            System.out.println("Solucao encontrada:\n");

            for (int i = 0; i < movimentos.size(); i++) {
                System.out.println("Movimento " + (i + 1) + ": " + movimentos.get(i));
            }

        } else {
            System.out.println("Nenhuma solucao encontrada.");
        }
    }

    /**
     * Implementa a busca em profundidade
     *
     * O algoritmo tenta realizar movimentos possíveis e explora os estados até
     * encontrar o objetivo.
     *
     * @param estado estado atual representado por string
     * @return true se encontrou solução
     */
    public static boolean buscaSolucao(String estado) {

        // Verifica se o estado é válido
        if (!estadoValido(estado)) {
            return false;
        }

        // Evita repetir estados já visitados
        if (visitados.contains(estado)) {
            return false;
        }

        // Marca estado como visitado
        visitados.add(estado);

        // Verifica se chegamos ao estado final
        if (estadoFinal(estado)) {
            return true;
        }

        // Possíveis movimentos do barco
        int[][] movimentosPossiveis = {
            {1, 0},
            {2, 0},
            {0, 1},
            {0, 2},
            {1, 1}
        };

        // Testa cada movimento possível
        for (int[] mov : movimentosPossiveis) {

            int m = mov[0];
            int c = mov[1];

            String novoEstado = gerarEstado(estado, m, c);

            if (novoEstado != null) {

                // Guarda descrição do movimento
                movimentos.add(movimento(estado, m, c));

                // Continua a busca recursivamente
                if (buscaSolucao(novoEstado)) {
                    return true;
                }

                // Backtracking: remove movimento caso não leve à solução
                movimentos.remove(movimentos.size() - 1);
            }
        }

        return false;
    }

    /**
     * Gera um novo estado após mover missionários e canibais.
     *
     * @param estado estado atual
     * @param m quantidade de missionários
     * @param c quantidade de canibais
     * @return novo estado ou null se o movimento for impossível
     */
    public static String gerarEstado(String estado, int m, int c) {

        int me = Character.getNumericValue(estado.charAt(0));
        int ce = Character.getNumericValue(estado.charAt(1));
        char barco = estado.charAt(2);

        int md = 3 - me;
        int cd = 3 - ce;

        if (barco == 'E') {

            me -= m;
            ce -= c;
            barco = 'D';

        } else {

            me += m;
            ce += c;
            barco = 'E';
        }

        return "" + me + ce + barco;
    }

    /**
     * Verifica se o estado é válido.
     *
     * Um estado é inválido quando: - existem números negativos - existem mais
     * de 3 pessoas - canibais são maioria onde existem missionários
     *
     * @param estado estado a ser verificado
     * @return true se for válido
     */
    public static boolean estadoValido(String estado) {

        int me = Character.getNumericValue(estado.charAt(0));
        int ce = Character.getNumericValue(estado.charAt(1));

        int md = 3 - me;
        int cd = 3 - ce;

        if (me < 0 || ce < 0 || md < 0 || cd < 0) {
            return false;
        }

        if (me > 3 || ce > 3 || md > 3 || cd > 3) {
            return false;
        }

        if (me > 0 && ce > me) {
            return false;
        }

        if (md > 0 && cd > md) {
            return false;
        }

        return true;
    }

    /**
     * Verifica se chegamos ao estado objetivo.
     *
     * Estado final esperado: todos na margem direita.
     *
     * @param estado estado atual
     * @return true se for objetivo
     */
    public static boolean estadoFinal(String estado) {

        int me = Character.getNumericValue(estado.charAt(0));
        int ce = Character.getNumericValue(estado.charAt(1));

        return me == 0 && ce == 0;
    }

    /**
     * Gera uma descrição textual do movimento realizado.
     *
     * @param estado estado atual
     * @param m missionários transportados
     * @param c canibais transportados
     * @return descrição do movimento
     */
    public static String movimento(String estado, int m, int c) {

        char barco = estado.charAt(2);

        String missionario;
        String canibal;

        if (m == 1) {
            missionario = "missionario";
        } else {
            missionario = "missionarios";
        }

        if (c == 1) {
            canibal = "canibal";
        } else {
            canibal = "canibais";
        }

        if (barco == 'E') {
            return "Barco vai da margem esquerda para a direita levando "
                    + m + " " + missionario + " e "
                    + c + " " + canibal + ".";
        } else {
            return "Barco vai da margem direita para a esquerda levando "
                    + m + " " + missionario + " e "
                    + c + " " + canibal + ".";
        }
    }
}
