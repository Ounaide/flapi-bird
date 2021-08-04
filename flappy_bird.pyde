from random import randint

w=600
h=800

def setup():
    size(w,h)

#movement constants
speed = 0
gravity = 0.3

class bird:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        
    def show(self):       
        if self.r > 0: #draw only if game is not over
            stroke(0)
            fill(255,255,0)
            ellipse(self.x,self.y,self.r,self.r) #draw the body
            noFill()
            beginShape() #draw the wing
            vertex(self.x,self.y+5)
            vertex(self.x-5,self.y+5)
            vertex(self.x,self.y)
            endShape()
            fill(255)
            ellipse(self.x+5,self.y-5,5,5) #draw the eye
            fill(0)
            strokeWeight(1)
            ellipse(self.x+5,self.y-5,1,1) #draw the pupil
            fill(255,0,50)
            ellipse(self.x+7,self.y+2,0.5*self.r,0.25*self.r) #draw the mouth
        
        
    def update(self):
        global speed
        global gravity
        if self.y<(h-20): #move the bird
            self.y += speed
            speed += gravity 
            speed *= 0.95
        else:
            speed=0
        if self.y<=50: #stop the bird from going above the window
            self.y=50

class pipe:
    def __init__(self,x,top,bottom):
        self.x = x
        self.top = top
        self.bottom = bottom
        self.gap = (top-bottom)
        if self.gap < 100: #resize the gaps so they are not ridiculously big or small
            self.top-=50
            self.bottom -=50
        if self.gap > 400:
            self.top += 100
            self.bottom += 100

        
    def show(self): #draw both parts of the pipe
        stroke(0)
        fill(0,255,100)
        rect(self.x,0,40,self.top)
        fill(0,255,100)
        rect(self.x,h,40,-self.bottom)
    
    def update(self): #move the pipe to the left
        self.x-=1
    


        

        
def gameover(bird): #destroy the bird and the pipes
    global pipes
    if bird.r!=0:
        print("game over")
        bird.r=0
        pipes=[]


        

b = bird(0.25*w, h//2,20)
pipes=[]

for _ in range(5): #establish the first pipes to start the loop
    p = pipe(randint(0.75*w,1.5*w),random(100,h//2),random(100,h//2))
    pipes.append(p)
    currentPipe=pipes[0]
    
def stretch(pipes): #make sure the pipes are not too close to each other
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
    if b.r>0: #display the score in the top left if not gameover
        textSize(25)
        fill(255)
        text(str(score),15,25)
    else:  #display the final score 
        textSize(50)
        fill(255,0,0)
        textAlign(CENTER)
        text("Score:\n"+str(score), w//2,h//2)
        
    b.show()
    b.update()
    stretch(pipes)
    
 
    if b.y>=h-30: #bird dies if it touches the ground
        gameover(b)
        
    for p in pipes: #display and move all pipes
        global currentPipe
        p.show()
        p.update()
        if p.x<b.x: #remove the pipe if succesfully gone through and create a new one
            pipes.remove(p)
            pipes.append(pipe(randint(0.75*w,1.5*w),random(100,h//2),random(100,h//2)))
            score+=1
            currentPipe=pipes[0]

    if b.x >= currentPipe.x-20: #check for collision between the bird and the closest pipe
        if b.y<currentPipe.top or b.y>h-currentPipe.bottom:
            gameover(b)

    if keyPressed: 
        if key == " ": #use the spacebar to jump
            b.y-=20 

    
