import pygame

#setup
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("made by subnerf2")
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

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

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        player_pos.x = pos[0]
        player_pos.y = pos[1]
        pygame.draw.circle(screen, "#000000", player_pos, 40)
        
    dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time


    screen.fill("#FFFFFF")
    pygame.draw.circle(screen, (200,50,50), player_pos, 25)
    pygame.display.flip()





pygame.quit()