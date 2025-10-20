import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Test Window")

# --- Main Game Loop ---
running = True
x = width // 2
y = height // 2
radius = 50
frames = 0
while running:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (white)
    screen.fill((0, 0, 0))

    # Draw a simple circle
    
    pygame.draw.circle(screen, (255, 0, 102), (x, y), radius)

    # Slowly move the circle for next frame
    frames = frames + 1
    # only move the ball every 10 frames
    if frames % 20 == 0:
        x = x + 1
        y = y + 1
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()