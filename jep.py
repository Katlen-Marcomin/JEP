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
        
#'--------------------------------------------------------------------------'#    
        
    def definirBox(self):
        self.x2 = self.x1 + abs(self.largura)
        self.y2 = self.y1 + abs(self.altura)
        
#'---------------------------------------------------------------------------'#        
    
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
  
#'------------------------------------------------------------------------'#  
  
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
            
#------------------------------------------------------------------#                  

class Jogo:
    def __init__(self):
        pyxel.init(136,100,"JEP")
        
        # Coisas
        self.heroi = Personagem(90,65,14,18,7,'meleca')
        self.dica1 = False
        self.dica2 = False
        self.dica3 = False
        self.dica4 = False
        self.sala_atual = 3
        
        self.portas = [
    # P1: Quarto
    {'x1': 20, 'x2': 45, 'destino': 1, 'arquivo': 'quarto.pyxres', 'heroi_x': 90, 'heroi_y': 65},
    # P2: Escritório
    {"x1": 75, "x2": 100, "destino": 2, "arquivo": "escritorio.pyxres", "heroi_x": 90, "heroi_y": 65},
    # P3: Sala
    {"x1": 79, 'x2': 112,'destino': 3, 'arquivo': 'sala.pyxres', 'heroi_x':  90, "heroi_y": 65}
]
        
        #Carregar imagem
     
        pyxel.load("sala.pyxres")      
        pyxel.images[1].load(0, 0, "personagem_56x72.png") 
        pyxel.run(self.update,self.draw)
    
#'------------------------------------------------------------------'#    
    
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
        obj.mover(dx,dy)

#'-------------------------------------------------------------------------'#

    def update(self):
    
        self.mover(self.heroi  ,pyxel.KEY_W,pyxel.KEY_S,pyxel.KEY_A,pyxel.KEY_D)
        
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        
            if pyxel.mouse_x == 44 and (pyxel.mouse_y >= 10 and pyxel.mouse_y <= 22):
            
                self.dica1 = True
                
        #Limites de Tela
        
        if self.heroi.x1 < 0:
            self.heroi.x1 = 0
            
        if self.heroi.x2 > 136:
            self.heroi.x1 = 136 - self.heroi.largura
            
        if self.heroi.y1 <58:
            self.heroi.y1 = 58
        
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
                        
        #Sair do cômodo
        elif self.sala_atual in [1, 2, 3]:
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
        
#'----------------------------------------------------------------------------'#        
                  
    def colisao(self,obj1,obj2):
        
        colisaoX = (obj2.x1 <= obj1.x1 and obj1.x1 <= obj2.x2) or (obj2.x1 <= obj1.x2 and obj1.x2 <= obj2.x2)
        colisaoY = (obj2.y1 <= obj1.y1 and obj1.y1 <= obj2.y2) or (obj2.y1 <= obj1.y2 and obj1.y2 <= obj2.y2)
        if colisaoX and colisaoY:
            return True
        else:
            return False
            
#'------------------------------------------------------------------------'#            
            
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0,0,0,0,0,136,100)
        self.heroi.draw()
        pyxel.mouse(True)
        
        # Avisos na Tela:
        
        if self.sala_atual == 0:
            for porta in self.portas:
                if porta['x1'] <= self.heroi.x2 and self.heroi.x1 <= porta['x2']:

                    if porta['destino'] in [1]  and self.heroi.y1 <= 60:
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
            elif origem == 3 and self.heroi.x1 >= 80 and self.heroi.y1 <= 75:
                pyxel.text(72, 12, '[E] Sair', 7)
        
        # tela das dicas
        
        if self.dica1:
        
            pyxel.rect(118,90,18,15,0)
            pyxel.text(119,91,'Dica',7)
            if pyxel.btnp(pyxel.KEY_F):
                self.dica1 = False
                
#----------------------------------------------------------------#

    def carregar_cenario(self,arquivo):
        pyxel.load(arquivo)
        pyxel.images[1].load(0, 0, 'personagem_56x72.png')
            
        
Jogo()




