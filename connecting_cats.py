import pgzrun
from random import randint
from time import time

width = 800
height = 600
cats = []
lines = []
starttime = 0
endtime = 0
totaltime = 0
num_cats = 10
next_cat = 0

def create_cat():
    global starttime
    for i in range(num_cats):
        cat = Actor("catcat") #image won't work (idk y)
        cat.pos = randint(40,width - 40),randint(40,height - 40) #random integer given inside the box
        cats.append(cat)
    starttime = time()

def draw():
    global totaltime
    screen.blit("bg",(0,0))
    num = 1
    for cat in cats:
        screen.draw.text(str(num),(cat.pos[0],cat.pos[1]+20)) 
        cat.draw()
        num = num+1
    for line in lines:
        screen.draw.line(line[0],line[1],(0,0,0))
    if next_cat <num_cats:
        totaltime = time() - starttime
        screen.draw.text(str(round (totaltime,1)),(10,10),fontsize = 30)
    else:
        screen.draw.text(str(round (totaltime,1)),(10,10),fontsize = 30)

def on_mouse_down(pos):
    global next_cat,lines
    if next_cat <num_cats:
        if cats [next_cat].collidepoint(pos):
            if next_cat:
                lines.append((cats[next_cat - 1].pos,cats[next_cat].pos))
                print(lines)
            next_cat += 1
    else:
        lines=[]
        next_cat = 0
create_cat()

pgzrun.go()