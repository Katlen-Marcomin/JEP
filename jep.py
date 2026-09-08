Quase sem espaço de armazenamento … Se você atingir o limite, não poderá criar, editar ou fazer upload de arquivos. Compre 30 GB por R$ 4,50 mensais.
100%
import pyxel
class Personagem:
    def __init__(self,x,y,largura,altura,cor,desenho):
        self.x1=x
        self.y1=y
        self.largura=largura
        self.altura=altura
        self.colSprites = 0
        self.linSprites = 0
        self.cor = cor
        self.passo = 0
        self.totalPassos = 2
        self.definirBox()
        self.desenho = desenho
    
        
    def definirBox(self):
        self.x2 = self.x1 + abs(self.largura)
        self.y2 = self.y1 + abs(self.altura)
    
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
        
    def draw(self):
    
        XImagem = self.largura * self.colSprites
        YImagem = self.altura * self.linSprites
        if self.desenho == 'meleca':
            pyxel.blt(self.x1, self.y1,             
                  0,                            
                  XImagem,YImagem,                        
                  self.largura, self.altura,    
                  self.cor)   
        else:
            pyxel.blt(self.x1, self.y1,             
                  1,                            
                  XImagem,YImagem,                        
                  self.largura, self.altura,    
                  self.cor)   
            
                  

class Jogo:
    def __init__(self):
        pyxel.init(120,100,"Colisao")
        # Atributos aqui
        self.heroi = Personagem(10,10,14,18,7,'meleca')
        #self.inimigo = Personagem(80,80,16,16,10,'gatinho')
        
        #Carregar imagem
       
        pyxel.load('meu_arquivo.pyxres')
        pyxel.images[0].load(0, 0, "personagem_56x72.png")
               
        pyxel.run(self.update,self.draw)
    
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
         
    def update(self):
        self.mover(self.heroi  ,pyxel.KEY_W,pyxel.KEY_S,pyxel.KEY_A,pyxel.KEY_D)
        #self.mover(self.inimigo,pyxel.KEY_W ,pyxel.KEY_S   ,pyxel.KEY_A   ,pyxel.KEY_D)
                  
    def colisao(self,obj1,obj2):
        
        colisaoX = (obj2.x1 <= obj1.x1 and obj1.x1 <= obj2.x2) or (obj2.x1 <= obj1.x2 and obj1.x2 <= obj2.x2)
        colisaoY = (obj2.y1 <= obj1.y1 and obj1.y1 <= obj2.y2) or (obj2.y1 <= obj1.y2 and obj1.y2 <= obj2.y2)
        if colisaoX and colisaoY:
            return True
        else:
            return False
            
            
        
   
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0,0,0,0,0,120,100)
        self.heroi.draw()
       # self.inimigo.draw()
Jogo()
