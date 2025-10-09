import pygame

# Initialize PyGame
pygame.init()

# Set up display
window_width = 800
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Blitting Images")

# Load images
hero_right = pygame.image.load("C:\\Users\\klase\\Downloads\\OIP (2).webp")
hero_left = pygame.image.load("C:\\Users\\klase\\Downloads\\OIP (1).webp")

# Get rectangles for positioning
hero_right_rect = hero_right.get_rect()
hero_left_rect = hero_left.get_rect()

# Position images
hero_right_rect.topleft = (0, 0)
hero_left_rect.topleft = (window_width, 0)

# Main loop
running = True
while running:
    screen.fill((192, 192, 192))  # Silver background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_right_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        hero_right_rect.x += 5
    if keys[pygame.K_UP]:
        hero_right_rect.y -= 5
    if keys[pygame.K_DOWN]:
        hero_right_rect.y += 5

    # Blit images to screen
    screen.blit(hero_right, hero_right_rect)
    screen.blit(hero_left, hero_left_rect)

    pygame.display.flip()

pygame.quit()
