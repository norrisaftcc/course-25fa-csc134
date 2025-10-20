import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)

# Physics constants
GRAVITY = 0.05
THRUST_POWER = 0.15
SIDE_THRUST_POWER = 0.08
MAX_SAFE_VELOCITY = 2.0

# Function to create lander
def create_lander(x, y):
    """Creates and returns a lander dictionary"""
    return {
        'x': x,
        'y': y,
        'vx': 0.0,
        'vy': 0.0,
        'fuel': 100,
        'size': 15,
        'landed': False,
        'crashed': False
    }

# Function to apply gravity
def apply_gravity(lander):
    """Applies gravitational acceleration to lander"""
    lander['vy'] += GRAVITY

# Function to apply thrust
def apply_thrust(lander, direction):
    """Applies thrust in specified direction if fuel available"""
    # If statement: check if fuel available
    if lander['fuel'] > 0:
        # If statement: determine thrust direction
        if direction == 'up':
            lander['vy'] -= THRUST_POWER
            lander['fuel'] -= 0.5
        elif direction == 'left':
            lander['vx'] -= SIDE_THRUST_POWER
            lander['fuel'] -= 0.3
        elif direction == 'right':
            lander['vx'] += SIDE_THRUST_POWER
            lander['fuel'] -= 0.3

# Function to update lander position
def update_lander(lander):
    """Updates lander position based on velocity"""
    lander['x'] += lander['vx']
    lander['y'] += lander['vy']

# Function to check landing
def check_landing(lander, ground_y):
    """Checks if lander has landed or crashed"""
    # If statement: check if touching ground
    if lander['y'] + lander['size'] >= ground_y:
        # Calculate total velocity magnitude
        velocity = math.sqrt(lander['vx']**2 + lander['vy']**2)
        
        # If statement: check if landing was safe
        if velocity <= MAX_SAFE_VELOCITY and abs(lander['vx']) < 1.5:
            lander['landed'] = True
            lander['vy'] = 0
            lander['vx'] = 0
            lander['y'] = ground_y - lander['size']
            return "SAFE LANDING!"
        else:
            lander['crashed'] = True
            lander['vy'] = 0
            lander['vx'] = 0
            return "CRASHED!"
    return None

# Function to draw lander
def draw_lander(screen, lander, thrusting):
    """Draws the lander on screen"""
    x = int(lander['x'])
    y = int(lander['y'])
    size = lander['size']
    
    # If statement: choose color based on status
    if lander['crashed']:
        color = RED
    elif lander['landed']:
        color = GREEN
    else:
        color = WHITE
    
    # Draw lander body (triangle)
    points = [
        (x, y - size),
        (x - size, y + size),
        (x + size, y + size)
    ]
    pygame.draw.polygon(screen, color, points)
    
    # If statement: draw thrust flame if thrusting
    if thrusting and not lander['landed'] and not lander['crashed']:
        flame_points = [
            (x - 5, y + size),
            (x + 5, y + size),
            (x, y + size + 15)
        ]
        pygame.draw.polygon(screen, ORANGE, flame_points)

# Function to draw ground
def draw_ground(screen, ground_y):
    """Draws the lunar surface"""
    pygame.draw.rect(screen, GRAY, (0, ground_y, WIDTH, HEIGHT - ground_y))

# Function to draw HUD
def draw_hud(screen, lander, font):
    """Draws heads-up display with lander info"""
    # Calculate velocity magnitude
    velocity = math.sqrt(lander['vx']**2 + lander['vy']**2)
    
    # Create text surfaces
    fuel_text = font.render(f"Fuel: {int(lander['fuel'])}%", True, WHITE)
    vel_text = font.render(f"Velocity: {velocity:.2f}", True, WHITE)
    vy_text = font.render(f"Vertical: {lander['vy']:.2f}", True, WHITE)
    vx_text = font.render(f"Horizontal: {lander['vx']:.2f}", True, WHITE)
    
    # If statement: color velocity based on safety
    if velocity > MAX_SAFE_VELOCITY:
        vel_color = RED
    else:
        vel_color = GREEN
    vel_text = font.render(f"Velocity: {velocity:.2f}", True, vel_color)
    
    # Draw text
    screen.blit(fuel_text, (10, 10))
    screen.blit(vel_text, (10, 35))
    screen.blit(vy_text, (10, 60))
    screen.blit(vx_text, (10, 85))
    
    # Draw controls
    controls = font.render("W: Up Thrust  A: Left  D: Right  R: Reset", True, YELLOW)
    screen.blit(controls, (WIDTH // 2 - 200, 10))

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lunar Lander - WAD Controls")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)
message_font = pygame.font.Font(None, 48)

# Game variables
ground_y = HEIGHT - 50
lander = create_lander(WIDTH // 2, 50)
game_message = None

# Main game loop (while loop)
running = True
while running:
    thrusting = False
    
    # Event loop (for loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keyboard state
    keys = pygame.key.get_pressed()
    
    # If statements: check for thrust input
    if keys[pygame.K_w]:
        apply_thrust(lander, 'up')
        thrusting = True
    if keys[pygame.K_a]:
        apply_thrust(lander, 'left')
    if keys[pygame.K_d]:
        apply_thrust(lander, 'right')
    
    # If statement: reset game
    if keys[pygame.K_r]:
        lander = create_lander(WIDTH // 2, 50)
        game_message = None
    
    # If statement: only update if not landed or crashed
    if not lander['landed'] and not lander['crashed']:
        apply_gravity(lander)
        update_lander(lander)
        result = check_landing(lander, ground_y)
        
        # If statement: check for landing result
        if result:
            game_message = result
    
    # If statement: check boundaries (bounce off sides)
    if lander['x'] < 0:
        lander['x'] = 0
        lander['vx'] = -lander['vx'] * 0.5
    elif lander['x'] > WIDTH:
        lander['x'] = WIDTH
        lander['vx'] = -lander['vx'] * 0.5
    
    # Drawing
    screen.fill(BLACK)
    draw_ground(screen, ground_y)
    draw_lander(screen, lander, thrusting)
    draw_hud(screen, lander, font)
    
    # If statement: draw landing message
    if game_message:
        msg_surface = message_font.render(game_message, True, 
                                         GREEN if lander['landed'] else RED)
        msg_rect = msg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(msg_surface, msg_rect)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()