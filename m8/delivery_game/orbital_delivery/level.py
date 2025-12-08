# level.py - Landing zones, terrain, and difficulty scaling

import random
import pygame
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    LANDING_PAD_WIDTH, LANDING_PAD_HEIGHT, LANDING_PAD_Y,
    GREEN, GRAY, DARK_GRAY, WHITE
)


class LandingPad:
    """Represents the landing zone target."""

    def __init__(self, x=None, width=LANDING_PAD_WIDTH):
        """
        Initialize landing pad.

        Args:
            x: X position (left edge). If None, randomized.
            width: Width of the pad
        """
        self.width = width
        self.height = LANDING_PAD_HEIGHT
        self.y = LANDING_PAD_Y

        if x is None:
            # Random position, but keep pad on screen
            margin = 50
            self.x = random.randint(margin, SCREEN_WIDTH - margin - self.width)
        else:
            self.x = x

    def get_center_x(self):
        """Get the center X coordinate of the pad."""
        return self.x + self.width // 2

    def draw(self, surface):
        """Draw the landing pad."""
        # Main pad surface
        pad_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, GREEN, pad_rect)

        # Pad border/markings
        pygame.draw.rect(surface, WHITE, pad_rect, 2)

        # Landing lights (small circles on each end)
        light_radius = 4
        pygame.draw.circle(surface, WHITE,
                           (self.x + light_radius + 2, self.y + self.height // 2),
                           light_radius)
        pygame.draw.circle(surface, WHITE,
                           (self.x + self.width - light_radius - 2, self.y + self.height // 2),
                           light_radius)


class Terrain:
    """Simple terrain/ground rendering."""

    def __init__(self):
        """Initialize terrain with some random variation."""
        self.ground_y = LANDING_PAD_Y + LANDING_PAD_HEIGHT
        self.generate_terrain()

    def generate_terrain(self):
        """Generate terrain height points."""
        self.points = []
        num_points = 20
        segment_width = SCREEN_WIDTH // (num_points - 1)

        for i in range(num_points):
            x = i * segment_width
            # Vary height slightly for visual interest
            y_offset = random.randint(-5, 5)
            self.points.append((x, self.ground_y + y_offset))

        # Make sure edges go to screen edge
        self.points[0] = (0, self.ground_y)
        self.points[-1] = (SCREEN_WIDTH, self.ground_y)

    def draw(self, surface):
        """Draw the terrain."""
        # Draw filled ground
        ground_points = self.points + [
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            (0, SCREEN_HEIGHT)
        ]
        pygame.draw.polygon(surface, DARK_GRAY, ground_points)

        # Draw terrain surface line
        if len(self.points) > 1:
            pygame.draw.lines(surface, GRAY, False, self.points, 2)


class Level:
    """
    Represents a complete level with landing pad and terrain.
    Handles difficulty scaling.
    """

    def __init__(self, difficulty=1):
        """
        Initialize a level.

        Args:
            difficulty: Difficulty level (1+), affects pad size/position
        """
        self.difficulty = difficulty

        # Adjust pad width based on difficulty
        base_width = LANDING_PAD_WIDTH
        width_reduction = min(difficulty * 5, 40)  # Max 40px reduction
        pad_width = max(base_width - width_reduction, 40)  # Min 40px width

        self.landing_pad = LandingPad(width=pad_width)
        self.terrain = Terrain()

    def get_pad_info(self):
        """Get landing pad position and size."""
        return {
            'x': self.landing_pad.x,
            'y': self.landing_pad.y,
            'width': self.landing_pad.width,
            'height': self.landing_pad.height,
            'center_x': self.landing_pad.get_center_x()
        }

    def draw(self, surface):
        """Draw the complete level."""
        self.terrain.draw(surface)
        self.landing_pad.draw(surface)


class StarField:
    """Background star field for atmosphere."""

    def __init__(self, num_stars=100):
        """Generate random star positions."""
        self.stars = []
        for _ in range(num_stars):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT - 100)  # Keep above ground
            brightness = random.randint(100, 255)
            size = random.choice([1, 1, 1, 2])  # Most stars are small
            self.stars.append((x, y, brightness, size))

    def draw(self, surface):
        """Draw the star field."""
        for x, y, brightness, size in self.stars:
            color = (brightness, brightness, brightness)
            if size == 1:
                surface.set_at((x, y), color)
            else:
                pygame.draw.circle(surface, color, (x, y), size)
