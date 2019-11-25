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
    
    
    
    if current_location == "field":
        location_F()
        
    turtle.done()

def you():
    turtle.color('red')
    turtle.circle(10)
    
def location_FH():
    turtle.penup()
    turtle.goto(-275,190)
    turtle.pendown()
    you()
    
def location_F():
    turtle.penup()
    turtle.goto(-205,190)
    turtle.pendown()
    you()
    

def location_P():
    turtle.penup()
    turtle.goto(-130,190)
    turtle.pendown()
    you()

def location_C():
    turtle.penup()
    turtle.goto(-60,190)
    turtle.pendown()
    you()

def location_Ra():
    turtle.penup()
    turtle.goto(0,190)
    turtle.pendown()
    you()

def location_iR():
    turtle.penup()
    turtle.goto(70,190)
    turtle.pendown()
    you()

def location_BH():
    turtle.penup()
    turtle.goto(150,190)
    turtle.pendown()
    you()
def location_CW():
    turtle.penup()
    turtle.goto(220,190)
    turtle.pendown()
    you()
    
def location_ToZ():
    turtle.penup()
    turtle.goto(-275,130)
    turtle.pendown()
    you()

def location_SC():
    turtle.penup()
    turtle.goto(-205,130)
    turtle.pendown()
    you()

def location_tDW():
    turtle.penup()
    turtle.goto(-205,130)
    turtle.pendown()
    you()
    
def location_LT():
    turtle.penup()
    turtle.goto(-130,130)
    turtle.pendown()
    you()

def location_UT():
    turtle.penup()
    turtle.goto(-60,130)
    turtle.pendown()
    you()

def location_RwB():
    turtle.penup()
    turtle.goto(0,130)
    turtle.pendown()
    you()

def location_iRUB():
    turtle.penup()
    turtle.goto(70,130)
    turtle.pendown()
    you()

def location_MH():
    turtle.penup()
    turtle.goto(150,130)
    turtle.pendown()
    you()

def location_DW():
    turtle.penup()
    turtle.goto(220,130)
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
    turtle.goto(-275,10)
    turtle.pendown()
    you()

def location_DF():
    turtle.penup()
    turtle.goto(-205,10)
    turtle.pendown()
    you()
def location_GBH():
    turtle.penup()
    turtle.goto(-130,10)
    turtle.pendown()
    you()
def location_WwR():
    turtle.penup()
    turtle.goto(-60,10)
    turtle.pendown()
    you()
def location_BW():
    turtle.penup()
    turtle.goto(0,10)
    turtle.pendown()
    you()
def location_HC():
    turtle.penup()
    turtle.goto(-275,-50)
    turtle.pendown()
    you()
def location_GC():
    turtle.penup()
    turtle.goto(-205,-50)
    turtle.pendown()
    you()
def location_DC():
    turtle.penup()
    turtle.goto(-130,-50)
    turtle.pendown()
    you()
def location_MC():
    turtle.penup()
    turtle.goto(-60,-50)
    turtle.pendown()
    you()

