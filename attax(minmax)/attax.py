from tkinter import * #para criar janelas
import numpy as np    #arrays todos bacanos
import random 



#SIMBOLOS
cor_cir_play_1="blue" #azul
cor_cir_play_2 = "orange"#laranja
cor_cir_play_pos="grey"
cor_cir_play_default="white"
cor_quadrado="Black"

#Programa em si
#Parte inicial
class Attax_PL3I():
    def __init__(self):
        self.menu_usuario()
        self.play_1_vez= True
        self.nao_fim_de_jogo= True
        self.quadrados_livres= True
        self.primeiro_clique= True
        self.posicao_clic1=np.array([0,0])
        self.jogador=1 if self.play_1_vez else 2
        
    def mainloop(self):
        self.janela.mainloop()

#Parte Grafica

    def menu_usuario(self):
        self.janela_menu=Tk()
        self.janela_menu.title('Menu_Attax_PL3I')
        self.butao1_menu=Button(self.janela_menu,text="Player vs Player", command=self.apos_butao_menu1)
        self.butao1_menu.pack()
        self.butao2_menu=Button(self.janela_menu,text="Player vs Pc", command=self.apos_butao_menu2)
        self.butao2_menu.pack()
        self.butao3_menu=Button(self.janela_menu,text="Pc vs Pc", command=self.apos_butao_menu3)
        self.butao3_menu.pack()
        self.butao4_menu=Button(self.janela_menu,text="quit", command=self.apos_butao_menu4)
        self.butao4_menu.pack()


      
    def desenhar_tabuleiro(self):
        self.janela=Tk() #cria janela com botoes de max,min e fechar como uma app normal
        self.janela.title('Attax_PL3I')
        self.tela_jogo = Canvas(self.janela, width=self.tamanho_tabuleiro, height=self.tamanho_tabuleiro, background=cor_cir_play_default)
        self.tela_jogo.pack()
        self.tela_jogo.delete("all")
        for i in range(self.divisoes-1):
            self.tela_jogo.create_line((i+1)*self.tamanho_quadrados, 0, (i+1)*self.tamanho_quadrados, self.tamanho_tabuleiro)
        for i in range(self.divisoes-1):
            self.tela_jogo.create_line(0,(i+1)*self.tamanho_quadrados, self.tamanho_tabuleiro, (i+1)*self.tamanho_quadrados)
        self.desenhar_circulos()
        for i in range(self.divisoes):
            for j in range(self.divisoes):
                if self.tabuleiro[i][j]==8:
                    posicao_logica=np.array([i,j])
                    posicao_grelha=self.converter_posicao_logica_para_grelha(posicao_logica)
                    self.tela_jogo.create_rectangle(posicao_grelha[0] - self.tamanho_simbolos*2, posicao_grelha[1] - self.tamanho_simbolos*2,
                                    posicao_grelha[0] + self.tamanho_simbolos*2, posicao_grelha[1] + self.tamanho_simbolos*2, 
                                    outline=cor_quadrado,fill=cor_quadrado)
        self.vez_depende_modo_jogo()
        
    def desenhar_circulos(self):
        for i in range(self.divisoes):
            for t in range (self.divisoes):
                posicao_logica=np.array([i,t])
                posicao_grelha=self.converter_posicao_logica_para_grelha(posicao_logica) 
                if self.tabuleiro[i][t]==0:
                    self.tela_jogo.create_oval(posicao_grelha[0] - self.tamanho_simbolos, posicao_grelha[1] - self.tamanho_simbolos,
                                    posicao_grelha[0] + self.tamanho_simbolos, posicao_grelha[1] + self.tamanho_simbolos, 
                                    outline=cor_cir_play_default,fill=cor_cir_play_default)
                elif self.tabuleiro[i][t]==1:                    
                    self.tela_jogo.create_oval(posicao_grelha[0] - self.tamanho_simbolos, posicao_grelha[1] - self.tamanho_simbolos,
                                    posicao_grelha[0] + self.tamanho_simbolos, posicao_grelha[1] + self.tamanho_simbolos, 
                                    outline=cor_cir_play_1,fill=cor_cir_play_1)
                elif self.tabuleiro[i][t]==2:                    
                    self.tela_jogo.create_oval(posicao_grelha[0] - self.tamanho_simbolos, posicao_grelha[1] - self.tamanho_simbolos,
                                    posicao_grelha[0] + self.tamanho_simbolos, posicao_grelha[1] + self.tamanho_simbolos, 
                                    outline=cor_cir_play_2,fill=cor_cir_play_2)
                elif self.tabuleiro[i][t]==3:
                    self.tela_jogo.create_oval(posicao_grelha[0] - self.tamanho_simbolos, posicao_grelha[1] - self.tamanho_simbolos,
                                    posicao_grelha[0] + self.tamanho_simbolos, posicao_grelha[1] + self.tamanho_simbolos, 
                                    outline=cor_cir_play_pos,fill=cor_cir_play_pos)

    def mostrar_fim(self):
        mensagem=('O vencedor :'+self.vencedor)
        self.tela_jogo.create_text(self.tamanho_quadrados*self.divisoes/2, self.tamanho_quadrados*self.divisoes/2, 
                                font="cmr 30 bold", fill='red', text=mensagem)

#Parte logica do menu
                            
    def apos_butao_menu1(self):
        self.modo_jogo=1
        self.janela_menu.destroy()
        self.janela_opcoes=Tk()
        self.janela_opcoes.title('Opcoes_Attax')
        self.butao1_opcoes=Button(self.janela_opcoes,text="Tabuleiro 7x7",command=self.escolher_tab)
        self.butao1_opcoes.pack()
        self.butao2_opcoes=Button(self.janela_opcoes,text="Tabuleiro 14x14",command=self.escolher_tab2)
        self.butao2_opcoes.pack()
        self.butao3_opcoes=Button(self.janela_opcoes,text="Tabuleiro 5x5",command=self.escolher_tab3)
        self.butao3_opcoes.pack()

    def apos_butao_menu2(self):
        self.modo_jogo=2
        self.janela_menu.destroy()
        self.janela_opcoes=Tk()
        self.janela_opcoes.title('Opcoes_Attax')
        self.butao1_opcoes=Button(self.janela_opcoes,text="Tabuleiro 7x7",command=self.escolher_tab)
        self.butao1_opcoes.pack()
        self.butao2_opcoes=Button(self.janela_opcoes,text="Tabuleiro 14x14",command=self.escolher_tab2)
        self.butao2_opcoes.pack()
        self.butao3_opcoes=Button(self.janela_opcoes,text="Tabuleiro 5x5",command=self.escolher_tab3)
        self.butao3_opcoes.pack()

    def apos_butao_menu3(self):
        print('PCvPc')
    def apos_butao_menu4(self):
        quit()

    def escolher_tab(self):
        self.f='tabuleiro_7x7.txt'
        self.tabuleiro = np.loadtxt(self.f)
        self.tabuleiro_dimensoes()
        self.janela_opcoes.destroy()
        self.desenhar_tabuleiro()

    def escolher_tab2(self):
        self.f='tabuleiro_14x14.txt'   
        self.tabuleiro = np.loadtxt(self.f)
        self.tabuleiro_dimensoes()
        self.janela_opcoes.destroy()
        self.desenhar_tabuleiro()
    
    def escolher_tab3(self):
        self.f='tabuleiro_5x5.txt'   
        self.tabuleiro = np.loadtxt(self.f)
        self.tabuleiro_dimensoes()
        self.janela_opcoes.destroy()
        self.desenhar_tabuleiro()

#Parte interação user-computador
#Como lidar com os cliques etc
#parte logica

    def tabuleiro_dimensoes(self):
        self.divisoes=(len(self.tabuleiro[0]))
        self.tamanho_tabuleiro = 600 #600 c o numero de pixeis
        self.tamanho_quadrados = self.tamanho_tabuleiro/self.divisoes # quadrados individuais dentro do tabuleiro
        self.tamanho_simbolos=(self.tamanho_quadrados*0.5)/2


    def vez_depende_modo_jogo(self):
        if self.modo_jogo==1:
            self.janela.bind('<Button-1>', self.clicar)
        elif self.modo_jogo==2:
            if self.play_1_vez:
                self.janela.bind('<Button-1>', self.clicar)
            else:
                self.fim()
                self.jogador=1 if self.play_1_vez else 2
                if self.nao_fim_de_jogo:
                    self.bot_random()
                else:
                    self.mostrar_fim()
    
    
    def clicar(self, event):
        posicao_grelha = [event.x, event.y]
        posicao_logica = self.converter_posicao_grelha_para_logica(posicao_grelha)
        self.fim()
        self.jogador=1 if self.play_1_vez else 2
        if self.nao_fim_de_jogo:
            if self.primeiro_clique:
                self.clic_1(posicao_logica)
            else:
                self.clic_2(posicao_logica)
        else:
            self.mostrar_fim()

    
    def clic_1(self,posicao_logica):
        if self.tabuleiro[posicao_logica[0]][posicao_logica[1]]==self.jogador and self.jogada_valida(posicao_logica):
            self.posicao_clic1 = np.array(posicao_logica, dtype=int)
            self.jogadas_possiveis(posicao_logica)
            self.desenhar_circulos()
            #print(self.tabuleiro)##TROUBLESHOOTER
            self.primeiro_clique= not self.primeiro_clique
    
    def clic_2(self,posicao_logica):
        posicao_logica = np.array(posicao_logica)
        if self.tabuleiro[posicao_logica[0]][posicao_logica[1]]==3:
            if posicao_logica[0]==(self.posicao_clic1[0]+2) or posicao_logica[0]==(self.posicao_clic1[0]-2) or posicao_logica[1]==(self.posicao_clic1[1]+2) or posicao_logica[1]==(self.posicao_clic1[1]-2) :
                self.tabuleiro[posicao_logica[0]][posicao_logica[1]]=self.jogador
                self.tabuleiro[self.posicao_clic1[0]][self.posicao_clic1[1]]=0
            else:
                self.tabuleiro[posicao_logica[0]][posicao_logica[1]]=self.jogador
            self.comer_pecas(posicao_logica)
            self.limpar_array()
            self.desenhar_circulos()
            self.primeiro_clique= not self.primeiro_clique
            self.play_1_vez = not self.play_1_vez
            #print(self.tabuleiro)##TROUBLESHOOTER
            self.vez_depende_modo_jogo()

    def jogada_valida(self, posicao_logica):
        posicao_logica = np.array(posicao_logica)
        count=0
        for i in range(-2,3):#deixar jogo simples (-1,2) verdadeiro (-2,3)
            for t in range (-2,3):#deixar jogo simples (-1,2) verdadeiro (-2,3)
                if (posicao_logica[0]+i) >=0 and (posicao_logica[1]+t) >=0 and (posicao_logica[0]+i) <=(self.divisoes-1) and (posicao_logica[1]+t) <=(self.divisoes-1):
                    if self.tabuleiro[posicao_logica[0]+i] [posicao_logica[1]+t]==0: 
                        count+=1
        if count>0:
            return self.quadrados_livres
        else:
            return not self.quadrados_livres
    
    def jogadas_possiveis(self, posicao_peca1):
        posicao_peca1 = np.array(posicao_peca1)
        for i in range(-2,3):#deixar jogo simples (-1,2) verdadeiro (-2,3)
            for t in range (-2,3):#deixar jogo simples (-1,2) verdadeiro (-2,3)
                if (posicao_peca1[0]+i) >=0 and (posicao_peca1[1]+t) >=0 and (posicao_peca1[0]+i) <=(self.divisoes-1) and (posicao_peca1[1]+t) <=(self.divisoes-1):
                    if self.tabuleiro[posicao_peca1[0]+i] [posicao_peca1[1]+t]==0: 
                        self.tabuleiro[posicao_peca1[0]+i] [posicao_peca1[1]+t]=3
    
    def comer_pecas(self, posicao_jogada):
        for i in range(-1,2):
            for t in range (-1,2):
                if self.play_1_vez:
                    if (posicao_jogada[0]+i) >=0 and (posicao_jogada[1]+t) >=0 and (posicao_jogada[0]+i) <=(self.divisoes-1) and (posicao_jogada[1]+t) <=(self.divisoes-1):
                        if self.tabuleiro[posicao_jogada[0]+i][posicao_jogada[1]+t]==2:
                            self.tabuleiro[posicao_jogada[0]+i][posicao_jogada[1]+t]=self.jogador
                else:
                    if (posicao_jogada[0]+i) >=0 and (posicao_jogada[1]+t) >=0 and (posicao_jogada[0]+i) <=(self.divisoes-1) and (posicao_jogada[1]+t) <=(self.divisoes-1):
                        if self.tabuleiro[posicao_jogada[0]+i][posicao_jogada[1]+t]==1:
                            self.tabuleiro[posicao_jogada[0]+i][posicao_jogada[1]+t]=self.jogador


    def limpar_array(self):
        for i in range(0,self.divisoes):
                for t in range (0,self.divisoes):
                    if self.tabuleiro[i][t]==3: 
                        self.tabuleiro[i][t]=0

    def fim(self):
        countazul=0
        countlaranj=0
        countvazio=0
        for i in range(self.divisoes):
            for t in range(self.divisoes):
                if self.tabuleiro[i][t]==1:
                    countazul+=1
                elif self.tabuleiro[i][t]==2:
                    countlaranj+=1
                elif self.tabuleiro[i][t]==0:
                    countvazio+=1
        if countazul==0:
            self.vencedor='Player2'
            self.nao_fim_de_jogo=not self.nao_fim_de_jogo
        elif countlaranj==0:
            self.vencedor='Player1'
            self.nao_fim_de_jogo=not self.nao_fim_de_jogo
        elif countvazio==0:
            if countazul>countlaranj:
                self.vencedor='Player1'
            elif countlaranj>countazul:
                self.vencedor='Player2'
            else:
                self.vencedor='Empate'
            self.nao_fim_de_jogo=not self.nao_fim_de_jogo

    def bot_random(self):#bot random so para perceber como integrar um bot ##lidar com o problema do codigo ser movido por um random event neste caso o clic do rato
        pos_disponivel1=[]
        pos_disponivel2=[]

        for i in range (self.divisoes):
            for t in range (self.divisoes):
                if self.tabuleiro[i][t]==self.jogador and self.jogada_valida([i,t]):
                    pos_disponivel1.append([i,t])

        posicao_logica=pos_disponivel1[random.randint(0, len(pos_disponivel1)-1)]
        #print('pos_log 1')##TROUBLESHOOTER
        #print(posicao_logica)##TROUBLESHOOTER
        self.clic_1(posicao_logica)

        for i in range (self.divisoes):
            for t in range (self.divisoes):
                if self.tabuleiro[i][t]==3:
                    pos_disponivel2.append([i,t])

        #print(pos_disponivel2)##TROUBLESHOOTER
        posicao_logica=pos_disponivel2[random.randint(0, len(pos_disponivel2)-1)]
        self.clic_2(posicao_logica)

        


 #Parte que premite converter a logica do jogo para a interface do usuario e vice-versa   
    def converter_posicao_logica_para_grelha(self, posicao_logica):
        posicao_logica = np.array(posicao_logica, dtype=int)
        return (self.tamanho_tabuleiro/self.divisoes)*posicao_logica + self.tamanho_tabuleiro/self.divisoes/2

    def converter_posicao_grelha_para_logica(self, posicao_grelha):
        posicao_grelha = np.array(posicao_grelha)
        return np.array(posicao_grelha//(self.tamanho_tabuleiro/self.divisoes), dtype=int)

    

Attax_PL3I()



