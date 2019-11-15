# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
SILVER = (211, 211, 211)
LIGHTBLACK=(32,32,32)
GREY=(96,96,96)
YELLOW=(255,255,0)
L_GREY=(64,64,64)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
L_RED=(204,0,0)
BROWN2 = (153, 76, 0)
BLUE=(0,0,51)
W_BLUE=(51,153,255)
ORANGE=(204,102,0)
D_GREY = (105, 105, 105)
BLUE1 = (0, 0, 255)
BLUE2 = (25,25,112)
BLUE4 = (0,0,153)

# Define all the variables being used
h=0
v=0
u=0
x=0
y=0
q=0
w=0
c=0
d=0
s=0
a=0
b=0
xx=0
yy=0
count=10
p=1
z=0
n=0
w=0
m=0
r=0
t=0
e=0
u=0
l=0
f=0
movx=0
movy=0

ship = pygame.image.load('ship.bmp')
pygame.Surface.set_colorkey(ship, BLACK)

# Define all the images being used
nasa_logo=pygame.image.load("large_nasa_logo.png")
nasa_logo2=pygame.image.load("large_nasa_logo2.png")
flag=pygame.image.load("US_flagSmall.jpg")
astronaut=pygame.image.load("Astronaut.jpg")
flag_pole=pygame.image.load("american-flag-pole.png")
sky_background=pygame.image.load("sky.jpg")
space_background=pygame.image.load("sky_space.jpg")

# Set the height and width of the screen
size = [700, 550]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moon Exploration")
 
# Loop until the user clicks the close button.
done=False
countdown=True
ready_blast=False
rocket_up=False
rocket_space=False
rocket_down=False
astronaut_move=False

#STARFALL
stars=[]
for u in range(100):
    l=random.randrange(0,550)
    f=random.randrange(0,390)
    stars.append([l,f])
    
clock = pygame.time.Clock()

def station(h,v):
    screen.fill(W_BLUE)
    # Grass
    pygame.draw.rect(screen, GREEN, [0+h,390+v,800,380]) 
    # Building
    pygame.draw.ellipse(screen, LIGHTBLACK, [30+h,450+v,350,20])    
    pygame.draw.rect(screen, BROWN2, [50+h,280+v,290,180])
    pygame.draw.rect(screen, BROWN2, [72+h,140+v,250,150])
    screen.blit(nasa_logo, [140+h,160+v])
    # Windows
    pygame.draw.rect(screen, BLUE4, [75+h,330+v,30,70], 0)
    pygame.draw.polygon(screen, BLUE1, [[75+h,330+70+v],[75+30+h,330+v],[75+30+h,330+70+v]], 0)
    pygame.draw.rect(screen, BLUE4, [115+h,330+v,30,70], 0)
    pygame.draw.polygon(screen, BLUE1, [[115+h,330+70+v],[115+30+h,330+v],[115+30+h,330+70+v]], 0)
    pygame.draw.rect(screen, BLUE4, [155+h,330+v,30,70], 0)
    pygame.draw.polygon(screen, BLUE1, [[155+h,330+70+v],[155+30+h,330+v],[155+30+h,330+70+v]], 0)
    pygame.draw.rect(screen, BLUE4, [195+h,330+v,30,70], 0)
    pygame.draw.polygon(screen, BLUE1, [[195+h,330+70+v],[195+30+h,330+v],[195+30+h,330+70+v]], 0)
    pygame.draw.rect(screen, BLUE4, [235+h,330+v,30,70], 0)
    pygame.draw.polygon(screen, BLUE1, [[235+h,330+70+v],[235+30+h,330+v],[235+30+h,330+70+v]], 0)
    pygame.draw.rect(screen, BLUE4, [275+h,330+v,30,70], 0)    
    pygame.draw.polygon(screen, BLUE1, [[275+h,330+70+v],[275+30+h,330+v],[275+30+h,330+70+v]], 0)    
    # Stand for Rocket
    pygame.draw.ellipse(screen, LIGHTBLACK, [581+h,487+v,120,10])
    pygame.draw.line(screen, BLACK, [590+h, 490+v], [590+h, 150+v], 9)
    pygame.draw.line(screen, BLACK, [690+h, 490+v], [690+h, 150+v], 9)
    pygame.draw.line(screen, BLACK, [590+h, 150+v], [690+h, 150+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 220+v], [690+h, 150+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 150+v], [690+h, 220+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 220+v], [690+h, 290+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 290+v], [690+h, 220+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 360+v], [690+h, 290+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 290+v], [690+h, 360+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 360+v], [690+h, 430+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 430+v], [690+h, 360+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 430+v], [690+h, 490+v], 3)
    pygame.draw.line(screen, BLACK, [590+h, 490+v], [690+h, 430+v], 3)
    pygame.draw.line(screen, BLACK, [536+h, 270+v], [590+h, 270+v], 6)
    pygame.draw.line(screen, BLACK, [536+h, 330+v], [590+h, 330+v], 6)
    # Begin Module
    pygame.draw.rect(screen, BLACK, [10,10+b,680,530], 0)
    pygame.draw.rect(screen, GREY, [0,0+b,700,550], 4)
    font = pygame.font.SysFont('Cambria', 59, True, False)
    text = font.render("COUNTDOWN",True,WHITE)      
    screen.blit(text, [36, 300+b]) 
    screen.blit(nasa_logo2, [96,410+b])
    font = pygame.font.SysFont('Times New Roman', 38, True, False)
    text = font.render("MOON EXPLORATION",True,WHITE)      
    screen.blit(text, [250, 460+b])        
    
def cloud(c,d):
    # Clouds
    pygame.draw.ellipse(screen,WHITE,[300+c,90+d-50,160,90]) 
    pygame.draw.ellipse(screen,WHITE,[360+c,90+d-50,160,90]) 
    pygame.draw.ellipse(screen,WHITE,[420+c,90+d-50,160,90])      
    pygame.draw.ellipse(screen,WHITE,[80+c,50+d-50*6,160,100]) 
    pygame.draw.ellipse(screen,WHITE,[140+c,50+d-50*6,160,100]) 
    pygame.draw.ellipse(screen,WHITE,[200+c,50+d-50*6,160,100])    
    pygame.draw.ellipse(screen,WHITE,[300+c,90+d-50*12,160,90]) 
    pygame.draw.ellipse(screen,WHITE,[420+c,90+d-50*80,160,90])  
    pygame.draw.ellipse(screen,WHITE,[-60+c,150+d-50*100,160,90]) 
    pygame.draw.ellipse(screen,WHITE,[0+c,150+d-50*100,160,90]) 
    pygame.draw.ellipse(screen,WHITE,[60+c,150+d-50*100,160,90])             
    pygame.draw.ellipse(screen,WHITE,[80+c,50+d-50*60,160,100]) 
    pygame.draw.ellipse(screen,WHITE,[140+c,50+d-50*60,160,100]) 
    pygame.draw.ellipse(screen,WHITE,[360+c,90+d-50*12,160,90]) 
    pygame.draw.ellipse(screen,WHITE,[420+c,90+d-50*12,160,90])     
    pygame.draw.ellipse(screen,WHITE,[-60+c,150+d-50*20,160,90]) 
    pygame.draw.ellipse(screen,WHITE,[0+c,150+d-50*20,160,90]) 
    pygame.draw.ellipse(screen,WHITE,[200+c,50+d-50*60,160,100]) 
    
def rocket(xx,yy,h,v,a,b):
    # Rocket
    # Draws auxiliary tank
    pygame.draw.ellipse(screen, ORANGE, [448+xx+h+a, 170+yy+z+q, 64, 100])
    pygame.draw.rect(screen, ORANGE, [448+xx+h+a, 220+yy+z+q, 64, 170])
    pygame.draw.line(screen, WHITE, [448+xx+h+a, 230+yy+z+q], [511+xx+h+a, 230+yy+z+q], 3)
    pygame.draw.line(screen, WHITE, [448+xx+h+a, 250+yy+z+q], [511+xx+h+a, 250+yy+z+q], 3)
    pygame.draw.line(screen, WHITE, [448+xx+h+a, 270+yy+z+q], [511+xx+h+a, 270+yy+z+q], 3)
    pygame.draw.line(screen, WHITE, [448+xx+h+a, 290+yy+z+q], [511+xx+h+a, 290+yy+z+q], 3)
    # Draws first side rocket
    pygame.draw.ellipse(screen, WHITE, [423+xx+h+a,324+yy+z+q,24,10], 0)    
    pygame.draw.ellipse(screen, BLACK, [423+xx+h+a,324+yy+z+q,24,10], 2)    
    pygame.draw.ellipse(screen, WHITE, [423+xx+h+a,209+yy+z+q,24,60], 0)    
    pygame.draw.ellipse(screen, BLACK, [423+xx+h+a,209+yy+z+q,24,60], 2)    
    pygame.draw.rect(screen, BLACK, [423+xx+h+a,239+yy+z+q,24,170], 2)    
    pygame.draw.rect(screen, WHITE, [425+xx+h+a,239+yy+z+q,21,171], 0)
    pygame.draw.line(screen, BLACK, [423+xx+h+a,408+yy+z+q], [445+xx+h+a,408+yy+z+q], 2)
    pygame.draw.line(screen, BLACK, [423+xx+h+a,378+yy+z+q], [445+xx+h+a,378+yy+z+q], 2)
    pygame.draw.line(screen, BLACK, [423+xx+h+a,348+yy+z+q], [445+xx+h+a,348+yy+z+q], 2)
    pygame.draw.line(screen, BLACK, [423+xx+h+a,318+yy+z+q], [445+xx+h+a,318+yy+z+q], 2)
    pygame.draw.line(screen, BLACK, [423+xx+h+a,288+yy+z+q], [445+xx+h+a,288+yy+z+q], 2)
    pygame.draw.line(screen, BLACK, [423+xx+h+a,258+yy+z+q], [445+xx+h+a,258+yy+z+q], 2)
    pygame.draw.polygon(screen, GREY, [[420+xx+h+a, 420+yy+z+q], [425+xx+h+a, 410+yy+z+q], [445+xx+h+a, 410+yy+z+b], [450+xx+h+a, 420+yy+z+q]])
    # Draws second side rocket    
    pygame.draw.ellipse(screen,WHITE,[511+xx+h+a,324+yy+z+q,24,10],0)    
    pygame.draw.ellipse(screen,BLACK,[511+xx+h+a,324+yy+z+q,24,10],2)    
    pygame.draw.ellipse(screen,WHITE,[511+xx+h+a,209+yy+z+q,24,60],0)    
    pygame.draw.ellipse(screen,BLACK,[511+xx+h+a,209+yy+z+q,24,60],2)    
    pygame.draw.rect(screen,BLACK,[511+xx+h+a,239+yy+z+q,24,170],2)    
    pygame.draw.rect(screen,WHITE,[513+xx+h+a,239+yy+z+q,21,171],0)
    pygame.draw.line(screen,BLACK,[511+xx+h+a,408+yy+z+q],[533+xx+h+a,408+yy+v+q],2)
    pygame.draw.line(screen,BLACK,[511+xx+h+a,378+yy+z+q],[533+xx+h+a,378+yy+v+q],2)
    pygame.draw.line(screen,BLACK,[511+xx+h+a,348+yy+z+q],[533+xx+h+a,348+yy+z+q],2)
    pygame.draw.line(screen,BLACK,[511+xx+h+a,318+yy+z+q],[533+xx+h+a,318+yy+z+q],2)
    pygame.draw.line(screen,BLACK,[511+xx+h+a,288+yy+z+q],[533+xx+h+a,288+yy+z+q],2)
    pygame.draw.line(screen,BLACK,[511+xx+h+a,258+yy+z+q],[533+xx+h+a,258+yy+z+q],2)
    pygame.draw.polygon(screen,GREY,[[508+xx+h+a,420+yy+z+q],[513+xx+h+a,410+yy+z+q],[533+xx+h+a,410+yy+z+q],[538+xx+h+a,420+yy+z+q]])
    # Draws body for the rocket
    pygame.draw.ellipse(screen,SILVER,[462+xx+h+a,230+yy+z+q,37,80])
    pygame.draw.rect(screen,SILVER,[462+xx+h+a,270+yy+z+q,37,115])   
    pygame.draw.polygon(screen,SILVER,[[432+xx+h+a,330+yy+z+q],[432+xx+h+a,290+yy+z+q],[462+xx+h+a,270+yy+z+q],[462+xx+h+a,330+yy+z+q]])
    pygame.draw.polygon(screen,SILVER,[[528+xx+h+a,330+yy+z+q],[528+xx+h+a,290+yy+z+q],[498+xx+h+a,270+yy+z+q],[498+xx+h+a,330+yy+z+q]])
    pygame.draw.polygon(screen,D_GREY,[[425+xx+h+a,340+yy+z+q],[430+xx+h+a,330+yy+z+q],[460+xx+h+a,330+yy+z+q],[460+xx+h+a,340+yy+z+q]])
    pygame.draw.polygon(screen,D_GREY,[[535+xx+h+a,340+yy+z+q],[530+xx+h+a,330+yy+z+q],[500+xx+h+a,330+yy+z+q],[500+xx+h+a,340+yy+z+q]])
    pygame.draw.line(screen,D_GREY,[430+xx+h+a,295+yy+z+q],[460+xx+h+a,295+yy+z+q],3)
    pygame.draw.line(screen,D_GREY,[430+xx+h+a,305+yy+z+q],[460+xx+h+a,305+yy+z+q],3)
    pygame.draw.line(screen,D_GREY,[530+xx+h+a,295+yy+z+q],[500+xx+h+a,295+yy+z+q],3)
    pygame.draw.line(screen,D_GREY,[530+xx+h+a,305+yy+z+q],[500+xx+h+a,305+yy+z+q],3)
    pygame.draw.line(screen,LIGHTBLACK,[462+xx+h+a,270+yy+z+q],[462+xx+h+a,330+yy+z+q],2)
    pygame.draw.line(screen,LIGHTBLACK,[498+xx+h+a,270+yy+z+q],[498+xx+h+a,330+yy+z+q],2) 
    pygame.draw.polygon(screen,GREY,[[465+xx+h+a,395+yy+z+q],[470+xx+h+a,385+yy+z+q],[490+xx+h+a,385+yy+z+q],[495+xx+h+a,395+yy+z+q]])  
    screen.blit(flag,[464+xx+h+a,360+yy+z+q])
    
def fire(x,y,m,w,r,t):
    # Fire for the main rocket
    pygame.draw.ellipse(screen, RED, [465+x+m+r,370+y+w+t,30,70], 0)
    pygame.draw.ellipse(screen, YELLOW, [475+x+m+r,390+y+w+t,10,30], 0)
    # Fire for the first side rocket
    pygame.draw.ellipse(screen, RED, [425+x+m+r,413+y+w+t,20,30], 0)
    pygame.draw.ellipse(screen, YELLOW, [429+x+m+r,417+y+w+t,12,20], 0)
    # Fire for the second rocket
    pygame.draw.ellipse(screen, RED, [513+x+m+r,413+y+w+t,20,30], 0)
    pygame.draw.ellipse(screen, YELLOW, [517+x+m+r,417+y+w+t,12,20], 0)     
    
def moon():
    screen.fill(BLACK)
    # Surface
    pygame.draw.ellipse(screen,(164,164,164),(-200,190,600,30))
    pygame.draw.ellipse(screen,(164,164,164),(200,190,600,30))
    pygame.draw.ellipse(screen,(164,164,164),(700,180,400,60))
    pygame.draw.rect(screen,(164,164,164),(0,215,800,450))
    # Craters
    pygame.draw.ellipse(screen,(100,100,100),(100,415,250,100))
    pygame.draw.ellipse(screen,(100,100,100),(50,300,100,30))
    pygame.draw.ellipse(screen,(100,100,100),(130,210,50,10))
    pygame.draw.ellipse(screen,(100,100,100),(660,450,300,130))
    pygame.draw.ellipse(screen,(100,100,100),(400,300,150,40))
    pygame.draw.ellipse(screen,(100,100,100),(300,250,100,20))
    pygame.draw.ellipse(screen,(100,100,100),(650,250,75,15))
    #Stars Bright
    pygame.draw.rect(screen,(255,255,255),(100,100,2,2))
    pygame.draw.rect(screen,(255,255,255),(150,170,2,2))
    pygame.draw.rect(screen,(255,255,255),(260,60,2,2))
    pygame.draw.rect(screen,(255,255,255),(400,100,2,2))
    pygame.draw.rect(screen,(255,255,255),(450,130,2,2))
    pygame.draw.rect(screen,(255,255,255),(520,80,2,2))
    pygame.draw.rect(screen,(255,255,255),(590,180,2,2))
    pygame.draw.rect(screen,(255,255,255),(600,20,2,2))
    pygame.draw.rect(screen,(255,255,255),(690,130,2,2))
    # Stars Medium
    pygame.draw.rect(screen,(150,150,150),(10,60,2,2))
    pygame.draw.rect(screen,(150,150,150),(130,130,2,2))
    pygame.draw.rect(screen,(150,150,150),(190,50,2,2))
    pygame.draw.rect(screen,(150,150,150),(250,100,2,2))
    pygame.draw.rect(screen,(150,150,150),(270,160,2,2))
    pygame.draw.rect(screen,(150,150,150),(350,120,2,2))
    pygame.draw.rect(screen,(150,150,150),(500,70,2,2))
    pygame.draw.rect(screen,(150,150,150),(720,150,2,2))
    #Stars Dim
    pygame.draw.rect(screen,(70,70,70),(10,100,2,2))
    pygame.draw.rect(screen,(70,70,70),(120,20,2,2))
    pygame.draw.rect(screen,(70,70,70),(150,100,2,2))
    pygame.draw.rect(screen,(70,70,70),(220,170,2,2))
    pygame.draw.rect(screen,(70,70,70),(300,40,2,2))
    pygame.draw.rect(screen,(70,70,70),(350,70,2,2))
    pygame.draw.rect(screen,(70,70,70),(400,20,2,2))
    pygame.draw.rect(screen,(70,70,70),(600,110,2,2))
    pygame.draw.rect(screen,(70,70,70),(700,60,2,2))
    pygame.draw.rect(screen,(70,70,70),(760,80,2,2))     
    
# ---------------------------- Main Program Loop -------------------------------
while not done:
     
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
         
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True  # Flag that we are done so we exit this loop
            
    screen.fill(WHITE)
    
# Countdown for rocket
    if countdown:    
        if count>=0:
            station(h,v)
            rocket(xx,yy,h,v,a,q)    
            if count ==10:
                sound=pygame.mixer.Sound('countdown.wav')
                sound.play()                        
                count ==9
                count ==8
                count ==7                  
                count ==6
                count ==5
                count ==4
                count ==3                
                count==2
                count==1 
                pygame.mixer.music.load('sound2.wav')
                pygame.mixer.music.play()                
            if count==0:
                b=700
                countdown=False
                ready_blast=True     
# Text for beginning
            font = pygame.font.SysFont('Agency FB', 120, True, False)
            text = font.render(str(count),True,YELLOW)
# Count
            count=count-1
            clock.tick(1)
# Place Text
            screen.blit(text, [140, 150])
# Rocket ready to blast off and begins blast off
    if ready_blast: 
        station(h,v)
        cloud(c,d)
        fire(x,y,m,w,r,t)
        rocket(xx,yy,h,z,a,q)
        v+=20
        yy-=10
        y-=10
        d+=20
        b+=20
        if h>=1 or h<=-1:            
            h=2*(-1)
            s+=1
        if v>=4 or v<-1:
            p=p*(-1)
            s+=1
        if s>=75:
            blast_off=False
            rocket_up=True
            v=400
            yy=200
            y=200
            d=100000
            v=100000
            screen.fill(BLACK)
                 
# Rocket flies in the sky 
    if rocket_up:
        screen.blit(space_background,[0,-200+e])
        screen.blit(sky_background,[0,0+n])
        fire(x,y,m,w,r,t)
        rocket(xx,yy,h,z,a,q)
        z-=30
        w-=30
        n+=25
        e+=10           
        if e==680:
            yy=-200
            xx=50
            n=100000
            e=100000
            rocket_up=False
            rocket_down=True            
            
    if rocket_down:
       moon()
       pygame.display.update()
       rocket(xx,yy,h,z,a,q)
       for i in stars:
                   i[1]+=1
                   pygame.draw.circle(screen, WHITE, i,1)
                   if i [1]>390:
                       i[1]=random.randrange(-50, -5)
                       i[0]=random.randrange(550)        
                       for yy in range(-200,329,10): 
                           yy=yy+1
       for i in range(200):
           pygame.time.delay(50)
           moon()
           screen.blit(ship, [300, i])
           pygame.mixer.music.load('a13-privlege.wav')
           pygame.mixer.music.play()
           pygame.display.update()
           
       rocket_down=False
# --------------------------------PROGRAM ENDS---------------------------------
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()    
                
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
   