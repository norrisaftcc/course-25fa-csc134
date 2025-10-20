import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 128, 0),  # Orange
    (128, 0, 255),  # Purple
]

# Function to create a ball dictionary
def create_ball(x, y, radius, color, vx, vy):
    """Creates and returns a ball dictionary"""
    return {
        'x': x,
        'y': y,
        'radius': radius,
        'color': color,
        'vx': vx,
        'vy': vy
    }

# Function to update ball position
def update_ball(ball):
    """Updates ball position based on velocity"""
    ball['x'] += ball['vx']
    ball['y'] += ball['vy']

# Function to handle wall collisions
def bounce_ball(ball, width, height):
    """Reverses velocity if ball hits a wall"""
    # If statement: Check left/right walls
    if ball['x'] - ball['radius'] <= 0 or ball['x'] + ball['radius'] >= width:
        ball['vx'] = -ball['vx']
    
    # If statement: Check top/bottom walls
    if ball['y'] - ball['radius'] <= 0 or ball['y'] + ball['radius'] >= height:
        ball['vy'] = -ball['vy']

# Function to draw a ball
def draw_ball(screen, ball):
    """Draws a single ball on the screen"""
    pygame.draw.circle(screen, ball['color'], 
                      (int(ball['x']), int(ball['y'])), 
                      ball['radius'])

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiple Bouncing Balls - C++ Concepts Demo")
clock = pygame.time.Clock()

# Create list of balls (demonstrates list/array usage)
balls = []
num_balls = 8

# Loop to initialize multiple balls
for i in range(num_balls):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    radius = random.randint(15, 30)
    color = COLORS[i % len(COLORS)]  # Cycle through colors
    vx = random.randint(-6, 6)
    vy = random.randint(-6, 6)
    
    # If statement: Ensure ball isn't stationary
    if vx == 0:
        vx = 3
    if vy == 0:
        vy = 3
    
    # Add ball to list (function call)
    balls.append(create_ball(x, y, radius, color, vx, vy))

# Main game loop (while loop)
running = True
while running:
    # Event loop (for loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Loop through each ball in the list
    for ball in balls:
        update_ball(ball)          # Function call
        bounce_ball(ball, WIDTH, HEIGHT)  # Function call
    
    # Drawing
    screen.fill(BLACK)
    
    # Loop to draw all balls
    for ball in balls:
        draw_ball(screen, ball)    # Function call
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()