import pyxel
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
        
        # Coisas
        self.heroi = Personagem(90,65,14,18,7,'meleca')
        self.dica1 = False
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
        
        
        self.portas = [
    # P1: Quarto
    {'x1': 20, 'x2': 45, 'destino': 1, 'arquivo': 'quarto.pyxres', 'heroi_x': 90, 'heroi_y': 65},
    # P2: Escritório
    {"x1": 75, "x2": 100, "destino": 2, "arquivo": "escritorio.pyxres", "heroi_x": 90, "heroi_y": 65},
    # P3: Sala
    {"x1": 79, 'x2': 112,'destino': 3, 'arquivo': 'sala.pyxres', 'heroi_x':  90,
 "heroi_y": 65},
    #Cofre
    {"x1": 0, 'x2': 10,'destino': 4, 'arquivo': 'azul.pyxres', 'heroi_x':  20,
 "heroi_y": 69}
]
        
        #Carregar imagem
     
        pyxel.load("sala.pyxres")      
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
        
        #Interação com os Objetos
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        
            if pyxel.mouse_x == 44 and (pyxel.mouse_y >= 10 and pyxel.mouse_y <= 22):
            
                self.dica1 = True
                
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
                    
            if self.sala_atual == 0 and (pyxel.mouse_x >= 119 and pyxel.mouse_x <= 137) and (pyxel.mouse_y >= 32 and pyxel.mouse_y <= 49):
                
                    self.qdc = True 
                
                
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
                            
        if self.sala_atual == 2:
            for porta in self.portas:
                if porta['destino'] == 4 and self.heroi.y1 <= 73:
                    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                        self.sala_atual = porta['destino']
                        self.carregar_cenario(porta['arquivo'])
                        self.heroi.x1 = porta['heroi_x']
                        self.heroi.y1 = porta['heroi_y']
                        
                        
        #Sair do cômodo
        elif self.sala_atual in [1, 2, 3, 4]:
            origem = self.sala_atual
            pode_sair = False

            # Quarto
            if origem == 1 and self.heroi.x1 >= 80 and self.heroi.y1 <= 75:
                pode_sair = True

            #Escritório
            elif origem == 2 and 10 <= self.heroi.x1 <= 50 and self.heroi.y1 <= 75:
                pode_sair = True

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
        pyxel.cls(0)
        pyxel.blt(0,0,0,0,0,136,100)
        self.heroi.draw()
        pyxel.mouse(True)
        
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
                        
        elif self.sala_atual in [1, 2, 3]:
            origem = self.sala_atual

            if origem == 1 and self.heroi.x1 >= 80 and self.heroi.y1 <= 75:
                pyxel.text(103, 10, '[E] Sair', 1)
            elif origem == 2 and 10 <= self.heroi.x1 <= 50 and self.heroi.y1 <= 75:
                pyxel.text(16, 18, '[E] Sair', 2)
            elif origem == 3 and self.heroi.x1 >= 72 and self.heroi.y1 <= 56:
                pyxel.text(72, 12, '[E] Sair', 7)
        
        # Tela das dicas
        
        if self.sala_atual == 3 and self.dica1:
        
            pyxel.rect(118,90,18,15,0)
            pyxel.text(119,91,'Dica',7)
            if pyxel.btnp(pyxel.KEY_F):
                self.dica1 = False
             
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

    
Jogo()


