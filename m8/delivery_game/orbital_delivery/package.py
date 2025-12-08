# package.py - Package types, rating logic, and review generation
# Each package evaluates its delivery and generates a review

import random
from constants import (
    FRAGILE_EXCELLENT, FRAGILE_GOOD, FRAGILE_ACCEPTABLE, FRAGILE_POOR,
    URGENT_EXCELLENT, URGENT_GOOD, URGENT_ACCEPTABLE, URGENT_POOR,
    POSITIVE_ADJECTIVES, NEGATIVE_SENSATIONS, NEUTRAL_CLOSINGS,
    COMPLAINTS, URGENT_PRAISE, URGENT_COMPLAINTS
)


class Package:
    """
    Represents a package being delivered.
    Tracks delivery metrics and generates ratings/reviews.
    """

    def __init__(self, package_type="fragile"):
        """
        Initialize a package.

        Args:
            package_type: Either "fragile" or "urgent"
        """
        self.package_type = package_type.lower()
        self.total_delta_v = 0.0  # Total acceleration experienced
        self.delivery_time = 0.0  # Time in seconds
        self.crashed = False

        # Cached values (generated once, then reused)
        self._cached_review = None
        self._cached_rating = None

        # Package personality (for display)
        self.names = {
            "fragile": ["Delicate Vase", "Antique Clock", "Crystal Set",
                        "Grandma's Ashes", "Prototype Sensor", "Fine China"],
            "urgent": ["Vital Organs", "Pizza (HOT)", "Classified Intel",
                       "Unstable Isotope", "Birthday Cake", "Live Specimen"]
        }
        self.name = random.choice(self.names.get(self.package_type, ["Mystery Box"]))

    def add_delta_v(self, delta_v):
        """Record acceleration experienced during delivery."""
        self.total_delta_v += delta_v

    def add_time(self, seconds):
        """Add to delivery time."""
        self.delivery_time += seconds

    def mark_crashed(self):
        """Mark that the delivery ended in a crash."""
        self.crashed = True

    def calculate_rating(self):
        """
        Calculate star rating (1-5) based on package type and delivery metrics.

        Returns:
            Integer from 1 to 5
        """
        if self.crashed:
            return 1

        if self.package_type == "fragile":
            return self._rate_fragile()
        elif self.package_type == "urgent":
            return self._rate_urgent()
        else:
            return 3  # Default for unknown types

    def _rate_fragile(self):
        """Rate based on total delta-v (acceleration) experienced."""
        dv = self.total_delta_v
        if dv < FRAGILE_EXCELLENT:
            return 5
        elif dv < FRAGILE_GOOD:
            return 4
        elif dv < FRAGILE_ACCEPTABLE:
            return 3
        elif dv < FRAGILE_POOR:
            return 2
        else:
            return 1

    def _rate_urgent(self):
        """Rate based on delivery time."""
        time = self.delivery_time
        if time < URGENT_EXCELLENT:
            return 5
        elif time < URGENT_GOOD:
            return 4
        elif time < URGENT_ACCEPTABLE:
            return 3
        elif time < URGENT_POOR:
            return 2
        else:
            return 1

    def generate_review(self):
        """
        Generate a text review based on rating and package type.
        Reviews are cached after first generation to prevent flickering.

        Returns:
            String containing the package's review
        """
        # Return cached review if already generated
        if self._cached_review is not None:
            return self._cached_review

        rating = self.calculate_rating()

        if self.crashed:
            self._cached_review = self._generate_crash_review()
        elif self.package_type == "fragile":
            self._cached_review = self._generate_fragile_review(rating)
        elif self.package_type == "urgent":
            self._cached_review = self._generate_urgent_review(rating)
        else:
            self._cached_review = "Delivery completed. No comment."

        return self._cached_review

    def _generate_crash_review(self):
        """Generate review for a crashed delivery."""
        templates = [
            f"I am now in {random.randint(3, 47)} pieces. {random.choice(COMPLAINTS)}",
            f"Well, that happened. {random.choice(COMPLAINTS)}",
            f"*sounds of settling debris* {random.choice(COMPLAINTS)}",
            f"I regret choosing this carrier. {random.choice(COMPLAINTS)}",
            f"My contents are now modern art. {random.choice(COMPLAINTS)}"
        ]
        return random.choice(templates)

    def _generate_fragile_review(self, rating):
        """Generate review for fragile package based on rating."""
        if rating == 5:
            adj = random.choice(POSITIVE_ADJECTIVES)
            return f"Pristine delivery! {adj} handling throughout. Would ship again!"
        elif rating == 4:
            adj = random.choice(POSITIVE_ADJECTIVES)
            return f"{adj} work overall. Minor bumps, but I'm intact. Recommended."
        elif rating == 3:
            sensation = random.choice(NEGATIVE_SENSATIONS)
            closing = random.choice(NEUTRAL_CLOSINGS)
            return f"Arrived intact, but felt {sensation} during descent. {closing}"
        elif rating == 2:
            sensation = random.choice(NEGATIVE_SENSATIONS)
            complaint = random.choice(COMPLAINTS)
            return f"Experienced {sensation}. Some internal damage likely. {complaint}"
        else:
            complaint = random.choice(COMPLAINTS)
            return f"I survived, barely. Felt like {random.choice(NEGATIVE_SENSATIONS)}. {complaint}"

    def _generate_urgent_review(self, rating):
        """Generate review for urgent package based on rating."""
        time_str = f"{self.delivery_time:.1f}s"
        if rating == 5:
            praise = random.choice(URGENT_PRAISE)
            return f"{praise} Delivered in {time_str}. Exceptional speed!"
        elif rating == 4:
            return f"Good hustle! {time_str} delivery time. I approve."
        elif rating == 3:
            return f"Adequate timing at {time_str}. I've seen faster, but acceptable."
        elif rating == 2:
            complaint = random.choice(URGENT_COMPLAINTS)
            return f"{time_str}? {complaint}"
        else:
            complaint = random.choice(URGENT_COMPLAINTS)
            return f"{time_str} to deliver?! {complaint}"

    def get_description(self):
        """Get a short description for the HUD."""
        if self.package_type == "fragile":
            return f"FRAGILE: {self.name}\nHandle with care!"
        else:
            return f"URGENT: {self.name}\nTime is critical!"

    def get_stars_string(self):
        """Get a string of star characters representing the rating."""
        rating = self.calculate_rating()
        return "*" * rating + "." * (5 - rating)


def create_random_package():
    """Create a random package type."""
    package_type = random.choice(["fragile", "urgent"])
    return Package(package_type)
