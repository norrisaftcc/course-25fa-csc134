#!/usr/bin/env python3
"""
Orbital Delivery - A Lunar Lander-style game where AI packages rate their delivery.

Entry point and main game loop.
Demonstrates modular Python game architecture with clean separation of concerns.
"""

import pygame
import sys

# Import game modules
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK,
    STATE_ORBIT, STATE_DESCENT, STATE_LANDED, STATE_CRASHED, STATE_RATING, STATE_GAME_OVER,
    LANDING_PAD_Y
)
from physics import apply_gravity, apply_thrust, update_position, check_landing, get_altitude
from ship import Ship
from package import Package, create_random_package
from level import Level, StarField
from ui import HUD, MenuScreen, RatingScreen, GameOverScreen


class Game:
    """
    Main game class handling initialization, game loop, and state management.
    """

    def __init__(self):
        """Initialize Pygame and game objects."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Orbital Delivery")
        self.clock = pygame.time.Clock()

        # Game state
        self.state = "title"  # title, orbit, descent, rating, game_over
        self.running = True
        self.difficulty = 1

        # Game objects
        self.ship = Ship()
        self.package = None
        self.level = None
        self.star_field = StarField()

        # UI components
        self.hud = HUD()
        self.menu = MenuScreen()
        self.rating_screen = RatingScreen()
        self.game_over_screen = GameOverScreen()

        # Delivery tracking
        self.landed_successfully = False

    def new_delivery(self):
        """Set up a new delivery attempt."""
        self.ship.reset()
        self.package = create_random_package()
        self.level = Level(self.difficulty)

        # Position ship above the landing pad (with some offset)
        pad_info = self.level.get_pad_info()
        self.ship.x = pad_info['center_x']
        self.ship.y = 80

        self.landed_successfully = False
        self.state = STATE_ORBIT

    def handle_events(self):
        """Process input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == "title":
                        self.running = False
                    else:
                        self.state = "title"

                elif event.key == pygame.K_SPACE:
                    self._handle_space_press()

    def _handle_space_press(self):
        """Handle space bar press based on current state."""
        if self.state == "title":
            self.new_delivery()

        elif self.state == STATE_ORBIT:
            self.state = STATE_DESCENT

        elif self.state == STATE_RATING:
            self.difficulty += 1
            self.new_delivery()

        elif self.state == STATE_GAME_OVER:
            self.difficulty = 1
            self.new_delivery()

    def handle_input(self):
        """Process held keys for continuous input."""
        if self.state != STATE_DESCENT:
            return

        keys = pygame.key.get_pressed()

        # Rotation
        if keys[pygame.K_a]:
            self.ship.rotate_left()
        if keys[pygame.K_d]:
            self.ship.rotate_right()

        # Thrust
        self.ship.thrusting = keys[pygame.K_w] and self.ship.can_thrust()

    def update(self):
        """Update game state."""
        if self.state != STATE_DESCENT:
            return

        # Apply physics
        self.ship.vel_x, self.ship.vel_y = apply_gravity(
            self.ship.vel_x, self.ship.vel_y)

        # Apply thrust if thrusting
        if self.ship.thrusting:
            self.ship.vel_x, self.ship.vel_y, delta_v = apply_thrust(
                self.ship.vel_x, self.ship.vel_y, self.ship.angle)
            self.ship.consume_fuel()

            # Track delta-v for fragile packages
            if self.package:
                self.package.add_delta_v(delta_v)

        # Update position
        self.ship.x, self.ship.y = update_position(
            self.ship.x, self.ship.y, self.ship.vel_x, self.ship.vel_y)

        # Keep ship on screen horizontally
        self.ship.x = max(20, min(SCREEN_WIDTH - 20, self.ship.x))

        # Update package time
        if self.package:
            self.package.add_time(1.0 / FPS)

        # Check for landing/crash
        pad_info = self.level.get_pad_info()
        result = check_landing(
            self.ship.x, self.ship.y,
            self.ship.vel_x, self.ship.vel_y,
            pad_info['x'], pad_info['y'],
            pad_info['width'], pad_info['height']
        )

        if result['status'] == 'landed':
            self.landed_successfully = True
            self.state = STATE_RATING

        elif result['status'] == 'crashed':
            self.landed_successfully = False
            if self.package:
                self.package.mark_crashed()
            self.state = STATE_RATING

        elif result['status'] == 'missed':
            self.landed_successfully = False
            if self.package:
                self.package.mark_crashed()
            self.state = STATE_RATING

        # Check for out of fuel while still high up
        if self.ship.fuel <= 0 and self.ship.y < LANDING_PAD_Y - 100:
            # Let them fall a bit, but eventually game over
            if self.ship.vel_y > 5:  # Falling fast
                self.state = STATE_GAME_OVER

    def draw(self):
        """Render the current frame."""
        # Clear screen
        self.screen.fill(BLACK)

        # Always draw stars
        self.star_field.draw(self.screen)

        if self.state == "title":
            self.menu.draw_title(self.screen)

        elif self.state == STATE_ORBIT:
            # Draw level and ship in background
            if self.level:
                self.level.draw(self.screen)
            self.ship.draw(self.screen)
            # Draw orbit overlay
            self.menu.draw_orbit(self.screen, self.package)

        elif self.state == STATE_DESCENT:
            # Draw level
            if self.level:
                self.level.draw(self.screen)

            # Draw ship
            self.ship.draw(self.screen)

            # Draw HUD
            altitude = get_altitude(self.ship.y, LANDING_PAD_Y)
            self.hud.draw(self.screen, self.ship, self.package, altitude)

        elif self.state == STATE_RATING:
            # Draw final scene
            if self.level:
                self.level.draw(self.screen)

            # Draw ship (crashed or landed)
            if self.landed_successfully:
                self.ship.draw(self.screen)
            else:
                self.ship.draw_crashed(self.screen)

            # Draw rating overlay
            self.rating_screen.draw(self.screen, self.package, self.landed_successfully)

        elif self.state == STATE_GAME_OVER:
            if self.level:
                self.level.draw(self.screen)
            self.ship.draw(self.screen)
            self.game_over_screen.draw(self.screen)

        # Update display
        pygame.display.flip()

    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


def main():
    """Entry point."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
