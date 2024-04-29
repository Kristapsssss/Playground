import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
winner_font = pygame.font.SysFont('Comic Sans MS', 360)

# Initialize the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
score = 0
lives = 5

# Set the bar x, y coordinates and width height
bar = pygame.Rect((SCREEN_WIDTH/2, SCREEN_HEIGHT-50, 600, 150))

# enemies
enemies = []
color_list = []
enemies_colors = [(169, 50, 38), (203, 67, 53), (136, 78, 160), (125, 60, 152), (23, 165, 137), (19, 141, 117),
                  (34, 153, 84), (46, 204, 113), (241, 196, 15), (243, 156, 18), (230, 126, 34), (208, 211, 212)
                  , (189, 195, 199), (127, 140, 141), (52, 73, 94)]
for y in range(4):
    for i in range(17):
        enemy = pygame.Rect(440 + i * 86, 100 + y * 100, 75, 50)
        color_list.append(random.choice(enemies_colors))
        enemies.append(enemy)


ball_center = [960, 540]
ball_x_move = random.uniform(3.1, 4.5)
ball_y_move = random.uniform(3.1, 4.5)



# Set cursor invisible
pygame.mouse.set_visible(False)

# Set clock
clock = pygame.time.Clock()

# Main game loop
while True:
    screen.fill((93, 173, 226))

    # Draw objects
    pygame.draw.rect(screen, (205, 92, 92), bar)

    ball = pygame.draw.circle(screen, (253, 254, 254), ball_center, 15)

    left_border = pygame.draw.line(screen, (40, 180, 99), [0, 0], [0, SCREEN_HEIGHT], 800)
    top_border = pygame.draw.line(screen, (40, 180, 99), [0, 0], [SCREEN_WIDTH, 0], 10)
    right_border = pygame.draw.line(screen, (40, 180, 99), [SCREEN_WIDTH, 0], [SCREEN_WIDTH, SCREEN_HEIGHT], 20)

    for enemy in enemies:
        pygame.draw.rect(screen, color=color_list[enemies.index(enemy)], rect=enemy)

    # Set collision of ball
    if ball.colliderect(bar):
        ball_y_move *= -1.00
        if score > 5 and -20 < ball_y_move < 20:
            ball_y_move *= 1.05
            ball_x_move *= 1.05
            bar.scale_by_ip(0.98, 0.98)
    elif ball.collidelistall([left_border, right_border]):
        ball_x_move *= -1.00
    elif ball.colliderect(top_border):
        ball_y_move *= -1.00
    # Collision with enemies
    elif ball.collidelistall(enemies):
        # Check for collision with multiple enemies at once
        if len(ball.collidelistall(enemies)) > 1:
            for enemy in ball.collidelistall(enemies):
                enemies[enemy].x = 2000
            ball_y_move *= -1.00
            score += 2
        else:
            for enemy in ball.collidelistall(enemies):
                if enemies[enemy].x-37.5 < ball.x < enemies[enemy].x+37.5 and not enemies[enemy].y-23 < ball.y < enemies[enemy].y+23:
                    ball_y_move *= -1.00
                else:
                    ball_x_move *= -1.00
                enemies[enemy].x = 2000
                score += 1


    # Set movement of ball
    ball_center[0] += ball_x_move
    ball_center[1] += ball_y_move
    # If ball out of bounds
    if ball_center[1] > 1200:
        ball_center[0] = 960
        ball_center[1] = 540
        lives -= 1
        if ball_x_move > 10:
            ball_x_move -= 10
        else:
            ball_x_move += 5
        if ball_y_move > 10:
            ball_y_move -= 10
        else:
            ball_y_move += 5
    elif ball_center[1] < 0:
        ball_center[1] += 50
    elif ball_center[0] > 1950:
        ball_center[1] -= 100
    elif ball_center[0] < 400:
        ball_center[0] += 100

    # Set Key presses and actions
    key = pygame.key.get_pressed()
    if key[K_ESCAPE]:
        pygame.quit()

    # Event handler
    for event in pygame.event.get():
        # If x is clicked, exit game
        if event.type == pygame.QUIT:
            pygame.quit()
        # If mouse is moved, will change the x position of the bar
        elif event.type == MOUSEMOTION and event.buttons[0] == 1:
            bar.x += event.rel[0]
            bar.y += event.rel[1]
            bar.x = max(400, min(bar.x, SCREEN_WIDTH - (bar.width + 10)))
            bar.y = max(950, min(bar.y, SCREEN_HEIGHT - (bar.height - 50)))

    # Handle gui text and images
    welcome_text = my_font.render('Welcome to Breakout', False, (0, 0, 0))
    instruction_text = my_font.render('break all the blocks to win', False, (0, 0, 0))
    speed_text = my_font.render(f'current ball speed: {abs(ball_y_move * ball_x_move):.2f}', False, (0, 0, 0))
    blocks_text = my_font.render(f'Blocks destroyed: {score}/68', False, (0, 0, 0))
    winner_text = winner_font.render('You Win!', False, (0, 204, 0))
    loser_text = winner_font.render("You lose!",False, (211, 47, 47 ))

    screen.blit(welcome_text, (30, 0))
    screen.blit(instruction_text, (30, 60))
    screen.blit(speed_text, (30, 240))
    screen.blit(blocks_text, (30, 300))

    heart = pygame.image.load('images/heart2.png')

    for life in range(lives):
        screen.blit(heart, (life*60, 990))

    # Win if all objects destroyed
    if score > 67:
        screen.blit(winner_text, (450, 100))
    elif lives < 1:
        screen.blit(loser_text, (450, 100))

    clock.tick(120)

    # Update screen
    pygame.display.update()


