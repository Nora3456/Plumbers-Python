import pygame
import sys


# 1) Initialize the engine
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


# 2) Setup the "hero" (the math)
player_rect = pygame.Rect(400, 300, 50, 50)
player_speed = 5
color = (255, 0, 0)

target_rects = [
   pygame.Rect(300, 300, 50, 50),
   pygame.Rect(500, 300, 50, 50),
   pygame.Rect(100, 300, 50, 50)
]
GREEN = (0, 255, 0)


# 3) The holy game loop
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()



      
   # Collision detection and removal
   for target_rect in list(target_rects): # Iterate over a copy to allow modification
           if player_rect.colliderect(target_rect):
               target_rects.remove(target_rect) # Remove the collided rectangle from the list


   screen.fill((135, 206, 235))
   pygame.draw.rect(screen, color, player_rect)
  
   for target_rect in target_rects:
           pygame.draw.rect(screen, GREEN, target_rect)
   pygame.display.flip()
   # Draw remaining targets




   # Cap to 60 FPS
   clock.tick(60)
  
