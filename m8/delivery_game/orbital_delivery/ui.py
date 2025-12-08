# ui.py - HUD, menus, and rating display

import pygame
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    WHITE, GREEN, RED, YELLOW, ORANGE, GRAY, BLACK,
    STARTING_FUEL, MAX_LANDING_VELOCITY
)


class HUD:
    """Heads-up display showing fuel, altitude, velocity, and package info."""

    def __init__(self):
        """Initialize HUD with fonts."""
        pygame.font.init()
        self.font_small = pygame.font.Font(None, 24)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_large = pygame.font.Font(None, 48)

    def draw(self, surface, ship, package, altitude):
        """
        Draw the HUD elements.

        Args:
            surface: Pygame surface to draw on
            ship: Ship object with fuel, velocity
            package: Current package being delivered
            altitude: Current altitude above ground
        """
        # Left panel - Ship info
        self._draw_fuel_gauge(surface, ship.fuel, 10, 10)
        self._draw_velocity(surface, ship.vel_x, ship.vel_y, 10, 70)
        self._draw_altitude(surface, altitude, 10, 130)

        # Right panel - Package info
        self._draw_package_info(surface, package, SCREEN_WIDTH - 200, 10)

    def _draw_fuel_gauge(self, surface, fuel, x, y):
        """Draw fuel gauge with bar and text."""
        # Label
        label = self.font_small.render("FUEL", True, WHITE)
        surface.blit(label, (x, y))

        # Gauge background
        gauge_width = 150
        gauge_height = 20
        pygame.draw.rect(surface, GRAY, (x, y + 20, gauge_width, gauge_height))

        # Fuel level
        fuel_percent = fuel / STARTING_FUEL
        fuel_width = int(gauge_width * fuel_percent)

        # Color based on fuel level
        if fuel_percent > 0.5:
            color = GREEN
        elif fuel_percent > 0.25:
            color = YELLOW
        else:
            color = RED

        pygame.draw.rect(surface, color, (x, y + 20, fuel_width, gauge_height))

        # Border
        pygame.draw.rect(surface, WHITE, (x, y + 20, gauge_width, gauge_height), 2)

        # Percentage text
        pct_text = self.font_small.render(f"{fuel:.0f}%", True, WHITE)
        surface.blit(pct_text, (x + gauge_width + 10, y + 22))

    def _draw_velocity(self, surface, vel_x, vel_y, x, y):
        """Draw velocity information."""
        import math
        speed = math.sqrt(vel_x**2 + vel_y**2)

        # Label
        label = self.font_small.render("VELOCITY", True, WHITE)
        surface.blit(label, (x, y))

        # Color based on landing safety
        if speed < MAX_LANDING_VELOCITY * 0.5:
            color = GREEN
        elif speed < MAX_LANDING_VELOCITY:
            color = YELLOW
        else:
            color = RED

        # Speed value
        speed_text = self.font_medium.render(f"{speed:.1f}", True, color)
        surface.blit(speed_text, (x, y + 18))

        # Direction indicator
        dir_text = self.font_small.render(f"({vel_x:.1f}, {vel_y:.1f})", True, GRAY)
        surface.blit(dir_text, (x + 60, y + 22))

    def _draw_altitude(self, surface, altitude, x, y):
        """Draw altitude display."""
        # Label
        label = self.font_small.render("ALTITUDE", True, WHITE)
        surface.blit(label, (x, y))

        # Value
        alt_text = self.font_medium.render(f"{altitude:.0f}m", True, WHITE)
        surface.blit(alt_text, (x, y + 18))

    def _draw_package_info(self, surface, package, x, y):
        """Draw package information."""
        if package is None:
            return

        # Package type header
        if package.package_type == "fragile":
            color = ORANGE
            header = "FRAGILE"
        else:
            color = YELLOW
            header = "URGENT"

        header_text = self.font_medium.render(header, True, color)
        surface.blit(header_text, (x, y))

        # Package name
        name_text = self.font_small.render(package.name, True, WHITE)
        surface.blit(name_text, (x, y + 28))

        # Relevant metric
        if package.package_type == "fragile":
            metric = f"Stress: {package.total_delta_v:.1f}"
        else:
            metric = f"Time: {package.delivery_time:.1f}s"

        metric_text = self.font_small.render(metric, True, GRAY)
        surface.blit(metric_text, (x, y + 50))


class MenuScreen:
    """Title and menu screens."""

    def __init__(self):
        """Initialize menu fonts."""
        pygame.font.init()
        self.font_title = pygame.font.Font(None, 64)
        self.font_subtitle = pygame.font.Font(None, 32)
        self.font_instruction = pygame.font.Font(None, 24)

    def draw_title(self, surface):
        """Draw the title screen."""
        surface.fill(BLACK)

        # Title
        title = self.font_title.render("ORBITAL DELIVERY", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        surface.blit(title, title_rect)

        # Subtitle
        subtitle = self.font_subtitle.render("AI Package Delivery Service", True, GRAY)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 200))
        surface.blit(subtitle, subtitle_rect)

        # Instructions
        instructions = [
            "Controls:",
            "W - Main Thruster",
            "A - Rotate Left",
            "D - Rotate Right",
            "",
            "Land gently on the green pad.",
            "Your package will rate the delivery!",
            "",
            "Press SPACE to start"
        ]

        y_offset = 280
        for line in instructions:
            if line.startswith("Controls"):
                text = self.font_subtitle.render(line, True, YELLOW)
            elif line.startswith("Press"):
                text = self.font_subtitle.render(line, True, GREEN)
            else:
                text = self.font_instruction.render(line, True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            surface.blit(text, text_rect)
            y_offset += 30

    def draw_orbit(self, surface, package):
        """Draw the pre-descent orbit screen."""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(200)
        surface.blit(overlay, (0, 0))

        # Header
        header = self.font_title.render("INCOMING DELIVERY", True, YELLOW)
        header_rect = header.get_rect(center=(SCREEN_WIDTH // 2, 100))
        surface.blit(header, header_rect)

        # Package info
        if package:
            type_color = ORANGE if package.package_type == "fragile" else YELLOW

            pkg_type = self.font_subtitle.render(
                f"Type: {package.package_type.upper()}", True, type_color)
            pkg_type_rect = pkg_type.get_rect(center=(SCREEN_WIDTH // 2, 180))
            surface.blit(pkg_type, pkg_type_rect)

            pkg_name = self.font_subtitle.render(package.name, True, WHITE)
            pkg_name_rect = pkg_name.get_rect(center=(SCREEN_WIDTH // 2, 220))
            surface.blit(pkg_name, pkg_name_rect)

            # What the package cares about
            if package.package_type == "fragile":
                care_text = "Cares about: Smooth handling"
            else:
                care_text = "Cares about: Speed"
            care = self.font_instruction.render(care_text, True, GRAY)
            care_rect = care.get_rect(center=(SCREEN_WIDTH // 2, 260))
            surface.blit(care, care_rect)

        # Start prompt
        prompt = self.font_subtitle.render("Press SPACE to begin descent", True, GREEN)
        prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH // 2, 400))
        surface.blit(prompt, prompt_rect)


class RatingScreen:
    """Display for showing package rating and review."""

    def __init__(self):
        """Initialize rating screen fonts."""
        pygame.font.init()
        self.font_title = pygame.font.Font(None, 48)
        self.font_stars = pygame.font.Font(None, 72)
        self.font_review = pygame.font.Font(None, 28)
        self.font_instruction = pygame.font.Font(None, 24)

    def draw(self, surface, package, landed_successfully):
        """
        Draw the rating screen.

        Args:
            surface: Pygame surface
            package: The package that was delivered
            landed_successfully: Boolean indicating clean landing
        """
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(220)
        surface.blit(overlay, (0, 0))

        # Header
        if landed_successfully:
            header_text = "DELIVERY COMPLETE"
            header_color = GREEN
        else:
            header_text = "DELIVERY FAILED"
            header_color = RED

        header = self.font_title.render(header_text, True, header_color)
        header_rect = header.get_rect(center=(SCREEN_WIDTH // 2, 100))
        surface.blit(header, header_rect)

        if package:
            # Package name
            name = self.font_review.render(f"Package: {package.name}", True, WHITE)
            name_rect = name.get_rect(center=(SCREEN_WIDTH // 2, 150))
            surface.blit(name, name_rect)

            # Star rating
            rating = package.calculate_rating()
            stars = "*" * rating + "." * (5 - rating)
            stars_text = self.font_stars.render(stars, True, YELLOW)
            stars_rect = stars_text.get_rect(center=(SCREEN_WIDTH // 2, 220))
            surface.blit(stars_text, stars_rect)

            # Numeric rating
            rating_text = self.font_review.render(f"{rating}/5 Stars", True, GRAY)
            rating_rect = rating_text.get_rect(center=(SCREEN_WIDTH // 2, 270))
            surface.blit(rating_text, rating_rect)

            # Review text (word-wrapped)
            review = package.generate_review()
            self._draw_wrapped_text(surface, review, SCREEN_WIDTH // 2, 330, 600)

        # Continue prompt
        prompt = self.font_instruction.render(
            "Press SPACE for next delivery  |  ESC to quit", True, GREEN)
        prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH // 2, 500))
        surface.blit(prompt, prompt_rect)

    def _draw_wrapped_text(self, surface, text, center_x, y, max_width):
        """Draw text wrapped to max_width, centered."""
        words = text.split(' ')
        lines = []
        current_line = []

        for word in words:
            test_line = ' '.join(current_line + [word])
            test_surface = self.font_review.render(test_line, True, WHITE)
            if test_surface.get_width() <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        # Draw each line centered
        line_height = 30
        for i, line in enumerate(lines):
            text_surface = self.font_review.render(line, True, WHITE)
            text_rect = text_surface.get_rect(center=(center_x, y + i * line_height))
            surface.blit(text_surface, text_rect)


class GameOverScreen:
    """Screen for when the player runs out of fuel."""

    def __init__(self):
        pygame.font.init()
        self.font_title = pygame.font.Font(None, 64)
        self.font_text = pygame.font.Font(None, 32)

    def draw(self, surface):
        """Draw game over screen."""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(230)
        surface.blit(overlay, (0, 0))

        # Title
        title = self.font_title.render("OUT OF FUEL", True, RED)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 200))
        surface.blit(title, title_rect)

        # Message
        message = self.font_text.render("The package drifts forever into the void...", True, GRAY)
        message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, 280))
        surface.blit(message, message_rect)

        # Prompt
        prompt = self.font_text.render("Press SPACE to try again  |  ESC to quit", True, WHITE)
        prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH // 2, 400))
        surface.blit(prompt, prompt_rect)
