Inteligência Artificial - Técnicas ou metodologias
    -Sistemas de comportamento Inteligente
        -Base de conhecimento
            -Armazenamento de experiência(PROLOG; SMA)
        -Motor de raciocínio / raciocínio automatizado (dedução, indução)
            -(Métodos de busca; SMA)
            -Cegos: Amplitude e profundidade
            -Heuristicos: Subida de encosta, guloso, A*, Algoritmos Genéticos
        -Aprendizado de máquina - Reconhecer padrões de repetição (com amostras)
            -Redes neurais

    -Métodos de busca
        -Modelagem de problema / Solução
        1)Estados (inicial/construtor, intermediario/construtor2, final)
        2)Regras de transição -> metodos que modificam o objeto
        3)Restrições - estados que não podem ser gerados
        4)Visitados - lista, árvore ou hasmap
        5)Função objetivo

    A) Problema das torres de hanoi
    
    Estados
        //toda pilha tem os seguintes comandos: empty, peek, push/add, pop/remove
        Stack t1 = new Stack();
        Stack t2 = new Stack();
        Stack t3 = new Stack();

    Estado inicial
        t1.push(3)
        t1.push(2)
        t1.push(1)
    
    Estado final ou função objetivo / meta
        t1.empty() && t2.empty()
    
    Regras de transição
        r1 - mover t1 para t2
        if ehValido(t1,t2){
            public void moverT1_T2(){
                t2.push(t1.pop());
            }
            Estado novo = new Estado(t1,t2,t3,"movendo topo t1 para topo t2")
            if(visitados.contains(novo)){
                visitados.add(novo);
            }
        }

        r1 - mover t1 para t3
        public void moverT1_T3(){
            t3.push(t1.pop());
        }

        r1 - mover t2 para t1
        public void moverT2_T1(){
            t1.push(t2.pop());
        }

        r1 - mover t2 para t3
        public void moverT2_T3(){
            t3.push(t2.pop());
        }

        r1 - mover t3 para t1
        public void moverT3_T1(){
            t1.push(t3.pop());
        }

        r1 - mover t3 para t2
        public void moverT1_T2(){
            t2.push(t3.pop());
        }
    
    Restrição
        public boolean ehValido(Origem, Stack Destino){
            if(Origem.empty()){
                return false;
            }
            if((int)Origem.peak() > (int)(Destino.peek)){
                return false;
            }

            return true;
        }
    
    Visitados - Lista ou árvore ou Hashmap

    B) Problema das Jarras
    jarra1 suporta 4 litros
    jarra2 suporta 3 litros
    torneira que jorra água infinitamente
    objetivo: deixar em uma das jarras 2 litros

    class Estado{
        int j1;
        int j2;

        public Estado(int j1, int j2){
            this.j1 = j1;
            this.j2 = j2;
        }

        public boolean ehMeta(){
            return (this.j1 == 2 & this.j2 == 0 || this.j1 == 0 & this.j2 == 2);
        }

        public void encherj1(){
            this.j1 = 4;
        }

        public void encherj2(){
            this.j2 = 3;
        }

        public void esvaziarj1(){
            this.j1 = 0;
        }

        public void esvaziarj2(){
            this.j2 = 0;
        }

        public void despejarj2_j1(){
            int j1 = this.j1;
            int j2 = this.j2;

            if(j2 > (4 - j1)){
                j2 = j2 - (4 - j1);
                j1 = 4;
            }else{
                j1 = j1 + j2;
                j2 = 0;
            }
        }
    }