from turtle import *
from random import randint
import time


s=getscreen()
s.setup(1000, 1000)
s.bgcolor('#000000')
t=getturtle()
t.color('#ffffff')
t.width(6)
t.speed(0)


wordList = ['Hello', 'Quack', 'Zebra', 'Chair', 'Boxes', 'Dwayne',\
             "St. Mark's School",\
            'elbow', 'remove', 'plausible', 'ghost', 'fuzzy', 'motion',\
            'mass', 'mountain', 'mountainous', 'dinner', 'yard', 'quilt',\
            'appreciate', 'condemned', 'taboo', 'possible', 'charge', 'bang',\
            'lethal', 'wicked', 'ordinary', 'learn', 'heartbreaking', 'lunch',\
            'quarrelsome', 'hurt', 'rush', 'time', 'iron', 'heavy', 'enjoy',\
            'wing', 'versed', 'obedient', 'wail', 'shade', 'gruesome', 'young',\
            'toungue', 'show', 'psychedelic', 'pack', 'discover', 'hallowed',\
            'earsplitting', 'billowy', 'cart', 'shelter', 'walk', 'embarrass',\
            'tub', 'toad', 'organic', 'steadfast', 'cars', 'guiltless', 'filthy']
fails = 6


tWriter = Turtle()
tWriter.hideturtle()
tWriter.shape('turtle')
tWriter.color('#ffffff')
tWriter.speed(0)

tBadLetters = Turtle()
tBadLetters.hideturtle()
tBadLetters.color('#ffffff')



alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
secretWord = ""
displayWord=""
lettersWrong = ""
lettersCorrect = ""
fails = 6
fontSize = 50
gameDone = False




def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto(-275,-300)
    tWriter.pendown()
    tWriter.write( newText, font=('Arial', fontSize, 'bold') )

def displayBadLetters(newText):
    tBadLetters.clear()
    tBadLetters.penup()
    tBadLetters.goto(-275,370)
    tBadLetters.pendown()
    tBadLetters.write( newText, font=('Arial', 30, 'bold') )

def chooseWord():
    global secretWord
    secretWord = wordList[randint(0,len(wordList)-1)]
    print("The secret word is: "+ secretWord)



def makeDisplay():
    global displayWord, secretWord, lettersCorrect
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter.lower() in lettersCorrect.lower():
                displayWord += letter + " "
            else:
                displayWord += "_" + " "

        else:
            displayWord += letter + " "



def drawGallows():
    t.penup()
    t.goto(-250, -250)
    t.pendown()
    t.forward(500)
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(50)
    t.hideturtle()
    



def drawHead():
    t.speed(0)
    t.right(90)
    for i in range(37):
        t.forward(10)
        t.left(10)


def drawTorso():
    t.penup()
    t.goto(-10,185)
    t.left(80)
    t.pendown()
    t.forward(250)
    



def drawRArm():
    t.penup()
    t.left(180)
    t.forward(150)
    t.right(120)
    t.pendown()
    t.forward(100)
    t.penup()
    t.right(180)
    t.forward(100)
    t.left(120)
    


def drawLArm():
    t.right(60)
    t.pendown()
    t.forward(100)
    t.penup()
    t.left(180)
    t.forward(100)
    t.right(120)



def drawRLeg():
    t.penup()
    t.forward(150)
    t.left(60)
    t.pendown()
    t.forward(120)
    t.penup()
    t.left(180)
    t.forward(120)
    t.left(30)




def drawLLeg():
    t.left(30)
    t.pendown()
    t.forward(120)
    t.penup()
    t.left(180)
    t.forward(120)


def updateHangmanPerson():
    global fails
    if fails == 5:
        drawHead()
    if fails == 4:
        drawTorso()
    if fails == 3:
        drawRArm()
    if fails == 2:
        drawLArm()
    if fails == 1:
        drawRLeg()
    if fails == 0:
        drawLLeg()

def getGuess():
    boxTitle = "Letters Used: " + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type // to guess the word")
    return guess





def checkWordGuess():
    global gameDone, fails
    boxTitle = "Guess the Word!!"
    guess = s.textinput(boxTitle, "Enter your guess for the word..")
    if guess.lower() == secretWord.lower():
        displayText("Yes! " + secretWord + " is the correct word!")
        gameDone = True
    else:
        displayText("No! " + guess + " is not the word")
        time.sleep(1)
        displayText(displayWord)
        fails -= 1
        updateHangmanPerson()

def playGame():
    global fails, lettersCorrect, lettersWrong, alpha, gameDone
    while gameDone == False and fails > 0 and "_" in displayWord:

        theGuess = getGuess()
        if theGuess == "//":
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess == "":
            displayText("Please guess only one letter")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess not in alpha:
            displayText("Please guess a letter")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        elif theGuess not in lettersWrong:
            displayText("No! " + theGuess + " is not the word")
            time.sleep(1)
            lettersWrong += theGuess.lower() + ","
            displayBadLetters("Not in word: {" + lettersWrong + "}")
            displayText(displayWord)
            fails -= 1
            updateHangmanPerson()
        else:
            displayText("No, " + theGuess + " is already guessed!")
            time.sleep(1)
            displayText(displayWord)
        if fails <= 0:
            displayBadLetters("No more guesses")
            displayText("You lose. The word was: " + secretWord)
            gameDone == True
        if "_" not in displayWord:
            displayBadLetters("You win!")
            gameDone = True


                




drawGallows()
drawHead()
drawTorso()
drawRArm()
drawLArm()
drawRLeg()
drawLLeg()

#start
time.sleep(1)
t.clear()

t.penup()
t.goto(-250,-250)
t.right(30)
t.pendown
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("Not in word: {" + lettersWrong + "}")
playGame()

