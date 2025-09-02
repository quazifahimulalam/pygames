import pygame


pygame.init()
screen_height , screen_width = 500 , 600
screen = pygame.display.set_mode((400 , 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen , (0 , 125 ,255) , pygame.Rect(50 , 50 , 300 , 400))
    
    pygame.display.flip()