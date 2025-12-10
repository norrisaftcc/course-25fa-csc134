# constants.py - Tuning values, thresholds, word banks
# All game parameters in one place for easy adjustment

# =============================================================================
# DISPLAY
# =============================================================================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (100, 149, 237)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# =============================================================================
# PHYSICS
# =============================================================================
GRAVITY = 0.05              # Downward acceleration per frame
THRUST_POWER = 0.12         # Upward acceleration when thrusting
ROTATION_SPEED = 3.0        # Degrees per frame
MAX_LANDING_VELOCITY = 2.0  # Maximum safe landing speed
FALLING_FAST_VELOCITY = 5.0 # Velocity threshold for "falling fast" game over

# =============================================================================
# FUEL
# =============================================================================
STARTING_FUEL = 100.0
FUEL_BURN_RATE = 0.3        # Fuel consumed per frame while thrusting

# =============================================================================
# SHIP
# =============================================================================
SHIP_START_X = 400
SHIP_START_Y = 80
SHIP_SIZE = 20              # Ship triangle size

# =============================================================================
# LANDING ZONE
# =============================================================================
LANDING_PAD_WIDTH = 100
LANDING_PAD_HEIGHT = 10
LANDING_PAD_Y = 550         # Y position of landing pad

# =============================================================================
# TERRAIN DIFFICULTY
# =============================================================================
TERRAIN_HEIGHT_BASE = 5          # Base terrain variation (pixels) at level 1
TERRAIN_HEIGHT_PER_LEVEL = 10    # Additional height variation per level
MAX_TERRAIN_HEIGHT = 80          # Cap on terrain roughness
TERRAIN_FLAT_ZONE_MARGIN = 30    # Extra flat space on each side of landing pad
TERRAIN_TRANSITION_WIDTH = 40    # Pixels to smooth terrain into flat zones

# Terrain wave parameters (for procedural generation)
TERRAIN_WAVE_PRIMARY_FREQ = 0.01     # Large hills frequency
TERRAIN_WAVE_PRIMARY_AMP = 0.6       # Large hills amplitude multiplier
TERRAIN_WAVE_SECONDARY_FREQ = 0.025  # Medium features frequency
TERRAIN_WAVE_SECONDARY_AMP = 0.3     # Medium features amplitude multiplier
TERRAIN_WAVE_TERTIARY_FREQ = 0.05    # Small bumps frequency
TERRAIN_WAVE_TERTIARY_AMP = 0.1      # Small bumps amplitude multiplier

# =============================================================================
# SHIP STARTING POSITION (Lateral Offset)
# =============================================================================
LATERAL_OFFSET_PER_LEVEL = 60    # Pixels offset per difficulty level
MAX_LATERAL_OFFSET = 300         # Maximum starting offset from pad
SHIP_SCREEN_MARGIN = 50          # Margin from screen edge for ship positioning

# =============================================================================
# FRAGILE PACKAGE - Rating thresholds (total delta-v experienced)
# =============================================================================
FRAGILE_EXCELLENT = 30      # 5 stars
FRAGILE_GOOD = 60           # 4 stars
FRAGILE_ACCEPTABLE = 100    # 3 stars
FRAGILE_POOR = 150          # 2 stars
# Anything above POOR = 1 star

# =============================================================================
# URGENT PACKAGE - Rating thresholds (seconds)
# =============================================================================
URGENT_EXCELLENT = 8        # 5 stars
URGENT_GOOD = 12            # 4 stars
URGENT_ACCEPTABLE = 18      # 3 stars
URGENT_POOR = 25            # 2 stars
# Anything above POOR = 1 star

# =============================================================================
# REVIEW WORD BANKS
# =============================================================================
POSITIVE_ADJECTIVES = [
    "Immaculate", "Butter-smooth", "Professional", "Delightful",
    "Exceptional", "Flawless", "Superb", "Outstanding"
]

NEGATIVE_SENSATIONS = [
    "several concerning jolts",
    "like a tumble dryer",
    "my life flash before my sensors",
    "existential dread",
    "every molecule rearranging",
    "what I can only describe as violence"
]

NEUTRAL_CLOSINGS = [
    "Could be worse.",
    "I've had rougher.",
    "Acceptable, I suppose.",
    "Room for improvement.",
    "It is what it is."
]

COMPLAINTS = [
    "This is fine.",
    "I contained antiques.",
    "Do you even have a license?",
    "My warranty is void now.",
    "I'll be filing a report.",
    "Was that turbulence or malice?"
]

URGENT_PRAISE = [
    "Lightning fast!",
    "Now THAT'S what I call service!",
    "Speed demon! I love it!",
    "Barely had time to get nervous!"
]

URGENT_COMPLAINTS = [
    "I could have walked faster.",
    "Did we stop for coffee?",
    "My expiration date is concerning now.",
    "The suspense was NOT appreciated."
]

# =============================================================================
# GAME STATES
# =============================================================================
STATE_ORBIT = "orbit"
STATE_DESCENT = "descent"
STATE_LANDED = "landed"
STATE_CRASHED = "crashed"
STATE_RATING = "rating"
STATE_GAME_OVER = "game_over"
