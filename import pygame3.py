import pygame

#setup lol
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("made by subnerf2")
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#FFFFFF")
    # Draw the player

    pygame.draw.rect(screen, "#0000FF", (20, 20, 50, 50))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt 

    dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time



    pygame.draw.circle(screen, (200,50,50), player_pos, 25)
    
    
    pygame.display.flip()





pygame.quit()