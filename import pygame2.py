import pygame

#setup
pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("made by subnerf2")
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt 

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        print(pos)

    dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time


    screen.fill("#000000")
    pygame.draw.circle(screen, (200,50,50), player_pos, 25)
    pygame.display.flip()





pygame.quit()