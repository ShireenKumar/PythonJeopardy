import pygame
import sys

pygame.init()
win = pygame.display.set_mode((1000, 1000))
win.fill((255, 255, 255))
font = pygame.font.SysFont("Arial",20)

win0 = pygame.display.set_mode((1000, 1000))
win0.fill((255, 255, 255))

points1 = 0
points2 = 0 
counter = 1

QandA = []

# Category 1: Disney
QandA.append(["Circle of _____", "Life"])
QandA.append(["Look for the _____ Necessities", "Bare"])
QandA.append(["Purple _____ He's got fifty-three", "Peacocks"])
QandA.append(["We are _____ if you don't", "Siamese"])

# Category 2: 80s Hits
QandA.append(["If only I could, I'd be _____ up that hill", "Running"])
QandA.append(["Never gonna _____ you up", "Give"])
QandA.append(["_____, are you okay?", "Annie"])
QandA.append(["You're _____ away, I'll be coming for you anyway", "Shying"])

# Category 3: 90s hits
QandA.append(["Hi! My name is, _____, Slim Shady", "Chika-chika"])
QandA.append(["Here we are now, _____ us", "Entertain"])
QandA.append(["And no, I don't want no _____", "Scrub"])
QandA.append(["_____ the world, _____ the world", "Around"])

# Category 4: Pop Songs of the 2010s
QandA.append(["But here's my _____, so call me, maybe", "Number"])
QandA.append(["I'm out the door, I'm gonna hit this _____", "City"])
QandA.append(["I know you get me, so I let my _____ come down", "Walls"])
QandA.append(["'Cause you think you're _____ than me", "Cooler"])

# Category 5: Pop Songs of the 2020s
QandA.append(["Ooooh I'm _____ by the lights", "Blinded"])
QandA.append(["Probably with that _____ girl", "Blonde"])
QandA.append(["_____ with me in the moment", "Keep"])
QandA.append(["You can see the world, following the _____", "Seasons"])


class Question:
    def __init__(self, question: str, answer: str, worth: int):
        self.question = question
        self.answer = answer
        self.worth = worth

    # this function checks an answer passsed as a parameter, returns True if it is correct, False if not
    def check(self,ans: str): 
        if ans == self.answer:
            return True
        else:
            return False
# Creating a class for the Buttons 
class Button:
    # Attributes for Button are listed here: 
    def __init__(self, color, x, y, width, height, text):
        # x and y are the coordinates of the button 
        self.x = x
        self.y = y
        # Width and height are the parameters of the rectangle/square button
        self.width = width
        self.height = height
        # Color of the button
        self.color = color
        #
        self.text = font.render(text,1,pygame.Color("Black"))
        # Surf represents the appearence of the object so when we are printing out the Button 
        # these peices of code put the width,height,text, and color together
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(self.color)
        self.surf.blit(self.text, (0, 0))
        # Question is the 
        self.question = ""
   
    #Created to make printing out buttons easier 
    def draw(self, win):
        #Takes in the surface and the x and y corrdinates 
        win.blit(self.surf, (self.x, self.y))

    # takes in the position of the mouse and checks if it's positions is within the dimensions of the button hence the x and y corrdinates 
    # as well as the width and the height, if the mouse is within the button it returns true if not false
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    # each question is assigned to a question number and set number sets a number for each button that has a question and answer
    def setNumber(self, k):
        self.number = k

    # This function adds value to the question attribute in the init function, it also takes in worth/points. 
    # QandA is a list with all our questions and answers to each button
    def addQuestion(self, worth: int):
        #Accounts for the categories which are always 0,5,10,15,20,and 25
        if self.number%5 == 0 or self.number == 0:
            self.question = ""
        # for the first column
        elif self.number > 0 and self.number < 5:
            self.question = Question(QandA[self.number-1][0], QandA[self.number-1][1], worth)
        # for the second column
        elif self.number > 5 and self.number < 10:
            self.question = Question(QandA[self.number-2][0], QandA[self.number-2][1], worth)
        # for the third column
        elif self.number > 10 and self.number < 15:
            self.question = Question(QandA[self.number-3][0], QandA[self.number-3][1], worth)
        # for the fourth column
        elif self.number > 15 and self.number < 20:
            self.question = Question(QandA[self.number-4][0], QandA[self.number-4][1], worth)
        # for the fifth column
        elif self.number > 20 and self.number < 25:
            self.question = Question(QandA[self.number-5][0], QandA[self.number-5][1], worth)

    # Made to change the color of a certain text to white 
    def fontBlack(self,text):
        self.text = font.render(text,1,pygame.Color("White"))
        self.surf.blit(self.text, (0, 0))

# This function allows us to make a button black when it is called
def drawblack(myButton):
    myButton.color = (0,0,0)
    myButton.surf.fill(myButton.color)
        
# This function redraws the button after every click so none of the other buttons disapear 
def redrawWindow(myButton):
    myButton.draw(win)

k = 0
l = 0
text2 = ""
# for loop for x and y to create the whole grid of buttons (start from 0, step = 50)
buttonl = []

for i in range(50, 600, 110):
    for j in range(50, 600, 110):
        text1 = ''
        # These if statements are 
        if j == 50:  
            text1 = 'Category ' 
        elif j== 160:
             text1 = '100'  
        elif j== 270:
             text1 = '200'
        elif j== 380:
             text1 = '300'
        elif j== 490:
             text1 = '400'
        myButton = Button((143,191,242), i, j, 100, 100, text1)
        if 'Category' in text1:
            drawblack(myButton)
            myButton.fontBlack('Category '+ str((j-(j-l))+1))
        myButton.number = k
        win.blit(myButton.surf, (i, j))
        buttonl.append(myButton)  
        redrawWindow(myButton)

        #win.blit(buttonl[k].surf, (i,j))
        k+=1
    l += 1

# Runs the game in a while loop which runs until the user quits the program or when run is false
run = True
while run:
    for a in buttonl:
        redrawWindow(a)

    pygame.display.update()
    
    # This allows the game to quit when you press the 'x' at the end of the screen
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        # This if statement accounts for the mouse clicking on the buttons to get the question
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks which button is being clicked
            for i in buttonl:
                # if that button is being clicked...
                if i.isOver(pos):
                    # turns that square black and redraws that button and updates the display
                    drawblack(i)
                    redrawWindow(i)
                    pygame.display.update()
                    #Assigns the points to each question 
                    if (i.number-1)%5 == 0:
                        selfworth = 100
                    elif (i.number-2)%5 == 0:
                        selfworth = 200
                    elif (i.number-3)%5 == 0:
                        selfworth = 300
                    elif (i.number-4)%5 == 0:
                        selfworth = 400
                    # If the button is the category then there will be no selfworth/no points 
                    elif (i.number)%5 == 0:
                        selfworth = 0

                    # if the button is a category button, then it will not add a question
                    cat = True
                    if selfworth != 0:
                        i.addQuestion(selfworth)
                        cat = False
                    else:
                        i.question = ""
                    
                    font = pygame.font.Font('freesansbold.ttf', 16)
                    
                    # changes the text that appears when a button is clicked (to avoid errors)
                    if not cat:
                        text = font.render(i.question.question, True, (0, 0, 0), (255,255,255))
                    else:
                        text = font.render("", True, (0, 0, 0), (255,255,255))
                    
                    # creates a rect behind the question to avoid overlap of the questions
                    pygame.draw.rect(win, (255, 255, 255), pygame.Rect(650, 100, 200, 200))
        
                    # creates a text rect of the question to display
                    textRect = text.get_rect(center = (800,200))
                    win.blit(text, textRect)
                    pygame.display.flip()

                    # creating the font, text, rect, and color for the input box
                    base_font = pygame.font.Font(None, 24)
                    user_text = ""
                    input_rect = pygame.Rect(50, 600, 140, 32)
                    color = pygame.Color('blue')
                    
                    #This while loop is for the player to input their answer
                    run2 = True
                    while run2 == True:    
                        for event in pygame.event.get():      
                            #When the mouse is clicked then the it lets the player input their answer      
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if input_rect.collidepoint(event.pos):
                                    run2 = True
                                else:
                                    run2 = False
                            # when a key is pressed...
                            if event.type == pygame.KEYDOWN:
                                #check for backspace
                                if event.key == pygame.K_BACKSPACE:
                                    user_text = user_text[:-1]
                                # otherwise, adds together a string of all the keys that which the user has entered (unicode)
                                else:
                                    user_text += event.unicode
                            
                            # when the user clicks on the input box, it will turn a lighter color
                            if run2:
                                color = pygame.Color((178, 221, 244))
                            else:
                                color = pygame.Color((103, 191, 237))

                            # creates a rect and draws it
                            pygame.draw.rect(win, color, input_rect)
                            # creates a text surface by rendering the font using the user's inputted text
                            text_surface = base_font.render(user_text, True, (255, 255, 255))

                            # blits the window with the input box
                            win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                            input_rect.w = max(100, text_surface.get_width()+10)

                            # flips the display
                            pygame.display.flip()
                            
                    #These sets of if statements are to check if the player answered the questions correct
                    if i.question.check(user_text) == True and counter%2 == 1:
                        points1 += i.question.worth
                    elif i.question.check(user_text) != True and counter%2 == 1:
                        points2 += (i.question.worth)/2
                    elif i.question.check(user_text) == True and counter%2 == 0:
                        points2 += i.question.worth
                    elif i.question.check(user_text) != True and counter%2 == 0:
                        points1 += (i.question.worth)/2

                # creates a new font w sans bold, size 16
                font = pygame.font.Font('freesansbold.ttf', 16)
                # This prints out the points for player 1 after every question is answered   
                player1 = font.render("Player 1 Points: " + str(points1), True, (0, 0, 0), (255,255,255))
                pygame.draw.rect(win, (255, 255, 255), pygame.Rect(700, 600, 200, 200))
                textRect = player1.get_rect(center = (800,400))

                # This prints out the points for player 2 after every question is answered  
                player2 = font.render("Player 2 Points: " + str(points2), True, (0, 0, 0), (255,255,255))
                pygame.draw.rect(win, (255, 255, 255), pygame.Rect(700, 700, 200, 200))
                textRect2 = player2.get_rect(center = (800,600))
                
                # blit 
                win.blit(player1, textRect)
                pygame.display.flip()
                win.blit(player2, textRect2)
                pygame.display.flip()

            counter+=1
        # Checks if the button is black (meaning it the question has been answered)
        gamended = True
        for g in buttonl:
            if g.color != (0, 0, 0):
                gamended = False
                
        # If it is black then it ends the game stating whether or not Player 1 wins or Player 2 wins  
        if gamended:
            if(points1>points2):
                # Player 1 wins the game 
                player1wins = font.render("Player 1 Wins!" , True, (0, 0, 0), (255,255,255))
                pygame.draw.rect(win, (255, 255, 255), pygame.Rect(500, 800, 200, 200))
                textRects = player1wins.get_rect(center = (800,700)) 
                win.blit(player1wins, textRects)
                pygame.display.flip()
                 
            elif(points1<points2):
                # Player 2 wins the game
                player2wins = font.render("Player 2 Wins!" , True, (0, 0, 0), (255,255,255))
                pygame.draw.rect(win, (255, 255, 255), pygame.Rect(500, 800, 200, 200))
                textRects = player2wins.get_rect(center = (800,700)) 
                win.blit(player2wins, textRects)
                pygame.display.flip()
            
            else:
                #There is a tie!
                player2wins = font.render("It's a tie!" , True, (0, 0, 0), (255,255,255))
                pygame.draw.rect(win, (255, 255, 255), pygame.Rect(500, 800, 200, 200))
                textRects = player2wins.get_rect(center = (800,700)) 
                win.blit(player2wins, textRects)
                pygame.display.flip()