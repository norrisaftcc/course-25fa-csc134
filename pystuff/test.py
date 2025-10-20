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
while running:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (white)
    screen.fill((255, 255, 255))

    # Draw a simple blue circle
    pygame.draw.circle(screen, (0, 0, 255), (width // 2, height // 2), 50)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()