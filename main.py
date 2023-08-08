# Ruth Cassidy  City & Guilds No - ETF9634

# Below website used as reference to create game
# https://copyassignment.com/car-race-game-in-pygame-and-python/
# Below websites where images taken
# falcon - https://nwsppr.co/wp-content/uploads/2020/04/Landos_Millennium_Falcon-1536x698.png
# space - https://tse3.mm.bing.net/th?id=OIP.HEMlhNsGO4auAypjMo6_jAHaEK&pid=Api&P=0&w=309&h=174
# tie1 - https://tse2.mm.bing.net/th?id=OIP.bMmoreSw_TIB4dDhJehlBgHaDt&pid=Api&P=0&w=409&h=204
# tie2 and tie3 - https://tse4.mm.bing.net/th?id=OIP.DGONaxzJp5H8l2c5_sqB6gHaEK&pid=Api&P=0&w=278&h=156
# music - https://www.thesoundarchive.com/star-wars.asp

# Recording of working game can be found in resources/video

import sys
import pygame
import random
import math
import time

# Initializes pygame library and mixer
pygame.init()
pygame.mixer.init()

# Sets size of display window
gameWindow = pygame.display.set_mode((1060, 750))
# Sets name of display window
pygame.display.set_caption('Escape Of The Falcon')
# Sets image to display window icon
gameIcon = pygame.image.load('resources/images/falcon.png')
pygame.display.set_icon(gameIcon)
smallFont = pygame.font.Font('freesansbold.ttf', 25)
largeFont = pygame.font.Font('freesansbold.ttf', 50)

introMusic = pygame.mixer.Sound('resources/sounds/intro.wav')
gameplay = pygame.mixer.Sound('resources/sounds/gameplay.wav')
gameOverSound = pygame.mixer.Sound('resources/sounds/gameOver.wav')
success = pygame.mixer.Sound('resources/sounds/success.wav')


class Sound:

    def __init__(self):
        pass

    def introMusic(self):
        introMusic.play()

    def stopIntroMusic(self):
        introMusic.stop()

    def gamePlayMusic(self):
        gameplay.play()

    def stopGamePlayMusic(self):
        gameplay.stop()

    def gameOverSound(self):
        gameOverSound.play()

    def successSound(self):
        success.play()


class Intro:

    def __init__(self):
        pass

    def start(self, x, y):
        startBtn = largeFont.render("Start", True, (59,138,188))
        gameWindow.blit(startBtn, (x, y))

    def instructions(self, x, y):
        instructionBtn = largeFont.render("Instructions", True, (59,138,188))
        gameWindow.blit(instructionBtn, (x, y))

    def info(self, x, y):
        infoBtn = largeFont.render("Info", True, (59,138,188))
        gameWindow.blit(infoBtn, (x, y))

    def infoBg(self, x, y):
        infoImg = pygame.image.load('resources/images/info.png')

        active = True
        while active:
            gameWindow.blit(pygame.transform.scale(infoImg, (1060, 750)), (x, y))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False

    def instructionsBg(self, x, y):
        instructionsImg = pygame.image.load('resources/images/instructions.jpg')
        active = True
        while active:
            gameWindow.blit(pygame.transform.scale(instructionsImg, (1060, 750)), (x, y))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False


def introScreen():
    intro = Intro()
    sound = Sound()

    gameStarted = True
    sound.introMusic()
    while gameStarted:
        welcomeImg = pygame.image.load('resources/images/welcome.jpg')
        gameWindow.blit(pygame.transform.scale(welcomeImg, (1060, 750)), (0, 0))
        intro.start(100, 600)
        intro.info(400, 600)
        intro.instructions(650, 600)

        # Coordinates of mouse
        x, y = pygame.mouse.get_pos()

        # Creates box around buttons to click
        startBtn = pygame.Rect(100, 600, 120, 50)
        if startBtn.collidepoint(x, y):
            if click:
                countdown()
        infoBtn = pygame.Rect(400, 600, 100, 50)
        if infoBtn.collidepoint(x, y):
            if click:
                intro.infoBg(0, 0)
        instructionsBtn = pygame.Rect(650, 600, 310, 50)
        if instructionsBtn.collidepoint(x, y):
            if click:
                intro.instructionsBg(0, 0)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameStarted = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def countdown():
    sound = Sound()
    countdownBg = pygame.image.load('resources/images/countdown.png')
    three = largeFont.render('3', True, (255, 0, 0))
    two = largeFont.render('2', True, (255, 0, 0))
    one = largeFont.render('1', True, (255, 0, 0))
    go = largeFont.render('Lets Go', True, (7, 188, 5))

    # Display countdown background and 3,2,1
    gameWindow.blit(pygame.transform.scale(countdownBg, (1060, 750)), (0, 0))
    pygame.display.update()

    gameWindow.blit(three, (500, 600))
    pygame.display.update()
    time.sleep(.5)

    gameWindow.blit(pygame.transform.scale(countdownBg, (1060, 750)), (0, 0))
    pygame.display.update()
    time.sleep(.5)

    gameWindow.blit(two, (500, 600))
    pygame.display.update()
    time.sleep(.5)

    gameWindow.blit(pygame.transform.scale(countdownBg, (1060, 750)), (0, 0))
    pygame.display.update()
    time.sleep(.5)

    gameWindow.blit(one, (500, 600))
    pygame.display.update()
    time.sleep(.5)

    gameWindow.blit(pygame.transform.scale(countdownBg, (1060, 750)), (0, 0))
    pygame.display.update()
    time.sleep(.5)

    # Display Go
    gameWindow.blit(go, (450, 600))
    pygame.display.update()
    time.sleep(1)
    sound.stopIntroMusic()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            gamePlay()


def gamePlay():
    sound = Sound()
    sound.gamePlayMusic()
    timeAlive = 0
    highscore = 0
    clock = pygame.time.Clock()
    # Sets welcome image of display window
    bg = pygame.image.load('resources/images/space.jpg')

    # Sets image and position of falcon ship for player
    falcon = pygame.image.load('resources/images/falcon.png')
    falconX = 0
    falconY = 375
    falconXMove = 0
    falconYMove = 0

    # Sets images and random position of other ships
    shipOne = pygame.image.load('resources/images/tie1.jpg')
    shipOneX = 930
    shipOneY = random.randint(50, 620)
    shipOneMove = 25
    shipTwo = pygame.image.load('resources/images/tie2.jpg')
    shipTwoX = 970
    shipTwoY = random.randint(50, 620)
    shipTwoMove = 25
    shipThree = pygame.image.load('resources/images/tie3.jpg')
    shipThreeX = 970
    shipThreeY = random.randint(50, 620)
    shipThreeMove = 25
    shipFour = pygame.image.load('resources/images/tie2.jpg')
    shipFourX = random.randint(0, 960)
    shipFourY = 50
    shipFourMove = 15

    def displayScore(x, y):
        scoreTxt = smallFont.render('Your Score: ' + str("{:.2f}".format(timeAlive)), True, (59,138,188))
        gameWindow.blit(scoreTxt, (x, y))

    # Catch exceptions when reading the text file
    try:
        with open('highscore.txt', 'r') as score:
            highscore = score.read()
    except:
        print("Oops! Something went wrong when reading the file")
        print(sys.exc_info()[0], " occurred")

    def displayHighscore(x, y):
        highscoreTxt = smallFont.render('Highscore: ' + str(highscore), True, (59,138,188))
        gameWindow.blit(highscoreTxt, (x, y))

    def gameOver():
        outcome = "win"
        # Plays relevant sound if high score beat or not
        if float(highscore) > timeAlive:
            outcome = "lose"
            sound.gameOverSound()
        else:
            outcome = "win"
            sound.successSound()

        gameOverBg = pygame.image.load('resources/images/gameOver.png')

        active = True
        while active:

            gameWindow.blit(pygame.transform.scale(gameOverBg, (1060, 750)), (0, 0))
            restartGame = smallFont.render('Press Enter To Try Again', True, (255, 0, 0))
            gameWindow.blit(restartGame, (380, 650))
            displayScore(580, 550)
            displayHighscore(300, 550)

            if outcome == "win":
                text = smallFont.render('High Score Achieved!', True, (7, 188, 5))

                # Catch exceptions when writing score to the text file
                try:
                    with open('highscore.txt', 'w') as score:
                        score.write(str("{:.2f}".format(timeAlive)))
                except:
                    print("Oops! Something went wrong when writing to the file")
                    print(sys.exc_info()[0], " occurred")
            else:
                text = smallFont.render('Better Luck Next Time', True, (255, 0, 0))
            gameWindow.blit(text, (400, 500))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        countdown()

    active = True
    while active:
        finish = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Checks keys pressed for movement of player falcon ship
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    falconXMove += 10
                if event.key == pygame.K_LEFT:
                    falconXMove -= 10
                if event.key == pygame.K_UP:
                    falconYMove -= 10
                if event.key == pygame.K_DOWN:
                    falconYMove += 10
            # Checks keys released to stop movement of player falcon ship
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    falconXMove = 0
                if event.key == pygame.K_LEFT:
                    falconXMove = 0
                if event.key == pygame.K_UP:
                    falconYMove = 0
                if event.key == pygame.K_DOWN:
                    falconYMove = 0

        # Creates the timer
        timeStr = str(int(timeAlive * 10) / 10)
        displayTime = smallFont.render(f"Time : {timeStr}", True, (255, 0, 0))
        gameWindow.fill(pygame.Color('black'), rect=(860, 10, 150, 70 / 2))
        gameWindow.blit(displayTime, (860, 20))
        pygame.display.flip()
        timeInMili = clock.tick(30)
        if not finish:
            timeAlive += timeInMili / 1000

        # Sets boundary for the players ship
        if falconX < 0:
            falconX = 0
        if falconX > 950:
            falconX = 950
        if falconY < 50:
            falconY = 50
        if falconY > 620:
            falconY = 620

        # Display resized welcome image to fit display
        gameWindow.blit(pygame.transform.scale(bg, (1060, 650)), (0, 50))
        # Display resized ships
        gameWindow.blit(pygame.transform.scale(falcon, (130, 80)), (falconX, falconY))
        gameWindow.blit(pygame.transform.scale(shipOne, (120, 80)), (shipOneX, shipOneY))
        gameWindow.blit(pygame.transform.scale(shipTwo, (80, 80)), (shipTwoX, shipTwoY))
        gameWindow.blit(pygame.transform.scale(shipThree, (80, 80)), (shipThreeX, shipThreeY))

        # Updates movement
        falconX += falconXMove
        falconY += falconYMove
        shipOneX -= shipOneMove
        shipTwoX -= shipTwoMove
        shipThreeX -= shipThreeMove
        if shipOneX < -50:
            shipOneX = 1065
            shipOneY = random.randint(50, 620)
        if shipTwoX < -50:
            shipTwoX = 1065
            shipTwoY = random.randint(50, 620)
        if shipThreeX < -50:
            shipThreeX = 1065
            shipThreeY = random.randint(50, 620)

        # Places fourth ship once reached time of 10
        if timeAlive > 10:
            gameWindow.blit(pygame.transform.scale(shipFour, (80, 80)), (shipFourX, shipFourY))
            shipFourY += shipFourMove
            if shipFourY > 620:
                shipFourY = 50
                shipFourX = random.randint(0, 960)

        # Crash functionality
        def crash(shipX, shipY, playerX, playerY):
            distance = math.sqrt(math.pow(shipX - playerX, 2) + math.pow(shipY - playerY, 2))

            # checking distance is smaller then 50 for crash to occur
            if distance < 80:
                return True
            else:
                return False

        # if crash occurs
        if crash(shipOneX, shipOneY, falconX, falconY) or \
                crash(shipTwoX, shipTwoY, falconX, falconY) or \
                crash(shipThreeX, shipThreeY, falconX, falconY) or \
                crash(shipFourX, shipFourY, falconX, falconY):
            shipOneMove = 0
            shipTwoMove = 0
            shipThreeMove = 0
            shipFourMove = 0
            falconXMove = 0
            falconYMove = 0
            sound.stopGamePlayMusic()
            gameOver()

        pygame.display.update()


introScreen()
pygame.quit()
