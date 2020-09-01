import pygame
import random

pygame.init()
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
# The above initialises the game and sets the screen height and width

player = pygame.image.load("image.png")
enemy_1 = pygame.image.load("enemy.png")
enemy_2 = pygame.image.load("monster.jpg")
enemy_3 = pygame.image.load("image.png")
# The above uploads the enemy images and player image

player_height = player.get_height()
player_width = player.get_width()
enemy_1_height = enemy_1.get_height()
enemy_1_width = enemy_1.get_width()
enemy_2_height = enemy_2.get_height()
enemy_2_width = enemy_2.get_width()
enemy_3_height = enemy_3.get_height()
enemy_3_width = enemy_3.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))
# The above gets the height and width for the objects and then prints them

playerXPosition = 100
playerYPosition = 50
# The above stores the position of the player

enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_1_height)
enemyYPosition = random.randint(0, screen_height - enemy_2_height)
enemyYPosition = random.randint(0, screen_height - enemy_3_height)
# The above starts the enemy in a random position

enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_1_height)
enemyYPosition = random.randint(0, screen_height - enemy_2_height)
enemyYPosition = random.randint(0, screen_height - enemy_3_height)
# The above starts the enemy off screen and on a random position

keyUp = False
keyDown = False
# This checks if the keys are pressed

while 1:
    screen.fill(0)  # Clears the screen.
    screen.blit(player, (playerXPosition,playerYPosition))
    # This draws the player image to the screen at the position specified. I.e. (100, 50)
    screen.blit(enemy_1, (enemyXPosition, enemyYPosition))
    screen.blit(enemy_2, (enemyXPosition, enemyYPosition))
    screen.blit(enemy_3, (enemyXPosition, enemyYPosition))

    pygame.display.flip()  # This updates the screen.
    # The above updates the screen.

#The below checks if the user has quit
for event in pygame.event.get():

    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)

if event.type == pygame.KEYDOWN: # This checks if the user has pushed the down arrow

    if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
        keyUp = True
    if event.key == pygame.K_DOWN:
        keyDown = True
# Test if the key pressed is the one we want to push.

if event.type == pygame.KEYUP:
    if event.key == pygame.K_UP:
        keyUp = False
    if event.key == pygame.K_DOWN:
        keyDown = False
# The above
if keyUp:
    if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

playerBox = pygame.Rect(player.get_rect())
# This is the bounding box for the player

playerBox.top = playerYPosition
playerBox.left = playerXPosition

enemyBox = pygame.Rect(enemy.get_rect())
enemyBox.top = enemyYPosition
enemyBox.left = enemyXPosition
# The bounding box for the enemy

if playerBox.colliderect(enemyBox):   # This is to test collision of boxes
    print("You lose!")

pygame.quit()
exit(0)

if enemyXPosition < 0 - enemy_width:
    print("You win!")

pygame.quit()

exit(0)