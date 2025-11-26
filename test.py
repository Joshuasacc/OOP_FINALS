import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Sample")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Rectangle position
x, y = 50, 50
speed = 5

# Game loop
running = True
while running:
    pygame.time.delay(30)  # Delay to control speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Fill background
    win.fill(WHITE)
    # Draw rectangle
    pygame.draw.rect(win, RED, (x, y, 50, 50))
    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
