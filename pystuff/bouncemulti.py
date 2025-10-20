import pygame
import sys
import random
import math

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

# Function to calculate distance between two balls
def get_distance(ball1, ball2):
    """Returns the distance between two ball centers"""
    dx = ball1['x'] - ball2['x']
    dy = ball1['y'] - ball2['y']
    return math.sqrt(dx * dx + dy * dy)

# Function to check if two balls are colliding
def check_ball_collision(ball1, ball2):
    """Returns True if two balls are colliding"""
    distance = get_distance(ball1, ball2)
    # If statement: collision occurs when distance < sum of radii
    if distance < ball1['radius'] + ball2['radius']:
        return True
    return False

# Function to handle ball-to-ball collision
def resolve_ball_collision(ball1, ball2):
    """Updates velocities when two balls collide"""
    # Calculate collision angle
    dx = ball2['x'] - ball1['x']
    dy = ball2['y'] - ball1['y']
    distance = math.sqrt(dx * dx + dy * dy)
    
    # If statement: prevent division by zero
    if distance == 0:
        return
    
    # Normalize collision vector
    nx = dx / distance
    ny = dy / distance
    
    # Relative velocity
    dvx = ball1['vx'] - ball2['vx']
    dvy = ball1['vy'] - ball2['vy']
    
    # Relative velocity in collision normal direction
    dot_product = dvx * nx + dvy * ny
    
    # If statement: only resolve if balls are moving toward each other
    if dot_product > 0:
        # Simple elastic collision (equal mass assumption)
        ball1['vx'] -= dot_product * nx
        ball1['vy'] -= dot_product * ny
        ball2['vx'] += dot_product * nx
        ball2['vy'] += dot_product * ny

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
        # Clamp position to prevent sticking
        if ball['x'] - ball['radius'] <= 0:
            ball['x'] = ball['radius']
        if ball['x'] + ball['radius'] >= width:
            ball['x'] = width - ball['radius']
    
    # If statement: Check top/bottom walls
    if ball['y'] - ball['radius'] <= 0 or ball['y'] + ball['radius'] >= height:
        ball['vy'] = -ball['vy']
        # Clamp position to prevent sticking
        if ball['y'] - ball['radius'] <= 0:
            ball['y'] = ball['radius']
        if ball['y'] + ball['radius'] >= height:
            ball['y'] = height - ball['radius']

# Function to draw a ball
def draw_ball(screen, ball):
    """Draws a single ball on the screen"""
    pygame.draw.circle(screen, ball['color'], 
                      (int(ball['x']), int(ball['y'])), 
                      ball['radius'])

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiple Bouncing Balls with Collisions")
clock = pygame.time.Clock()

# Create list of balls (demonstrates list/array usage)
balls = []
num_balls = 8

# Loop to initialize multiple balls
for i in range(num_balls):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    radius = random.randint(20, 35)
    color = COLORS[i % len(COLORS)]  # Cycle through colors
    vx = random.randint(-4, 4)
    vy = random.randint(-4, 4)
    
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
    
    # Loop through each ball to update position
    for ball in balls:
        update_ball(ball)          # Function call
        bounce_ball(ball, WIDTH, HEIGHT)  # Function call
    
    # Nested loop to check collisions between all pairs of balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):  # Only check each pair once
            # If statement: check collision
            if check_ball_collision(balls[i], balls[j]):
                resolve_ball_collision(balls[i], balls[j])
    
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