import pyxel
import random
class Personagem:
    def __init__(self,x,y,largura,altura,cor,desenho):
        self.x1 = x
        self.y1 = y
        self.largura = largura
        self.altura = altura
        self.colSprites = 0
        self.linSprites = 0
        self.cor = cor
        self.passo = 0
        self.totalPassos = 2
        self.definirBox()
        self.desenho = desenho
        
#_________________________________________________________________________#     
        
    def definirBox(self):
        self.x2 = self.x1 + abs(self.largura)
        self.y2 = self.y1 + abs(self.altura)
        
#_________________________________________________________________________#          
    
    def mover(self,dx,dy):
    
        if dx > 0:
            self.colSprites = 3 
            
        if dy > 0:
            self.colSprites = 0
        if dx < 0:
            self.colSprites = 2
        if dy < 0:
            self.Sprites = 1
            
        
        if dx != 0 or dy != 0:
            self.passo += 1
            if self.passo > self.totalPassos:
                self.colSprites +=1
                self.passo = 0
            if self.colSprites >3:
                self.colSprites = 0
                
        if self.desenho == 'meleca':
        
            if dx > 0:
                self.linSprites = 3 
            
            if dy > 0:
                self.linSprites = 0
            if dx < 0:
                self.linSprites = 2
            if dy < 0:
                self.linSprites = 1
                
            
            if dx != 0 or dy != 0:
                self.passo += 1
            if self.passo > self.totalPassos:
                self.colSprites +=1
                self.passo = 0
            if self.colSprites >3:
                self.colSprites = 0
     
            self.x1 = self.x1 + dx
            self.y1 = self.y1 + dy
            self.definirBox()
  
#_________________________________________________________________________#   
  
    def draw(self):
    
        XImagem = self.largura * self.colSprites
        YImagem = self.altura * self.linSprites
        if self.desenho == 'meleca':
            pyxel.blt(self.x1, self.y1,             
                  1,                            
                  XImagem,YImagem,                        
                  self.largura, self.altura,    
                  self.cor)   
        else:
            pyxel.blt(self.x1, self.y1,             
                  1,                            
                  XImagem,YImagem,                        
                  self.largura, self.altura,    
                  self.cor)   
            
#_________________________________________________________________________#                   

class Jogo:
    def __init__(self):
        pyxel.init(136,100,"JEP")
        
        self.heroi = Personagem(90,65,14,18,7,'meleca')
        #Inicio e Fim
        self.exp = 0
        self.qual_texto = 0
        self.qual_final = 0
        self.introducao = True
        self.historia_inicial = []
        self.escolha = False
        #Dicas
        self.dica1 = False
        self.dica2 = False
        self.dica3 = False
        self.dica4 = False
        self.dica5 = False
        self.dica1_C = False
        self.dica2_C = False
        self.dica3_C = False
        self.dica4_C = False
        self.dica5_C = False
        self.dicas_total = 0
        # Coisas
        self.sala_atual = 3
        self.livro_vermelho = False
        self.livro_verde = False
        self.livro_amarelo = False
        self.sofa = False
        self.subir = False
        self.descer = False
        self.quadro = False
        self.globo = False
        self.sofa = False
        self.tapete = False
        self.qdc = False
        self.Vcogumelo = False
        
        self.win = False
        self.n_tentativas = 1
        self.t = 1
        self.texto = ''
      
        #Portas do Corredor
        self.portas = [
    # P1: Quarto
    {'x1': 20, 'x2': 45, 'destino': 1, 'arquivo': 'quarto.pyxres', 'heroi_x': 90, 'heroi_y': 65},
    # P2: Escritório
    {"x1": 75, "x2": 100, "destino": 2, "arquivo": "escritorio.pyxres", "heroi_x": 90, "heroi_y": 65},
    # P3: Sala
    {"x1": 80, 'x2': 112,'destino': 3, 'arquivo': 'sala.pyxres', 'heroi_x':  72,
 "heroi_y": 65},
    #Cofre
    {"x1": 0, 'x2': 10,'destino': 4, 'arquivo': 'cofre.pyxres', 'heroi_x':  20,
 "heroi_y": 69}
]

        #Criar Senha
        self.senha = ''
        c = 0
        
        while c != 4:
            num = random.randint(0,9)
            if str(num) in self.senha:
                pass
            else:
                self.senha += str(num)
                c += 1
            
     
        pyxel.load('sala.pyxres')      
        pyxel.images[1].load(0, 0, "personagem_56x72.png") 
        pyxel.run(self.update,self.draw)
    
#_________________________________________________________________________#      
    
    def mover(self,obj,up,down,left,right):
        dx=0
        dy=0
        if pyxel.btn(up):
            dy = -1
        if pyxel.btn(down):
            dy = +1
        if pyxel.btn(left):
            dx = -1
        if pyxel.btn(right):
            dx = +1
        
        nx = obj.x1 + dx
        ny = obj.y1 + dy
        
        if self.posicao_valida(nx, ny):
            obj.mover(dx, dy)
        
    
#_________________________________________________________________________#  

    def update(self):
    
        self.mover(self.heroi  ,pyxel.KEY_W,pyxel.KEY_S,pyxel.KEY_A,pyxel.KEY_D)
        
     #---------------------Interação com os Objetos------------------------------#
     
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        
            # Dicas
            if self.sala_atual == 3 and pyxel.mouse_x == 44 and (10 <= pyxel.mouse_y <= 22):
                self.dica1 = True
                if not self.dica1_C:
                    self.dica1_C = True
                    self.dicas_total += 1
        
            if self.sala_atual == 1 and (36 <= pyxel.mouse_x <= 46) and (14 <= pyxel.mouse_y <= 23):
                self.dica2 = True
                if not self.dica2_C:
                    self.dica2_C = True
                    self.dicas_total += 1
        
            if self.sala_atual == 2 and (117 <= pyxel.mouse_x <= 126) and (44 <= pyxel.mouse_y <= 51):
                self.dica3 = True
                if not self.dica3_C:
                    self.dica3_C = True
                    self.dicas_total += 1
        
            if self.sala_atual == 2 and pyxel.mouse_x == 73 and pyxel.mouse_y == 28:
                self.dica4 = True
                if not self.dica4_C:
                    self.dica4_C = True
                    self.dicas_total += 1
        
            if self.sala_atual == 0 and (52 <= pyxel.mouse_x <= 62) and (37 <= pyxel.mouse_y <= 48):
                self.dica5 = True
                if not self.dica5_C:
                    self.dica5_C = True
                    self.dicas_total += 1
                
            #Sala
            if pyxel.mouse_x == 41 and (pyxel.mouse_y >= 9 and pyxel.mouse_y <= 22):
                
                    self.livro_vermelho = True
             
            if pyxel.mouse_x == 46 and (pyxel.mouse_y >= 11 and pyxel.mouse_y <= 22):
                
                    self.livro_verde = True 
                    
            if pyxel.mouse_x == 48 and (pyxel.mouse_y >= 12 and pyxel.mouse_y <= 22):
                
                    self.livro_amarelo = True 
            
            if self.sala_atual == 3 and (pyxel.mouse_x >= 8 and pyxel.mouse_x <= 23) and (pyxel.mouse_y >= 12 and pyxel.mouse_y <= 30):
                
                    self.quadro = True 
                    
            if self.sala_atual == 3 and (pyxel.mouse_x >= 52 and pyxel.mouse_x <= 57) and (pyxel.mouse_y >= 13 and pyxel.mouse_y <= 22):
                
                    self.globo = True 
                    
            if self.sala_atual == 3 and (pyxel.mouse_x >= 3 and pyxel.mouse_x <= 58) and (pyxel.mouse_y >= 33 and pyxel.mouse_y <= 61):
                
                    self.sofa = True 
                    
            if self.sala_atual == 3 and (pyxel.mouse_x >= 10 and pyxel.mouse_x <= 50) and (pyxel.mouse_y >= 69 and pyxel.mouse_y <= 87):
                
                    self.tapete = True 
                    
            if self.sala_atual == 3 and (pyxel.mouse_x >= 32 and pyxel.mouse_x <= 38) and (pyxel.mouse_y >= 19 and pyxel.mouse_y <= 23): 
                
                self.Vcogumelo = True
                
            if self.sala_atual == 3 and (pyxel.mouse_x >= 31 and pyxel.mouse_x <= 39) and (pyxel.mouse_y >= 16 and pyxel.mouse_y <= 18): 
                
                self.Vcogumelo = True  
            
            #Corredor
            if self.sala_atual == 0 and (pyxel.mouse_x >= 119 and pyxel.mouse_x <= 137) and (pyxel.mouse_y >= 32 and pyxel.mouse_y <= 49):
                
                    self.qdc = True 
 
 #--------------------------------------------------------------------------------#
                
        #Limites de Tela
        
        if self.heroi.x1 < 0:
            self.heroi.x1 = 0
            
        if self.heroi.x2 > 136:
            self.heroi.x1 = 136 - self.heroi.largura
        
        
        if self.sala_atual in [1 , 2, 3]:
            tamanho_dos_pisos = 48
        else:
            tamanho_dos_pisos = 58
            
        if self.heroi.y1 < tamanho_dos_pisos:
            self.heroi.y1 = tamanho_dos_pisos
        
        if self.heroi.y2 > 100:
            self.heroi.y1 = 100 - self.heroi.altura
        
            
        #Troca de sala ADC
        
        if self.sala_atual == 0:
            for porta in self.portas:
                if porta['x1'] <= self.heroi.x2 and self.heroi.x1 <= porta['x2']:
                    if porta['destino'] == 3 and self.heroi.y1 >= 75:
                        if pyxel.btnp(pyxel.KEY_E):
                            self.sala_atual = porta['destino']
                            self.carregar_cenario(porta['arquivo'])
                            self.heroi.x1 = porta['heroi_x']
                            self.heroi.y1 = porta['heroi_y']
                    elif porta['destino'] in [1, 2] and self.heroi.y1 <= 60:
                        if pyxel.btnp(pyxel.KEY_E):
                            self.sala_atual = porta['destino']
                            self.carregar_cenario(porta['arquivo'])
                            self.heroi.x1 = porta['heroi_x']
                            self.heroi.y1 = porta['heroi_y']
                            
        elif self.sala_atual == 2:
            if 16 <= self.heroi.x1 <= 47 and self.heroi.y1 <= 65 and pyxel.btnp(pyxel.KEY_E):
                self.sala_atual = 0
                self.carregar_cenario('corredor.pyxres')
                self.heroi.x1 = 85
                self.heroi.y1 = 65
            elif self.heroi.x1 <= 15 and self.heroi.y1 <= 73 and pyxel.btnp(pyxel.KEY_E):
                if self.dicas_total == 5:
                    self.sala_atual = 4
                    self.carregar_cenario('cofre.pyxres')
                        
                
        #Sair do cômodo
        elif self.sala_atual in [1, 3, 4]:
            origem = self.sala_atual
            pode_sair = False

            # Quarto
            if origem == 1 and self.heroi.x1 >= 80 and self.heroi.y1 <= 75:
                pode_sair = True

            #Escritório

            #Sala
            elif origem == 3 and self.heroi.x1 >= 80 and self.heroi.y1 <= 75:
                pode_sair = True

            if pode_sair and pyxel.btnp(pyxel.KEY_E):
            
                pode_sair = False
                self.sala_atual = 0
                self.carregar_cenario('corredor.pyxres')

                if origem == 1:       
                    self.heroi.x1 = 30
                    self.heroi.y1 = 65
                elif origem == 2:   
                    self.heroi.x1 = 85
                    self.heroi.y1 = 65
                elif origem == 3:     
                    self.heroi.x1 = 90
                    self.heroi.y1 = 78
            
            #Inicio e Finais
        if self.introducao:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.KEY_SPACE):
                if self.qual_texto < 4:  
                    self.qual_texto += 1
                else:
                    self.introducao = False
                    self.qual_texto = 0
                    
       # if self.texto == self.senha:
        #    self.win = True
         #   self.escolha = True
        if self.escolha:
            if pyxel.btnp(pyxel.KEY_1):
                self.escolha = False
                self.qual_final = 1
                self.qual_texto = 0
            elif pyxel.btnp(pyxel.KEY_2):
                self.escolha = False
                self.qual_final = 3
                self.qual_texto = 0
                
        if self.qual_final > 0:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_SPACE):
                if self.qual_texto < 3:
                    self.qual_texto += 1
                    
            
        
        self.heroi.definirBox()
        
#_________________________________________________________________________#          
                  
    def colisao(self,obj1,obj2):
        
        colisaoX = (obj2.x1 <= obj1.x1 and obj1.x1 <= obj2.x2) or (obj2.x1 <= obj1.x2 and obj1.x2 <= obj2.x2)
        colisaoY = (obj2.y1 <= obj1.y1 and obj1.y1 <= obj2.y2) or (obj2.y1 <= obj1.y2 and obj1.y2 <= obj2.y2)
        if colisaoX and colisaoY:
            return True
        else:
            return False
            
#_________________________________________________________________________#              
         
    def draw(self):
        pyxel.mouse(True)
        
        if self.introducao or self.escolha or self.qual_final > 0:
            self.inicio_e_finais()
            return
 
        if self.introducao or self.qual_final > 0:
            self.inicio_e_finais() 
        else:

            if self.sala_atual <= 4:
                pyxel.blt(0,0,0,0,0,136,100)
                if self.sala_atual != 4:
                    self.heroi.draw()
                    
        
            # Avisos na Tela:
            
            if self.sala_atual == 0:
                for porta in self.portas:
                    if porta['x1'] <= self.heroi.x2 and self.heroi.x1 <= porta['x2']:

                        if porta['destino'] == 1  and self.heroi.y1 <= 60:
                            pyxel.text(porta['x1'] - 7, 19, '[E] Entrar', 7)
                        elif porta['destino'] == 2  and self.heroi.y1 <= 60:
                            pyxel.text(porta['x1'] + 2 , 19, '[E] Entrar', 7)    
                        elif porta['destino'] == 3 and self.heroi.y1 >= 75:
                            pyxel.text(porta['x1'] - 4, 92, '[E] Entrar', 7)
                            
            if self.sala_atual == 2:
                if self.heroi.x1 <= 15 and self.heroi.y1 <= 70:
                    if self.dicas_total == 5:
                        pyxel.text(2, 19, '[E] Ver', 1)
                    else:
                        pyxel.text(2, 19, 'Indisponivel', 2)
                elif 10 <= self.heroi.x1 <= 50 and self.heroi.y1 <= 75:
                    pyxel.text(16, 18, '[E] Sair', 2)
                            
                            
            elif self.sala_atual in [1, 2, 3]:
                origem = self.sala_atual

                if origem == 1 and self.heroi.x1 >= 80 and self.heroi.y1 <= 75:
                    pyxel.text(103, 10, '[E] Sair', 1)
                elif origem == 2 and 10 <= self.heroi.x1 <= 50 and self.heroi.y1 <= 75:
                    pyxel.text(16, 18, '[E] Sair', 2)
                elif origem == 3 and self.heroi.x1 >= 72 and self.heroi.y1 <= 56:
                    pyxel.text(72, 12, '[E] Sair', 7)
            
            # Tela das Dicas e Nomes de Objetos
            
            #Dicas
            if self.sala_atual == 3 and self.dica1:
            
                pyxel.rect(118,90,18,15,0)
                pyxel.text(119,91,self.senha[0],7)
                if pyxel.btnp(pyxel.KEY_F):
                    self.dica1 = False
                    
            if self.sala_atual == 1 and self.dica2:
            
                pyxel.rect(118,90,18,15,0)
                pyxel.text(119,91,self.senha[1],7)
                if pyxel.btnp(pyxel.KEY_F):
                    self.dica2 = False
            
            if self.sala_atual == 2 and self.dica3:
            
                pyxel.rect(118,90,18,15,0)
                pyxel.text(119,91,self.senha[2],7)
                if pyxel.btnp(pyxel.KEY_F):
                    self.dica3 = False
            
            if self.sala_atual == 2 and self.dica4:
            
                pyxel.rect(118,90,18,15,0)
                pyxel.text(119,91,self.senha[3],7)
                if pyxel.btnp(pyxel.KEY_F):
                    self.dica4 = False
            
            if self.sala_atual == 0 and self.dica5:
            
                pyxel.rect(110,90,26,15,0)
                senha_errada = self.senha[3] + self.senha[2] + self.senha[0] + self.senha[1]
                pyxel.text(119,91,senha_errada,7)
                if pyxel.btnp(pyxel.KEY_F):
                    self.dica5 = False         
            
            #Outros
            if self.livro_vermelho and self.sala_atual == 3:
             
                pyxel.rect(75, 91, 60, 7, 0)
                pyxel.text(78,92,'Albúm de Fotos',7)   
                if pyxel.btnp(pyxel.KEY_F):
                    self.livro_vermelho = False
                    
            if self.livro_verde and self.sala_atual == 3:
             
                pyxel.rect(75, 91, 60, 7, 0)
                pyxel.text(78,92,'Nome da Planta',7)   
                if pyxel.btnp(pyxel.KEY_F):
                    self.livro_verde = False
                    
            if self.livro_amarelo and self.sala_atual == 3:
             
                pyxel.rect(75, 91, 60, 7, 0)
                pyxel.text(78,92,'Livro Infantil',7)   
                if pyxel.btnp(pyxel.KEY_F):
                    self.livro_amarelo = False
                    
            if self.sala_atual == 3 and self.quadro:
           
                pyxel.rect(95,90,60,15,0)
                pyxel.text(96,91,'22/02/2007',7)
                if pyxel.btnp(pyxel.KEY_F):
                    self.quadro = False
                    
            if self.sala_atual == 3 and self.globo:
            
                pyxel.rect(95,90,60,15,0)
                pyxel.text(96,91,'Papai Noel',7)
                if pyxel.btnp(pyxel.KEY_F):
                    self.globo = False
                    
            if self.sala_atual == 3 and self.sofa:
            
                pyxel.rect(63,90,72,15,0)
                pyxel.text(64,91,'Poeira e Carrinhos',7)
                if pyxel.btnp(pyxel.KEY_F):
                    self.sofa = False
                    
            if self.sala_atual == 3 and self.tapete:
            
                pyxel.rect(113,90,60,15,0)
                pyxel.text(114,91,'Areia',7)
                if pyxel.btnp(pyxel.KEY_F):
                    self.tapete = False
                    
            if self.sala_atual == 0 and self.qdc:
            
                pyxel.rect(87,90,60,15,0)
                pyxel.text(88,91,'Relogio Fofo',7) 
                if pyxel.btnp(pyxel.KEY_F):
                    self.qdc = False
                    
            if self.sala_atual == 3 and self.Vcogumelo:
            
                pyxel.rect(68,90,70,15,0)
                pyxel.text(69,91,'Cogumelo Venenoso',7) 
                if pyxel.btnp(pyxel.KEY_F):
                    self.Vcogumelo = False
           
           
            #Cofre
            
            if self.sala_atual == 4 and not self.win and self.n_tentativas <= 5:
                
                pyxel.rect(100, 22, 24, 12, 7)
                pyxel.text(104, 25, self.texto + "|", 4)
                    
                if self.t <= 4:
                    if pyxel.input_text and pyxel.input_text.isdigit():
                        self.texto += pyxel.input_text
                        self.t += 1
                    
                if self.t == 5:
                    self.t = 1
                    if self.texto == self.senha:
                        self.win = True
                        self.escolha = True
                        
                    i = 0
                    while i < 4 and not self.win:    
                        if self.texto[i] in self.senha and self.texto[i] != self.senha[i]:
                            pass
                            
                        if self.texto[i] == self.senha[i]:
                            pass
                            
                        if not (self.texto[i] in self.senha):
                            pass
                            
                        i += 1
                        
                    self.texto = ''
                    self.n_tentativas += 1

                    if not self.win and self.n_tentativas == 6:
                        self.qual_final = 2
                        self.qual_texto = 0
                        self.n_tentativas = 10
                        
            
           
#_________________________________________________________________________#  

    def carregar_cenario(self,arquivo):
        pyxel.load(arquivo)
        pyxel.images[1].load(0, 0, 'personagem_56x72.png')
            
#_________________________________________________________________________#  

    def posicao_valida(self, x, y):
        # Pés
        pes_x1 = x + 2
        pes_x2 = x + self.heroi.largura - 2
        pes_y1 = y + 12
        pes_y2 = y + self.heroi.altura

        #--------------Quarto--------------#
        if self.sala_atual == 1:
            #mesa de cabeceira esquerda
            if (pes_x2 >= 11 and pes_x1 <= 28) and (pes_y1 <= 66):
                return False
                
            #mesa de cabeceira direita
            if (pes_x2 >= 85 and pes_x1 <= 101) and (pes_y1 <= 66):
                return False
                
            #cama
            if (pes_x2 >= 28 and pes_x1 <= 84) and (pes_y1 <= 73):
                return False
                
            #bau da cama
            if (pes_x2 >= 41 and pes_x1 <= 70) and (pes_y1 <= 77):
                return False

        #-------------Escritório-------------#
        if self.sala_atual == 2:
            #mesa e cadeira
            if (pes_x2 >= 58 and pes_x1 <= 140) and (pes_y1 <= 68):
                return False
                
            #ESCADA
                
            if (pes_x2 >= 12 and pes_x1 <= 32) and (pes_y1 > 93):
                self.subir = True
                self.descer = False
                
            if (pes_x2 >= 12 and pes_x1 <= 32) and (pes_y1 > 82 and pes_y2 <= 84):
                self.subir = False
                self.descer = True
                
            if (pes_x1 == 32) and (pes_y1 > 93) and self.subir:
                self.subir = False
                self.descer = False
                
            if (pes_x2 >= 12 and pes_x1 <= 32) and (pes_y1 < 80) and self.subir:
                return False
                  
            if (pes_x2 >= 12 and pes_x1 <= 32) and (pes_y1 >= 78 and pes_y1 <= 93) and self.subir is False and self.descer is False:
                return False
                
            #Armário
            if (pes_x2 >= 0 and pes_x1 <= 10) and (pes_y1 >= 17):
                return False

        #----------------Sala----------------#
        if self.sala_atual == 3:
            #sofá
            if (pes_x2 >= 0 and pes_x1 <= 55) and (pes_y1 <= 63):
                return False
        

        return True
        
#_________________________________________________________________________#   

    def inicio_e_finais(self):
    
        #Introdução
        if self.introducao:
            pyxel.cls(0)
            pyxel.rect(4, 15, 128, 58, 7)
            if self.qual_texto == 0:
                pyxel.text(10, 22, "Voce brigou com", 0)
                pyxel.text(10, 31, "seus pais porque acha que", 0)
                pyxel.text(10, 40, "eles nao o amam mais...", 0)
                pyxel.text(12, 80, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 1:
                pyxel.text(10, 22, "Eles passam muito tempo", 0)
                pyxel.text(10, 31, "trabalhando e o deixam", 0)
                pyxel.text(10, 40, "de lado.", 0)
                pyxel.text(12, 80, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 2:
                pyxel.text(10, 22, "Voce lembra que guardaram", 0)
                pyxel.text(10, 31, "um documento importante", 0)
                pyxel.text(10, 40, "dentro de um cofre.", 0)
                pyxel.text(12, 80, '[Clique Para Avancar]', 6)   
            elif self.qual_texto == 3:
                pyxel.text(10, 22, "Voce quer achar", 0)
                pyxel.text(10, 31, "a senha para rasgar os", 0)
                pyxel.text(10, 40,  "documentos e se vingar!", 0)
                pyxel.text(12, 80, '[Clique Para Avancar]', 6)   
            elif self.qual_texto == 4:
                pyxel.text(10, 22, "Encontre as dicas pela", 0)
                pyxel.text(10, 31, "casa e descubra a senha.", 0)
                pyxel.text(12, 80, '[clique Para Jogar]', 10)
                
       #Escolhas
        if self.escolha:
            pyxel.cls(0)
            pyxel.rect(4, 15,128,58,7)
            pyxel.text(10,22,'Tens os Documentos nas maos.',0)
            pyxel.text(10,31,'O que vais fazer?', 0)
            pyxel.text(10,45,'[1] Rasgar os Documentos',3)
            pyxel.text(10,54,'[2] Nao rasgar',3)   
                
      # Finais
        if self.qual_final == 1:
            pyxel.cls(0)
            pyxel.rect(4, 15, 128, 58, 7)
            if self.qual_texto == 0:
                pyxel.text(10, 22, "Sem os documentos, a", 0)
                pyxel.text(10, 31, "empresa perdeu o contrato", 0)
                pyxel.text(10, 40, "e processou seus pais.", 0)
                pyxel.text(12, 80, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 1:
                pyxel.text(10, 22, "A pressao e as dividas", 0)
                pyxel.text(10, 31, "foram grandes demais", 0)
                pyxel.text(10, 40, "para a familia suportar.", 0)
                pyxel.text(12, 80, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 2:
                pyxel.text(10, 22, "A casa foi vendida e a", 0)
                pyxel.text(10, 31, "rotina que voce conhecia", 0)
                pyxel.text(10, 40, "acabou para sempre.", 0)
                pyxel.text(12, 80, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 3:
                pyxel.text(10, 22, "Sua raiva destruiu", 0)
                pyxel.text(10, 31, "a vida de quem mais te", 0)
                pyxel.text(10, 40, "amava.", 0)
                pyxel.text(12, 80, '[Fim]', 10)
                
        elif self.qual_final == 2:
            pyxel.cls(0)
            pyxel.rect(4, 12, 128, 76, 7)
            if self.qual_texto == 0:
                pyxel.text(8, 16, "Voce digitou o codigo errado.", 0)
                pyxel.text(8, 25, "Luzes vermelhas estao piscando.", 0)
                pyxel.text(8, 34, "e um alarme ensurdecedor ecoa.", 0)
                pyxel.text(8, 43, "Seus pais chegam com a policia.", 0)
                pyxel.text(8, 52, "Sua mae te abraca assustada", 0)
                pyxel.text(8, 61, "achando que foi invasao.", 0)
                pyxel.text(12, 82, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 1:
                pyxel.text(8, 16, "Ficas em silencio, tremendo", 0)
                pyxel.text(8, 25, "de culpa. O policial analiza", 0)
                pyxel.text(8, 34, "as cameras e diz serio:", 0)
                pyxel.text(8, 43, "- Nao houve invasao.", 0)
                pyxel.text(8, 52, "Foi o filho de voces.", 0)
                pyxel.text(12, 82, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 2:
                pyxel.text(8, 16, "O abraco da sua mae se", 0)
                pyxel.text(8, 25, "desfaz. O olhar de pavor", 0)
                pyxel.text(8, 34, "vira um silencio profundo.", 0)
                pyxel.text(8, 43, "Devido às suas intenções de ,", 0)
                pyxel.text(8, 52, "roubo,as autoridades intervêm.", 0)
                pyxel.text(12, 82, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 3:
                pyxel.text(8, 16, "Enquanto a viatura te leva,", 0)
                pyxel.text(8, 25, " Voce ve seus pais chorando", 0)
                pyxel.text(8, 34, "no portao.", 0)
                pyxel.text(8, 43, "Eles nao estavam bravos,", 0)
                pyxel.text(8, 52, "mas de coracao partido.", 0)
                pyxel.text(12, 82, '[Fim!]', 10)
                
        elif self.qual_final == 3:
            pyxel.cls(0)
            pyxel.rect(4, 12, 128, 76, 7)
            if self.qual_texto == 0:
                pyxel.text(8, 16, "Voce abre o cofre, mas decide", 0)
                pyxel.text(8, 25, "nao rasgar os documentos.", 0)
                pyxel.text(8, 34, "Seus pais chegam a casa e", 0)
                pyxel.text(8, 43, "trazem o teu bolo favorito!", 0)
                pyxel.text(8, 52, "Pedem desculpas por terem", 0)
                pyxel.text(8, 61, "te deixado de lado...", 0)
                pyxel.text(12, 82, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 1:
                pyxel.text(8, 16, "Eles entregam os papeis", 0)
                pyxel.text(8, 25, "importantes a tempo,", 0)
                pyxel.text(8, 34, "recebem uma promocao", 0)
                pyxel.text(8, 43, "e passam a dedicar mais", 0)
                pyxel.text(8, 52, "tempo para brincar com voce.", 0)
                pyxel.text(12, 82, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 2:
                pyxel.text(8, 16, "Nem todos os sentimentos", 0)
                pyxel.text(8, 25, "sao ditos em palavras...", 0)
                pyxel.text(8, 34, "O amor esta escondido", 0)
                pyxel.text(8, 43, "nos cuidados do dia-a-dia.", 0)
                pyxel.text(12, 82, '[Clique Para Avancar]', 6)
            elif self.qual_texto == 3:
                pyxel.text(8, 16, "Você abriu o cofre, mas", 0)
                pyxel.text(8, 25, "decidiste nao fechar", 0)
                pyxel.text(8, 34, "o coracao. A raiva passou", 0)
                pyxel.text(8, 43, "e a sua familia continua", 0)
                pyxel.text(8, 52, "aqui.", 0)
                pyxel.text(12, 82, '[Fim]', 10)
                
             
#__________________________________________________________________#    
Jogo()
