# ship.py - Ship state and rendering

import math
import pygame
from constants import (
    SHIP_START_X, SHIP_START_Y, SHIP_SIZE,
    STARTING_FUEL, FUEL_BURN_RATE, ROTATION_SPEED,
    WHITE, ORANGE, YELLOW, RED
)


class Ship:
    """
    Represents the delivery ship with position, velocity, fuel, and angle.
    Handles rendering and state management.
    """

    def __init__(self, x=SHIP_START_X, y=SHIP_START_Y):
        """Initialize ship at starting position."""
        self.x = x
        self.y = y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.angle = 0.0  # 0 = pointing up, positive = clockwise
        self.fuel = STARTING_FUEL
        self.thrusting = False
        self.size = SHIP_SIZE

    def reset(self, x=SHIP_START_X, y=SHIP_START_Y):
        """Reset ship to starting state."""
        self.x = x
        self.y = y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.angle = 0.0
        self.fuel = STARTING_FUEL
        self.thrusting = False

    def rotate_left(self):
        """Rotate counter-clockwise."""
        self.angle -= ROTATION_SPEED

    def rotate_right(self):
        """Rotate clockwise."""
        self.angle += ROTATION_SPEED

    def can_thrust(self):
        """Check if ship has fuel to thrust."""
        return self.fuel > 0

    def consume_fuel(self):
        """Consume fuel when thrusting."""
        if self.fuel > 0:
            self.fuel = max(0, self.fuel - FUEL_BURN_RATE)
            return True
        return False

    def get_triangle_points(self):
        """
        Calculate the three points of the ship triangle based on position and angle.
        Returns list of (x, y) tuples for the triangle vertices.
        """
        angle_rad = math.radians(self.angle)

        # Ship is a triangle pointing in the direction of angle
        # Nose (front)
        nose_x = self.x + math.sin(angle_rad) * self.size
        nose_y = self.y - math.cos(angle_rad) * self.size

        # Left wing
        left_angle = angle_rad + math.radians(140)
        left_x = self.x + math.sin(left_angle) * (self.size * 0.7)
        left_y = self.y - math.cos(left_angle) * (self.size * 0.7)

        # Right wing
        right_angle = angle_rad - math.radians(140)
        right_x = self.x + math.sin(right_angle) * (self.size * 0.7)
        right_y = self.y - math.cos(right_angle) * (self.size * 0.7)

        return [(nose_x, nose_y), (left_x, left_y), (right_x, right_y)]

    def get_flame_points(self):
        """
        Calculate points for the thrust flame triangle.
        Returns list of (x, y) tuples for the flame vertices.
        """
        angle_rad = math.radians(self.angle)

        # Flame comes out the back of the ship
        # Base of flame (between the wings)
        back_offset = self.size * 0.5

        # Center of flame base
        base_x = self.x - math.sin(angle_rad) * back_offset
        base_y = self.y + math.cos(angle_rad) * back_offset

        # Flame tip (extends further back)
        import random
        flame_length = self.size * (0.8 + random.random() * 0.4)  # Flicker effect
        tip_x = self.x - math.sin(angle_rad) * (back_offset + flame_length)
        tip_y = self.y + math.cos(angle_rad) * (back_offset + flame_length)

        # Flame base width
        base_width = self.size * 0.3
        left_x = base_x + math.cos(angle_rad) * base_width
        left_y = base_y + math.sin(angle_rad) * base_width
        right_x = base_x - math.cos(angle_rad) * base_width
        right_y = base_y - math.sin(angle_rad) * base_width

        return [(left_x, left_y), (right_x, right_y), (tip_x, tip_y)]

    def draw(self, surface):
        """
        Draw the ship on the given surface.

        Args:
            surface: Pygame surface to draw on
        """
        # Draw ship body (triangle)
        ship_points = self.get_triangle_points()
        pygame.draw.polygon(surface, WHITE, ship_points)
        pygame.draw.polygon(surface, WHITE, ship_points, 2)

        # Draw thrust flame if thrusting
        if self.thrusting and self.fuel > 0:
            flame_points = self.get_flame_points()
            # Inner flame (yellow)
            pygame.draw.polygon(surface, YELLOW, flame_points)
            # Outer glow effect - slightly larger orange flame
            import random
            if random.random() > 0.3:  # Flicker
                pygame.draw.polygon(surface, ORANGE, flame_points, 2)

    def draw_crashed(self, surface):
        """Draw a crashed/destroyed ship."""
        # Draw some debris triangles
        import random
        for i in range(4):
            offset_x = random.randint(-20, 20)
            offset_y = random.randint(-10, 10)
            size = random.randint(3, 8)
            points = [
                (self.x + offset_x, self.y + offset_y),
                (self.x + offset_x + size, self.y + offset_y + size),
                (self.x + offset_x - size, self.y + offset_y + size)
            ]
            pygame.draw.polygon(surface, RED, points)
