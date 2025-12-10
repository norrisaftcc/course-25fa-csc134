# physics.py - Pure functions for gravity, thrust, and collision
# No side effects - takes state in, returns new state

import math
from constants import GRAVITY, THRUST_POWER, MAX_LANDING_VELOCITY


def apply_gravity(vel_x, vel_y, dt=1.0):
    """
    Apply gravitational acceleration to velocity.

    Args:
        vel_x: Current horizontal velocity
        vel_y: Current vertical velocity
        dt: Delta time multiplier (default 1.0 for frame-based)

    Returns:
        Tuple of (new_vel_x, new_vel_y)
    """
    return vel_x, vel_y + GRAVITY * dt


def apply_thrust(vel_x, vel_y, angle_degrees, thrust_power=THRUST_POWER, dt=1.0):
    """
    Apply thrust in the direction the ship is facing.
    Ship angle 0 = pointing up, positive = clockwise rotation.

    Args:
        vel_x: Current horizontal velocity
        vel_y: Current vertical velocity
        angle_degrees: Ship's current angle in degrees (0 = up)
        thrust_power: Force of thrust
        dt: Delta time multiplier

    Returns:
        Tuple of (new_vel_x, new_vel_y, delta_v) where delta_v is acceleration magnitude
    """
    # Convert angle to radians, offset so 0 degrees = up
    angle_rad = math.radians(angle_degrees - 90)

    # Calculate thrust components
    thrust_x = math.cos(angle_rad) * thrust_power * dt
    thrust_y = math.sin(angle_rad) * thrust_power * dt

    # Delta-v is the magnitude of acceleration applied
    delta_v = math.sqrt(thrust_x**2 + thrust_y**2)

    return vel_x + thrust_x, vel_y + thrust_y, delta_v


def update_position(x, y, vel_x, vel_y, dt=1.0):
    """
    Update position based on velocity.

    Args:
        x, y: Current position
        vel_x, vel_y: Current velocity
        dt: Delta time multiplier

    Returns:
        Tuple of (new_x, new_y)
    """
    return x + vel_x * dt, y + vel_y * dt


def check_landing(x, y, vel_x, vel_y, pad_x, pad_y, pad_width, pad_height):
    """
    Check if ship has landed on the pad.

    Args:
        x, y: Ship position (center bottom of ship)
        vel_x, vel_y: Ship velocity
        pad_x, pad_y: Landing pad top-left corner
        pad_width, pad_height: Landing pad dimensions

    Returns:
        Dictionary with landing result:
        - 'status': 'flying', 'landed', 'crashed', or 'missed'
        - 'on_pad': Boolean, whether ship is over the pad
        - 'velocity_ok': Boolean, whether landing velocity is safe
    """
    result = {
        'status': 'flying',
        'on_pad': False,
        'velocity_ok': False
    }

    # Check if ship has reached ground level
    if y < pad_y:
        return result  # Still in the air

    # Check if ship is over the landing pad
    on_pad = pad_x <= x <= pad_x + pad_width
    result['on_pad'] = on_pad

    # Check landing velocity
    landing_speed = math.sqrt(vel_x**2 + vel_y**2)
    velocity_ok = landing_speed <= MAX_LANDING_VELOCITY
    result['velocity_ok'] = velocity_ok

    # Determine outcome
    if on_pad and velocity_ok:
        result['status'] = 'landed'
    elif on_pad and not velocity_ok:
        result['status'] = 'crashed'
    else:
        result['status'] = 'missed'

    return result


def get_speed(vel_x, vel_y):
    """Calculate total speed from velocity components."""
    return math.sqrt(vel_x**2 + vel_y**2)


def get_altitude(y, ground_y):
    """Calculate altitude above ground."""
    return max(0, ground_y - y)


def check_terrain_collision(x, y, terrain_height_func, ship_margin=10):
    """
    Check if ship has collided with terrain.

    Args:
        x, y: Ship position (center)
        terrain_height_func: Function that returns terrain Y at given X
        ship_margin: Collision buffer around ship center

    Returns:
        True if ship has collided with terrain, False otherwise
    """
    # Check collision at ship center and slightly to each side
    check_points = [x - ship_margin, x, x + ship_margin]

    for check_x in check_points:
        terrain_y = terrain_height_func(check_x)
        if y >= terrain_y:
            return True

    return False
