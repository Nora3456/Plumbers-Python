import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

BLUE = (135, 206, 235)
GREEN = (34, 139, 34)

homer_img = pygame.image.load("homer.png").convert_alpha()
homer_img = pygame.transform.scale(homer_img, (60, 60))

player_rect = homer_img.get_rect()
player_rect.x = 100
player_rect.y = 400

player_speed = 5
y_velocity = 0
gravity = 0.6
jump_strength = -12
on_ground = False

## mThe bushes platforms
platforms = [
    pygame.Rect(0, 550, 800, 50),     
    pygame.Rect(200, 450, 150, 20),
    pygame.Rect(450, 380, 150, 20),
]

# Donut ("collectible coins")
donut_img = pygame.image.load("donut.png").convert_alpha()
donut_img = pygame.transform.scale(donut_img, (40, 40))

donuts = [
    pygame.Rect(220, 410, 40, 40),
    pygame.Rect(280, 410, 40, 40),
    pygame.Rect(480, 340, 40, 40),
    pygame.Rect(540, 340, 40, 40),
    pygame.Rect(700, 510, 40, 40)
]

font = pygame.font.SysFont(None, 60)
win = False


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    if keys[pygame.K_SPACE] and on_ground:
        y_velocity = jump_strength
        on_ground = False

    y_velocity += gravity
    player_rect.y += y_velocity

    on_ground = False
    for platform in platforms:
        if player_rect.colliderect(platform) and y_velocity >= 0:
            player_rect.bottom = platform.top
            y_velocity = 0
            on_ground = True

    for donut in list(donuts):
        if player_rect.colliderect(donut):
            donuts.remove(donut)

    if len(donuts) == 0:
        win = True

    screen.fill(BLUE)

    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    for donut in donuts:
        screen.blit(donut_img, donut)

    screen.blit(homer_img, player_rect)

    if win:
        text = font.render("YOU WIN!", True, (255, 255, 0))
        screen.blit(text, (300, 200))

    pygame.display.flip()
    clock.tick(60)