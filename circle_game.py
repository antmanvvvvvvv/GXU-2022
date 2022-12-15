import pygame


pygame.init()
clock = pygame.time.Clock()

screenx = 1000
screeny = 600
screen = pygame.display.set_mode((screenx,screeny))
x = 500
y = 300
use_clock = True
fps = 250
# makes the leave button work
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    ks = pygame.key.get_pressed()
    if ks[pygame.K_w]:
        y = y - 1
    if ks[pygame.K_s]:
        y = y + 1
    if ks[pygame.K_a]:
        x = x - 1
    if ks[pygame.K_d]:
        x = x + 1
    if x > screenx:
        x = x - 1000
    if x < 0:
        x = x + 1000
    if y > screeny:
        y = y - 600
    if y < 0:
        y = y + 600
    screen.fill((0, 155, 255))
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 20)
    pygame.display.flip()


    if use_clock:
        clock.tick(fps)

pygame.quit()
