# Allow pygame_sdl2 to be imported as pygame.
try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import pygame

pygame.init()
pygame.mixer.init()

testmode = False

FPS = 60
clock = pygame.time.Clock()
SCREENWIDTH = 1280
SCREENHEIGHT = 720
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

blue = (127, 255, 212)
purple = (180, 182, 227)
pink = (255, 103, 180)
yellow = (255, 252, 197)
white = (255, 255, 255)

rightarrow = pygame.image.load('img/arrows/right.png')
rightarrow_rect = pygame.Rect(SCREENWIDTH - 120, SCREENHEIGHT - 200, 100, 55)
larrow = pygame.image.load('img/arrows/left.png')
larrow_rect = pygame.Rect(SCREENWIDTH - 300, SCREENHEIGHT - 200, 100, 55)
uarrow = pygame.image.load('img/arrows/up.png')
uarrow_rect = pygame.Rect(SCREENWIDTH - 190, SCREENHEIGHT - 300, 55, 100)
darrow = pygame.image.load('img/arrows/down.png')
darrow_rect = pygame.Rect(SCREENWIDTH - 190, SCREENHEIGHT - 125, 55, 100)

guffy = pygame.image.load("img/giraffe.png")
guffyrect = pygame.Rect(100, 100, 64, 64)

leo = pygame.image.load("img/lion.png")
leorect = pygame.Rect(700, 321, 64, 64)

pineapple = pygame.image.load("img/pineapple.png")
pineapplerect = pygame.Rect(308, 497, 64, 64)
pineappleon = True

pea = pygame.image.load("img/pea.png")
pearect = pygame.Rect(650, 80, 64, 64)
peaon = True

puffer = pygame.image.load("img/puffer.png")
pufferrect = pygame.Rect(193, 442, 64, 64)

pufferleft = pygame.image.load("img/pufferleft.png")

shark = pygame.image.load('img/shark.png')
sharkrect = pygame.Rect(600, 100, 64, 64)

squid = pygame.image.load('img/squid.png')
squidrect = pygame.Rect(602, 123, 64, 64)

manta = pygame.image.load('img/manta.png')
mantarect = pygame.Rect(411, 421, 64, 64)

fruitnumstart = 2
fruitnum = fruitnumstart

cupcake = pygame.image.load("img/cupcake.png")
cupcakerect = pygame.Rect(400, 173, 64, 64)

seaweed = pygame.image.load('img/seaweed.png')
seaweedrect = pygame.Rect(301, 210, 64, 72)

fonts = pygame.font.Font("font/animeace2_ital.ttf", 18)
playagainsurface = fonts.render("Play Again", False, white)
playagainrect = playagainsurface.get_rect(left=350, top=375)

quitsurface = fonts.render("Quit", False, white)
quitrect = quitsurface.get_rect(left=370, top=425)

jungleSound = pygame.mixer.Sound("snd/jungle.wav")

speed = 4
lspeed = 1
sspeed = 2
direction = "up"
level = 1
gameon = True

jungleSound.play(-1)

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if rightarrow_rect.collidepoint(mousepos):
                direction = "right"
            if larrow_rect.collidepoint(mousepos):
                direction = "left"
            if uarrow_rect.collidepoint(mousepos):
                direction = "up"
            if darrow_rect.collidepoint(mousepos):
                direction = 'down'
            if level == 100:
                if playagainrect.collidepoint(mousepos):
                    guffyrect.center = (100, 100)
                    leorect.center = (700, 321)
                    pineappleon = True
                    peaon = True
                    fruitnum = fruitnumstart
                    level = 1
                if quitrect.collidepoint(mousepos):
                    gameon = False

    if level == 1:
        screen.fill(blue)
        screen.blit(rightarrow, rightarrow_rect)
        screen.blit(larrow, larrow_rect)
        screen.blit(uarrow, uarrow_rect)
        screen.blit(darrow, darrow_rect)
        screen.blit(cupcake, cupcakerect)
        screen.blit(guffy, guffyrect)
        screen.blit(leo, leorect)

        if direction == "right":
            guffyrect.centerx = guffyrect.centerx + speed
        if direction == 'left':
            guffyrect.centerx = guffyrect.centerx - speed
        if direction == "up":
            guffyrect.centery = guffyrect.centery - speed
        if direction == 'down':
            guffyrect.centery = guffyrect.centery + speed

        if guffyrect.right > SCREENWIDTH:
            direction = "left"
        if guffyrect.left < 0:
            direction = "right"
        if guffyrect.top < 0:
            direction = "down"
        if guffyrect.bottom > SCREENHEIGHT:
            direction = "up"

        if not testmode:
            if guffyrect.centerx > leorect.centerx:
                leorect.centerx = leorect.centerx + lspeed
            if guffyrect.centerx < leorect.centerx:
                leorect.centerx = leorect.centerx - lspeed
            if guffyrect.centery < leorect.centery:
                leorect.centery = leorect.centery - lspeed
            if guffyrect.centery > leorect.centery:
                leorect.centery = leorect.centery + lspeed
   
        if pineappleon:
            if guffyrect.colliderect(pineapplerect):
                speed = 5
                pineappleon = False
                fruitnum = fruitnum - 1
        if pineappleon:
            screen.blit(pineapple, pineapplerect)

        if peaon:
            if guffyrect.colliderect(pearect):
                speed = 5
                peaon = False
                fruitnum = fruitnum - 1
        if peaon:
            screen.blit(pea, pearect)

        if guffyrect.colliderect(cupcakerect):
            speed = 2
        
        if fruitnum == 0:
            level = 2
    
        if guffyrect.colliderect(leorect):
            screen.fill(pink)
            gameoversurface = fonts.render("Game Over", False, white)
           
            screen.blit(gameoversurface, (350, 302))
            screen.blit(playagainsurface, playagainrect)
            screen.blit(quitsurface, quitrect)
            level = 100

    if level == 2:
        testmode = False
        screen.fill(purple)
        screen.blit(puffer, pufferrect)
        screen.blit(manta, mantarect)
        screen.blit(squid, squidrect)
        screen.blit(shark, sharkrect)
        screen.blit(seaweed, seaweedrect)
        screen.blit(rightarrow, rightarrow_rect)
        screen.blit(larrow, larrow_rect)
        screen.blit(uarrow, uarrow_rect)
        screen.blit(darrow, darrow_rect)

        if direction == "right":
            pufferrect.centerx = pufferrect.centerx + speed
        if direction == "left":
            puffer = pufferleft
            pufferrect.centerx = pufferrect.centerx - speed
        if direction == "up":
            pufferrect.centery = pufferrect.centery - speed
        if direction == "down":
            pufferrect.centery = pufferrect.centery + speed

        if pufferrect.right > SCREENWIDTH:
            direction = "left"
        if pufferrect.left < 0:
            direction = "right"
        if pufferrect.top < 0:
            direction = "down"
        if pufferrect.bottom > SCREENHEIGHT:
            direction = "up"

    clock.tick(FPS)
    pygame.display.update()


