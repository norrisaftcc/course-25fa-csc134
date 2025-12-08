# Orbital Delivery: Product Requirements Document

## Project Overview

**Concept:** A Lunar Lander-style game where the player delivers AI-powered packages from orbit to planetary surfaces. Packages rate their delivery experience 1-5 stars based on how they were handled.

**Purpose:** Serve as a teaching example of modular Python game architecture, demonstrating separation of concerns and clean code organization even in a language outside the core CSC 134 curriculum.

**Tech Stack:** Python 3.x with Pygame. External logic modules to maintain readable, teachable code structure.

## Core Gameplay

### Controls
| Input | Action |
|-------|--------|
| W | Main thruster (applies upward force relative to ship orientation) |
| A | Rotate counter-clockwise |
| D | Rotate clockwise |

### Physics Model
- Simplified arcade gravity (constant downward acceleration)
- Vacuum environment (no atmospheric drag)
- Momentum-based movement (thrust adds to velocity, doesn't set it)
- No orbital mechanics—gravity pulls straight down

### Win/Lose Conditions
- **Successful delivery:** Land on designated pad with velocity below damage threshold
- **Failed delivery:** Crash (excessive landing velocity) or miss the landing zone
- **Game over:** Out of fuel mid-descent

## Package Rating System

Each package evaluates its delivery based on specific criteria and generates a 1-5 star rating with a brief text review.

### MVP Package Types

| Type | Rating Criteria | What They Care About |
|------|-----------------|---------------------|
| **Fragile** | Delta-v experienced (total acceleration applied during descent) | Smooth, gentle handling |
| **Urgent** | Time from release to landing | Speed of delivery |

### Rating Calculation

**Fragile Packages:**
```
total_delta_v = sum of all acceleration magnitudes applied
5 stars: < threshold_low
4 stars: < threshold_medium  
3 stars: < threshold_high
2 stars: < threshold_critical
1 star:  >= threshold_critical (or crash)
```

**Urgent Packages:**
```
delivery_time = landing_timestamp - release_timestamp
5 stars: < time_excellent
4 stars: < time_good
3 stars: < time_acceptable
2 stars: < time_slow
1 star:  >= time_slow (or crash)
```

### Review Generation (Mad Libs)

Reviews are constructed from templates with slots filled based on rating and package type.

**Example Templates (Fragile):**
- 5★: "Pristine delivery. {positive_adjective} handling throughout. Would ship again."
- 3★: "Arrived intact, but felt {negative_sensation} during descent. {neutral_closing}"
- 1★: "I am {number} pieces now. {complaint}"

**Word Banks:**
```python
positive_adjectives = ["Immaculate", "Butter-smooth", "Professional", "Delightful"]
negative_sensations = ["several concerning jolts", "like a tumble dryer", "my life flash"]
complaints = ["This is fine.", "I contained antiques.", "Do you even have a license?"]
```

## Game Flow

```
┌─────────────┐
│   ORBIT     │  Player receives package info, sees landing zone
└──────┬──────┘
       │ Player initiates descent
       ▼
┌─────────────┐
│   DESCENT   │  Active gameplay - thrust, rotate, manage fuel
└──────┬──────┘
       │ Landing or crash
       ▼
┌─────────────┐
│   RATING    │  Package displays stars + review text
└──────┬──────┘
       │ Continue or quit
       ▼
┌─────────────┐
│ NEXT PACKAGE│  New package type, adjusted difficulty
└─────────────┘
```

## Architecture

### File Structure
```
orbital_delivery/
├── main.py              # Entry point, game loop, Pygame setup
├── physics.py           # Pure functions: gravity, thrust, collision
├── ship.py              # Ship state and rendering
├── package.py           # Package types, rating logic, review generation
├── level.py             # Landing zones, terrain, difficulty scaling
├── ui.py                # HUD, menus, rating display
├── constants.py         # Tuning values, thresholds, word banks
└── assets/
    ├── sprites/
    └── sounds/
```

### Design Principles Demonstrated

| Principle | Where It Appears |
|-----------|------------------|
| **Single Responsibility** | physics.py does math only, package.py handles rating only |
| **Pure Functions** | Physics calculations take state in, return new state, no side effects |
| **Separation of Concerns** | Game logic vs. rendering vs. input handling in distinct modules |
| **Data-Driven Design** | Thresholds and word banks in constants.py, not hardcoded |
| **State Machine** | Game phases as explicit states with defined transitions |

### Key Interfaces

**Physics Module:**
```python
def apply_gravity(velocity: Vector2, dt: float) -> Vector2
def apply_thrust(velocity: Vector2, ship_angle: float, thrust_power: float, dt: float) -> Vector2
def check_landing(position: Vector2, velocity: Vector2, landing_zone: Rect) -> LandingResult
```

**Package Module:**
```python
def calculate_rating(package_type: str, metrics: DeliveryMetrics) -> int
def generate_review(package_type: str, rating: int) -> str
```

## MVP Scope

### In Scope
- Single ship with thrust and rotation
- Two package types (Fragile, Urgent)
- One terrain/landing zone per run
- Star rating with generated review
- Basic fuel mechanic
- Functional HUD (fuel, altitude, velocity, package info)

### Out of Scope (Future)
- Multiple delivery stops per descent
- Additional package types (Heavy, Confidential, etc.)
- Persistent scoring/career mode
- Terrain variety
- Sound effects and music
- Particle effects for thrust

## Tuning Parameters

All values in `constants.py` for easy adjustment:

```python
# Physics
GRAVITY = 0.1
THRUST_POWER = 0.2
ROTATION_SPEED = 3.0
MAX_LANDING_VELOCITY = 2.0

# Fuel
STARTING_FUEL = 100.0
FUEL_BURN_RATE = 0.5

# Fragile rating thresholds (total delta-v)
FRAGILE_EXCELLENT = 50
FRAGILE_GOOD = 100
FRAGILE_ACCEPTABLE = 150
FRAGILE_POOR = 200

# Urgent rating thresholds (seconds)
URGENT_EXCELLENT = 10
URGENT_GOOD = 15
URGENT_ACCEPTABLE = 20
URGENT_POOR = 30
```

## Success Criteria

1. **Playable:** Ship controls feel responsive; landing is challenging but achievable
2. **Readable:** A CSC 134 student can follow the code structure and understand module boundaries
3. **Teachable:** Architecture demonstrates principles covered in Weeks 13-14 (SOLID, separation of concerns)
4. **Fun:** The rating/review system creates replayability and "one more try" motivation

## Open Questions

- [ ] Should fuel display be numeric or gauge-based?
- [ ] Does the ship explode on crash, or just crumple sadly?
- [ ] Starting altitude: fixed or randomized within range?
- [ ] Should packages have visible personality before delivery (nervous fragile box, impatient urgent box)?
