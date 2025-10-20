import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball!")

# --- NEW: Create a clock to control framerate ---
clock = pygame.time.Clock()

# Ball properties
x = width // 2
y = height // 2
radius = 50
ball_color = (255, 0, 102) # Bright pink

# --- NEW: Set up ball's velocity (pixels per frame) ---
x_speed = 4
y_speed = 4

# --- Main Game Loop ---
running = True
while running:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- GAME LOGIC ---
    
    # Move the ball based on its speed
    x += x_speed
    y += y_speed

    # --- NEW: Bouncing Logic ---
    
    # If the ball's right edge hits the right wall OR its left edge hits the left wall
    if (x + radius >= width) or (x - radius <= 0):
        x_speed = -x_speed  # Reverse the horizontal direction

    # If the ball's bottom edge hits the bottom wall OR its top edge hits the top wall
    if (y + radius >= height) or (y - radius <= 0):
        y_speed = -y_speed  # Reverse the vertical direction


    # --- DRAWING ---
    
    # Fill the screen with a color (black)
    screen.fill((0, 0, 0))

    # Draw the circle at its new position
    pygame.draw.circle(screen, ball_color, (x, y), radius)

    # Update the display
    pygame.display.flip()

    # --- NEW: Limit the game to 60 frames per second (FPS) ---
    # This makes the ball's speed consistent
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()