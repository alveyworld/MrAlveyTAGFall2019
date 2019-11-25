import turtle
# Setup the graphics window

def main(current_location):
    turtle.setup(800, 500,400, 400)
    turtle.title("Turtle Window")
    turtle.reset()
    turtle.speed(0)

    turtle.penup()
    turtle.goto(-300,200)
    turtle.pendown()

    for squaresInLayer in range(0,8):
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.penup()
         turtle.forward(20)
         turtle.pendown()   

    turtle.penup()
    turtle.goto(-300,150)
    turtle.pendown()

    for squaresInLayer in range(0,8):
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.penup()
         turtle.forward(20)
         turtle.pendown() 

    turtle.penup()
    turtle.goto(-300,100)
    turtle.pendown()

    for squaresInLayer in range(0,8):
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.penup()
         turtle.forward(20)
         turtle.pendown() 
    turtle.penup()
    turtle.goto(-300,50)
    turtle.pendown()

    for squaresInLayer in range(0,5):
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.penup()
         turtle.forward(20)
         turtle.pendown()
    turtle.penup()
    turtle.goto(-300,0)
    turtle.pendown()
    for squaresInLayer in range(0,4):
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.right(90)
         turtle.forward(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.penup()
         turtle.forward(20)
         turtle.pendown()
    
    if current_location == "farm house":
        location_FH()
    
    if current_location == "field":
        location_F()
        
    if current_location == "pasture":
        location_P()
    
    if current_location == "clearing":
        location_C()
   
    if current_location == "ravine":
        location_Ra()
        
    if current_location == "in ravine":
        location_iR()
        
    if current_location == "bullywags huts":
        location_BH()
        
    turtle.done()

def you():
    turtle.color('red')
    turtle.circle(10)
    
def location_FH():
    turtle.penup()
    turtle.goto(-275,175)
    turtle.pendown()
    you()
    
def location_F():
    turtle.penup()
    turtle.goto(-205,175)
    turtle.pendown()
    you()
    

def location_P():
    turtle.penup()
    turtle.goto(-130,175)
    turtle.pendown()
    you()

def location_C():
    turtle.penup()
    turtle.goto(-60,175)
    turtle.pendown()
    you()

def location_Ra():
    turtle.penup()
    turtle.goto(0,175)
    turtle.pendown()
    you()

def location_iR():
    turtle.penup()
    turtle.goto(70,175)
    turtle.pendown()
    you()

def location_BH():
    turtle.penup()
    turtle.goto(150,175)
    turtle.pendown()
    you()
def location_CW():
    turtle.penup()
    turtle.goto(220,175)
    turtle.pendown()
    you()
    
def location_ToZ():
    turtle.penup()
    turtle.goto(-275,120)
    turtle.pendown()
    you()

def location_SC():
    turtle.penup()
    turtle.goto(-205,120)
    turtle.pendown()
    you()

def location_tDW():
    turtle.penup()
    turtle.goto(-205,120)
    turtle.pendown()
    you()
    
def location_LT():
    turtle.penup()
    turtle.goto(-130,120)
    turtle.pendown()
    you()

def location_UT():
    turtle.penup()
    turtle.goto(-60,120)
    turtle.pendown()
    you()

def location_RwB():
    turtle.penup()
    turtle.goto(0,120)
    turtle.pendown()
    you()

def location_iRUB():
    turtle.penup()
    turtle.goto(70,120)
    turtle.pendown()
    you()

def location_MH():
    turtle.penup()
    turtle.goto(150,120)
    turtle.pendown()
    you()

def location_DW():
    turtle.penup()
    turtle.goto(220,120)
    turtle.pendown()
    you()
    
def location_BS():
    turtle.penup()
    turtle.goto(-275,70)
    turtle.pendown()
    you()
def location_Ri():
    turtle.penup()
    turtle.goto(-205,70)
    turtle.pendown()
    you()
def location_SC():
    turtle.penup()
    turtle.goto(-130,70)
    turtle.pendown()
    you()
def location_W():
    turtle.penup()
    turtle.goto(-60,70)
    turtle.pendown()
    you()
def location_C():
    turtle.penup()
    turtle.goto(0,70)
    turtle.pendown()
    you()
def location_WwC():
    turtle.penup()
    turtle.goto(70,70)
    turtle.pendown()
    you()
def location_SB():
    turtle.penup()
    turtle.goto(150,70)
    turtle.pendown()
    you()
def location_SW():
    turtle.penup()
    turtle.goto(220,70)
    turtle.pendown()
    you()

def location_OH():
    turtle.penup()
    turtle.goto(-275,20)
    turtle.pendown()
    you()

def location_DF():
    turtle.penup()
    turtle.goto(-205,20)
    turtle.pendown()
    you()
def location_GBH():
    turtle.penup()
    turtle.goto(-130,20)
    turtle.pendown()
    you()
def location_WwR():
    turtle.penup()
    turtle.goto(-60,20)
    turtle.pendown()
    you()
def location_BW():
    turtle.penup()
    turtle.goto(0,20)
    turtle.pendown()
    you()
def location_HC():
    turtle.penup()
    turtle.goto(-275,-30)
    turtle.pendown()
    you()
def location_GC():
    turtle.penup()
    turtle.goto(-205,-30)
    turtle.pendown()
    you()
def location_DC():
    turtle.penup()
    turtle.goto(-130,-30)
    turtle.pendown()
    you()
def location_MC():
    turtle.penup()
    turtle.goto(-60,-30)
    turtle.pendown()
    you()