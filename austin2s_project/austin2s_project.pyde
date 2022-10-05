Size = 500
keypressed = False
images = ["247810.png","987181.png","3083606.png","3401281.png","3530464.png","7408559.png"]
A = "247810.png"
B = "987181.png"
C = "3083606.png"
D = "3401281.png"
E = "3530464.png"
F = "7408559.png"
money = 10

 
def setup():
    size(500,500)  
    background(0,0,0)
                    
def draw():
    global A,B,C,D,E,F,keypressed,images
# Drawing the slot machine
    background(0,0,0)
    rect(100, 100, 300, 300, 7)
    fill(100,100,100)
    rect(100, 46, 300, 46, 7)
    fill (225,10,10)
    circle(40,200,80)
    rect(100, 220, 300, 60, 7)
    fill(115,23,23)
    stroke(225)
    line(40, 360, 40, 240)
    stroke(255)
    line(100, 360, 40, 360)
    stroke(255)
    line(40, 360, 40, 240)
    stroke(255)
    line(200, 400, 200, 100)
    stroke(255)
    line(300, 400, 300, 100)
    stroke(255)
    line(40, 360, 40, 240)
    stroke(255)
    textSize(52)
    text("$LOTS", 180,87)
    textSize(52)
    text("MONEY: " + str(money),0,40)
    # if keypressed == True:
    #   money -= 2
    #   keypressed = False
    
# Checks if the keypress(SPACE) is pressed it will pick 3 random numbers all attached to a variable that = an image 
    if keypressed == False:
        number = random(1,7)
        number = int(number)
        if number == 1:
            image (loadImage(A),125,225,50,50)
        elif number == 2:
            image (loadImage(B),125,225,50,50)
        elif number == 3:
            image (loadImage(C),125,225,50,50)
        elif number == 4:
            image (loadImage(D),125,225,50,50) 
        elif number == 5:
            image (loadImage(E),125,225,50,50)  
        elif number == 6:
            image (loadImage(F),125,225,50,50)
        else: image (loadImage(F),125,225,50,50)
        
        number = random(1,7)
        number = int(number)
        if number == 1:
            image (loadImage(A),225,225,50,50)
        elif number == 2:
            image (loadImage(B),225,225,50,50)
        elif number == 3:
            image (loadImage(C),225,225,50,50)
        elif number == 4:
            image (loadImage(D),225,225,50,50) 
        elif number == 5:
            image (loadImage(E),225,225,50,50)  
        elif number == 6:
            image (loadImage(F),225,225,50,50)
        else: image (loadImage(F),225,225,50,50)

        number = random(1,7)
        number = int(number)
        if number == 1:
            image (loadImage(A),325,225,50,50)
        elif number == 2:
            image (loadImage(B),325,225,50,50)
        elif number == 3:
            image (loadImage(C),325,225,50,50)
        elif number == 4:
            image (loadImage(D),325,225,50,50) 
        elif number == 5:
            image (loadImage(E),325,225,50,50)  
        elif number == 6:
            image (loadImage(F),325,225,50,50)
        else: image (loadImage(F),325,225,50,50)
    
        
        # function that tells the images to stop changing
def keyPressed():
    global keypressed,A,B,C,D,E,F,images
    if key == SPACE and keypressed == True:
        keypressed = False
    if key == SPACE and keypressed == False:
        keypressed = True
