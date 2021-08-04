from sys import exit
from random import randint

w=600
h=800

def setup():
    size(w,h)
    
speed = 0
gravity = 0.3

class bird:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r=r
        
    def show(self):       
        if self.r>0:
            stroke(0)
            fill(255,255,0)
            ellipse(self.x,self.y,self.r,self.r)
            noFill()
            beginShape()
            vertex(self.x,self.y+5)
            vertex(self.x-5,self.y+5)
            vertex(self.x,self.y)
            endShape()
            fill(255)
            ellipse(self.x+5,self.y-5,5,5)
            fill(0)
            strokeWeight(1)
            ellipse(self.x+5,self.y-5,1,1)
            fill(255,0,50)
            ellipse(self.x+7,self.y+2,0.5*self.r,0.25*self.r)
        
        
    def update(self):
        global speed
        global gravity
        if self.y<(h-20):
            self.y += speed
            speed+=gravity 
            speed*=0.95
        else:
            speed=0
        if self.y<=50:
            self.y=50

class pipe:
    def __init__(self,x,top,bottom):
        self.x = x
        self.top = top
        self.bottom = bottom
        self.gap = (top-bottom)
        if self.gap < 100:
            self.top-=50
            self.bottom -=50
        if self.gap>400:
            self.top+=50
            self.bottom+=50

        
    def show(self):
        stroke(0)
        fill(0,255,100)
        rect(self.x,0,40,self.top)
        fill(0,255,100)
        rect(self.x,h,40,-self.bottom)
    
    def update(self):
        self.x-=1
    


        

        
def gameover(bird):
    global pipes
    if bird.r!=0:
        print("game over")
        bird.r=0
        pipes=[]


        

b = bird(0.25*w, h//2,20)
pipes=[]

for _ in range(5):
    p = pipe(randint(0.75*w,1.5*w),random(100,h//2),random(100,h//2))
    pipes.append(p)
    currentPipe=pipes[0]
    
def stretch(pipes): 
    for _ in range(5):
        try:
            if pipes[_+1].x-pipes[_].x <100:
                pipes[_+1].x+=150
        except:
            pass


score=0
def draw():
    global pipes
    background(0,255,255)
    
    global score
    if b.r>0:
        textSize(25)
        fill(255)
        text(str(score),15,25)
    else:  
        textSize(50)
        fill(255,0,0)
        textAlign(CENTER)
        text("Score:\n"+str(score), w//2,h//2)
        
    b.show()
    b.update()
    stretch(pipes)
    
 
    if b.y>=h-50:
        gameover(b)
        
    for p in pipes:
        global currentPipe
        p.show()
        p.update()
        if p.x<b.x:
            pipes.remove(p)
            pipes.append(pipe(randint(0.75*w,1.5*w),random(100,h//2),random(100,h//2)))
            score+=1
            currentPipe=pipes[0]

    if b.x >= currentPipe.x-20:
        if b.y<currentPipe.top or b.y>h-currentPipe.bottom:
            gameover(b)

    if keyPressed:
        if key == " ":
            b.y-=20 





    
