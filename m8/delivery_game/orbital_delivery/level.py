# level.py - Landing zones, terrain, and difficulty scaling

import random
import math
import pygame
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    LANDING_PAD_WIDTH, LANDING_PAD_HEIGHT, LANDING_PAD_Y,
    TERRAIN_HEIGHT_BASE, TERRAIN_HEIGHT_PER_LEVEL, MAX_TERRAIN_HEIGHT,
    TERRAIN_FLAT_ZONE_MARGIN,
    GREEN, GRAY, DARK_GRAY, WHITE, RED
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
            # Random position, but keep pad on screen with margin for terrain
            margin = 80
            self.x = random.randint(margin, SCREEN_WIDTH - margin - self.width)
        else:
            self.x = x

    def get_center_x(self):
        """Get the center X coordinate of the pad."""
        return self.x + self.width // 2

    def get_flat_zone(self):
        """
        Get the X range that should be flat for landing.
        Returns (left_x, right_x) tuple.
        """
        return (
            self.x - TERRAIN_FLAT_ZONE_MARGIN,
            self.x + self.width + TERRAIN_FLAT_ZONE_MARGIN
        )

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
    """
    Terrain with hills and valleys that scale with difficulty.
    Provides collision detection via height lookup.
    """

    def __init__(self, difficulty=1, flat_zone=None):
        """
        Initialize terrain with difficulty-based variation.

        Args:
            difficulty: Level difficulty (1+), affects terrain roughness
            flat_zone: (left_x, right_x) tuple for flat landing area, or None
        """
        self.difficulty = difficulty
        self.flat_zone = flat_zone
        self.base_y = LANDING_PAD_Y + LANDING_PAD_HEIGHT

        # Calculate terrain roughness based on difficulty
        self.height_variation = min(
            TERRAIN_HEIGHT_BASE + (difficulty - 1) * TERRAIN_HEIGHT_PER_LEVEL,
            MAX_TERRAIN_HEIGHT
        )

        self.generate_terrain()

    def generate_terrain(self):
        """
        Generate terrain with smooth hills and valleys.
        Uses multiple sine waves for natural-looking terrain.
        """
        self.points = []
        num_points = 50  # More points for smoother terrain

        # Generate base terrain using layered sine waves
        for i in range(num_points + 1):
            x = (i / num_points) * SCREEN_WIDTH

            # Skip detailed generation if in flat zone
            if self.flat_zone and self.flat_zone[0] <= x <= self.flat_zone[1]:
                y = self.base_y
            else:
                # Layer multiple frequencies for natural terrain
                y_offset = 0

                # Primary wave (large hills)
                y_offset += math.sin(x * 0.01 + random.random() * 0.5) * self.height_variation * 0.6

                # Secondary wave (medium features)
                y_offset += math.sin(x * 0.025 + random.random()) * self.height_variation * 0.3

                # Tertiary wave (small bumps)
                y_offset += math.sin(x * 0.05 + random.random() * 2) * self.height_variation * 0.1

                y = self.base_y - y_offset  # Negative because y increases downward

            self.points.append((x, y))

        # Smooth transition into flat zone
        if self.flat_zone:
            self._smooth_flat_zone_edges()

    def _smooth_flat_zone_edges(self):
        """Create smooth transitions at flat zone boundaries."""
        if not self.flat_zone:
            return

        flat_left, flat_right = self.flat_zone
        transition_width = 40  # Pixels to smooth over

        for i, (x, y) in enumerate(self.points):
            # Left transition (approaching flat zone)
            if flat_left - transition_width < x < flat_left:
                t = (x - (flat_left - transition_width)) / transition_width
                t = t * t * (3 - 2 * t)  # Smoothstep
                new_y = y * (1 - t) + self.base_y * t
                self.points[i] = (x, new_y)

            # Right transition (leaving flat zone)
            elif flat_right < x < flat_right + transition_width:
                t = (x - flat_right) / transition_width
                t = t * t * (3 - 2 * t)  # Smoothstep
                new_y = self.base_y * (1 - t) + y * t
                self.points[i] = (x, new_y)

    def get_height_at(self, x):
        """
        Get terrain height (Y value) at a given X position.
        Used for collision detection.

        Args:
            x: X coordinate to check

        Returns:
            Y coordinate of terrain surface at that X
        """
        # Clamp x to valid range
        x = max(0, min(SCREEN_WIDTH, x))

        # Find the two points this x falls between
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]

            if x1 <= x <= x2:
                # Linear interpolation
                if x2 == x1:
                    return y1
                t = (x - x1) / (x2 - x1)
                return y1 + t * (y2 - y1)

        # Fallback
        return self.base_y

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
    Handles difficulty scaling for terrain, pad size, and ship position.
    """

    def __init__(self, difficulty=1):
        """
        Initialize a level.

        Args:
            difficulty: Difficulty level (1+), affects terrain, pad size, ship offset
        """
        self.difficulty = difficulty

        # Adjust pad width based on difficulty
        base_width = LANDING_PAD_WIDTH
        width_reduction = min((difficulty - 1) * 5, 40)  # Max 40px reduction
        pad_width = max(base_width - width_reduction, 50)  # Min 50px width

        # Create landing pad first
        self.landing_pad = LandingPad(width=pad_width)

        # Create terrain with flat zone around pad
        flat_zone = self.landing_pad.get_flat_zone()
        self.terrain = Terrain(difficulty=difficulty, flat_zone=flat_zone)

    def get_pad_info(self):
        """Get landing pad position and size."""
        return {
            'x': self.landing_pad.x,
            'y': self.landing_pad.y,
            'width': self.landing_pad.width,
            'height': self.landing_pad.height,
            'center_x': self.landing_pad.get_center_x()
        }

    def get_terrain_height(self, x):
        """Get terrain height at given X coordinate."""
        return self.terrain.get_height_at(x)

    def get_ship_start_offset(self):
        """
        Calculate horizontal offset for ship starting position.
        Level 1 starts above pad, higher levels add lateral offset.

        Returns:
            X offset in pixels (positive = right of pad, negative = left)
        """
        if self.difficulty <= 1:
            return 0  # Level 1: start directly above pad

        # Calculate offset based on difficulty
        from constants import LATERAL_OFFSET_PER_LEVEL, MAX_LATERAL_OFFSET

        base_offset = (self.difficulty - 1) * LATERAL_OFFSET_PER_LEVEL
        offset = min(base_offset, MAX_LATERAL_OFFSET)

        # Randomly choose left or right
        direction = random.choice([-1, 1])

        # Make sure ship starts on screen
        pad_center = self.landing_pad.get_center_x()
        proposed_x = pad_center + (offset * direction)

        # Clamp to screen bounds with margin
        margin = 50
        if proposed_x < margin:
            direction = 1  # Force right
        elif proposed_x > SCREEN_WIDTH - margin:
            direction = -1  # Force left

        return offset * direction

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
