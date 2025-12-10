# Behind The Scenes: Orbital Delivery

A technical deep-dive into how this game works, written for first and second-year CS students.

## Table of Contents

1. [The Game Loop](#1-the-game-loop)
2. [State Machines](#2-state-machines)
3. [The Physics System](#3-the-physics-system)
4. [Procedural Terrain Generation](#4-procedural-terrain-generation)
5. [The Rating System](#5-the-rating-system)
6. [Code Organization Principles](#6-code-organization-principles)
7. [Common Patterns You'll See](#7-common-patterns-youll-see)
8. [Debugging Tips](#8-debugging-tips)
9. [Exercises to Try](#9-exercises-to-try)

---

## 1. The Game Loop

Every game, from Pong to AAA titles, runs on the same fundamental concept: **the game loop**.

```
┌─────────────────────────────────────────┐
│                                         │
│    ┌──────────┐                         │
│    │  Handle  │ ◄── Check for keyboard  │
│    │  Input   │     presses, mouse, etc │
│    └────┬─────┘                         │
│         │                               │
│         ▼                               │
│    ┌──────────┐                         │
│    │  Update  │ ◄── Move things, check  │
│    │  State   │     collisions, physics │
│    └────┬─────┘                         │
│         │                               │
│         ▼                               │
│    ┌──────────┐                         │
│    │   Draw   │ ◄── Render everything   │
│    │  Frame   │     to the screen       │
│    └────┬─────┘                         │
│         │                               │
│         ▼                               │
│    ┌──────────┐                         │
│    │   Wait   │ ◄── Maintain 60 FPS     │
│    └────┬─────┘                         │
│         │                               │
│         └─────────────────────────────┘ │
│                   REPEAT                │
└─────────────────────────────────────────┘
```

In our code (`main.py`), this looks like:

```python
def run(self):
    """Main game loop."""
    while self.running:
        self.handle_events()  # Input
        self.handle_input()   # More input (held keys)
        self.update()         # Physics & logic
        self.draw()           # Render
        self.clock.tick(FPS)  # Wait (maintain 60 FPS)
```

### Why 60 FPS?

- **60 frames per second** means the loop runs 60 times every second
- Each frame lasts about **16.67 milliseconds**
- `clock.tick(60)` tells Pygame to wait if we finish early
- This keeps the game running at consistent speed on fast and slow computers

### The Input Split

Notice we have both `handle_events()` and `handle_input()`. Why?

- **Events** are one-time occurrences: "the spacebar was just pressed"
- **Input state** is continuous: "is W currently held down?"

```python
# Events: "Did they JUST press space?"
def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Do something ONCE

# Input state: "Is W being held right now?"
def handle_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        # Do this EVERY FRAME while held
```

---

## 2. State Machines

Games have different "modes" - you're on a menu, then playing, then viewing scores. We model this as a **state machine**.

```
┌─────────┐  SPACE   ┌─────────┐  SPACE   ┌─────────┐
│  TITLE  │ ───────► │  ORBIT  │ ───────► │ DESCENT │
└─────────┘          └─────────┘          └────┬────┘
     ▲                                         │
     │                                   land/ │
     │         ┌─────────┐  SPACE       crash │
     └──────── │ RATING  │ ◄───────────────────┘
       ESC     └─────────┘
```

In code, we use a simple string variable:

```python
self.state = "title"  # Can be: title, orbit, descent, rating, game_over
```

Then in `update()` and `draw()`, we check the state:

```python
def update(self):
    if self.state != STATE_DESCENT:
        return  # Only update physics during descent

    # ... physics code ...

def draw(self):
    if self.state == "title":
        self.menu.draw_title(self.screen)
    elif self.state == STATE_DESCENT:
        # Draw ship, terrain, HUD...
```

### Why Use States?

Without states, you'd have spaghetti code with flags everywhere:
```python
# BAD: Hard to follow, easy to break
if is_playing and not is_paused and not showing_menu and not game_over:
    # ...
```

With states, logic is clear:
```python
# GOOD: Each state has clear behavior
if self.state == STATE_DESCENT:
    # ...
```

---

## 3. The Physics System

The physics in `physics.py` uses **pure functions** - they take input and return output without modifying anything else.

### Gravity

```python
def apply_gravity(vel_x, vel_y, dt=1.0):
    return vel_x, vel_y + GRAVITY * dt
```

Every frame, we add a small amount to the downward velocity. That's it! Gravity in games is just "add a constant to Y velocity each frame."

- `GRAVITY = 0.05` means we add 0.05 to `vel_y` each frame
- Over 60 frames (1 second), that's +3.0 velocity
- The ship accelerates downward, just like real gravity

### Thrust

```python
def apply_thrust(vel_x, vel_y, angle_degrees, thrust_power, dt=1.0):
    angle_rad = math.radians(angle_degrees - 90)
    thrust_x = math.cos(angle_rad) * thrust_power * dt
    thrust_y = math.sin(angle_rad) * thrust_power * dt
    # ...
    return vel_x + thrust_x, vel_y + thrust_y, delta_v
```

Thrust uses **trigonometry** to convert an angle into X and Y components:

```
        0° (up)
         │
         │    thrust_y = sin(angle) × power
  270° ──┼── 90°
         │    thrust_x = cos(angle) × power
         │
       180°
```

The `-90` offset is because in our game, 0° means pointing up, but in standard trig, 0° means pointing right.

### Why "Pure Functions"?

Pure functions make code easier to test and debug:

```python
# We can test physics in isolation:
new_vx, new_vy = apply_gravity(0, 0)
assert new_vy == GRAVITY  # Easy to verify!

# No hidden state to worry about
# Same input ALWAYS gives same output
```

---

## 4. Procedural Terrain Generation

The terrain is generated using **layered sine waves**, a technique used in many games for natural-looking landscapes.

### The Basic Idea

A single sine wave makes smooth hills:
```
     ~~~~
    ~    ~
   ~      ~
  ~        ~~~~
```

But it looks artificial. Layer multiple frequencies for natural terrain:

```python
# Primary wave: BIG hills (low frequency)
y += sin(x * 0.01) * height * 0.6

# Secondary wave: medium bumps
y += sin(x * 0.025) * height * 0.3

# Tertiary wave: small details
y += sin(x * 0.05) * height * 0.1
```

The numbers:
- `0.01, 0.025, 0.05` - Frequencies (how often hills occur)
- `0.6, 0.3, 0.1` - Amplitudes (how much each layer contributes)

### The Flat Zone Problem

We need a flat area for the landing pad! The solution:

1. Generate terrain normally
2. Identify the "flat zone" around the pad
3. Force those points to the base height
4. Smooth the transition with **interpolation**

```python
# Smoothstep interpolation (etically eases in and out)
t = t * t * (3 - 2 * t)
new_y = terrain_y * (1 - t) + flat_y * t
```

This creates a gradual ramp from hilly terrain into the flat landing zone.

---

## 5. The Rating System

The package rating system demonstrates **polymorphism** - different package types calculate ratings differently.

### Rating Algorithm

```python
def calculate_rating(self):
    if self.crashed:
        return 1  # Crash = 1 star, always

    if self.package_type == "fragile":
        return self._rate_fragile()  # Based on delta-v
    elif self.package_type == "urgent":
        return self._rate_urgent()   # Based on time
```

### Fragile: Delta-V Based

"Delta-v" (Δv) means "change in velocity" - how much acceleration was applied.

```python
def _rate_fragile(self):
    dv = self.total_delta_v
    if dv < 30:   return 5  # Excellent
    elif dv < 60: return 4  # Good
    elif dv < 100: return 3  # Acceptable
    # ...
```

Every time you thrust, we add to `total_delta_v`:
```python
if self.ship.thrusting:
    # ... apply thrust ...
    self.package.add_delta_v(delta_v)
```

### Urgent: Time Based

Simple timer - how many seconds from start to landing?

```python
def _rate_urgent(self):
    time = self.delivery_time
    if time < 8:  return 5   # Under 8 seconds = perfect
    elif time < 12: return 4
    # ...
```

### Review Generation: Mad Libs Style

Reviews are templates with slots filled randomly:

```python
def _generate_fragile_review(self, rating):
    if rating == 5:
        adj = random.choice(["Immaculate", "Butter-smooth", "Professional"])
        return f"Pristine delivery! {adj} handling throughout."
```

**Important:** Reviews are cached to prevent flickering:
```python
def generate_review(self):
    if self._cached_review is not None:
        return self._cached_review  # Return same review every time

    # Generate once, cache it
    self._cached_review = self._generate_review_internal()
    return self._cached_review
```

---

## 6. Code Organization Principles

### Single Responsibility Principle

Each module does ONE thing:

| Module | Responsibility | What it does NOT do |
|--------|---------------|---------------------|
| `physics.py` | Calculate positions/velocities | Draw anything |
| `ship.py` | Manage ship state | Know about packages |
| `package.py` | Rate deliveries | Draw UI |
| `ui.py` | Display information | Calculate physics |

### Data-Driven Design

All tuning values are in `constants.py`:

```python
# Easy to tweak without touching logic
GRAVITY = 0.05
THRUST_POWER = 0.12
MAX_LANDING_VELOCITY = 2.0
FRAGILE_EXCELLENT = 30
```

**Why?**
- Game designers can adjust values without reading code
- Prevents "magic numbers" scattered everywhere
- Easy to experiment with balance

### Separation of Concerns

```
┌──────────────────────────────────────────────────────────┐
│                        main.py                            │
│  (Coordinates everything, but does minimal actual work)  │
└────────────┬─────────────────────────────┬───────────────┘
             │                             │
    ┌────────▼────────┐           ┌────────▼────────┐
    │    physics.py   │           │      ui.py      │
    │  (Math only)    │           │ (Display only)  │
    └─────────────────┘           └─────────────────┘
             │                             │
    ┌────────▼────────┐           ┌────────▼────────┐
    │    ship.py      │           │   package.py    │
    │ (Ship state)    │           │ (Rating logic)  │
    └─────────────────┘           └─────────────────┘
```

---

## 7. Common Patterns You'll See

### The Update-Draw Pattern

Almost every game object follows this:
```python
class Ship:
    def update(self):  # Change state
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self, surface):  # Show state
        pygame.draw.polygon(surface, WHITE, self.get_points())
```

### Caching Expensive Operations

When something is expensive or random, calculate once and store it:
```python
# BAD: Generates new debris every frame (60x per second!)
def draw_crashed(self):
    for i in range(4):
        pos = random.randint(-20, 20)  # Different every frame!
        # draw...

# GOOD: Generate once, reuse
def draw_crashed(self):
    if self._debris is None:
        self._debris = [random.randint(-20, 20) for _ in range(4)]
    for pos in self._debris:
        # draw...
```

### Guard Clauses

Return early instead of deep nesting:
```python
# BAD: Deep nesting
def update(self):
    if self.state == STATE_DESCENT:
        if self.ship.fuel > 0:
            if self.ship.thrusting:
                # do stuff...

# GOOD: Guard clauses
def update(self):
    if self.state != STATE_DESCENT:
        return
    if self.ship.fuel <= 0:
        return
    if not self.ship.thrusting:
        return
    # do stuff...
```

---

## 8. Debugging Tips

### Print Statements Are Your Friend

```python
# Temporary debug output
print(f"Ship pos: ({self.ship.x:.1f}, {self.ship.y:.1f})")
print(f"Velocity: ({self.ship.vel_x:.2f}, {self.ship.vel_y:.2f})")
print(f"State: {self.state}")
```

### Visualize Collision Boxes

```python
# Draw collision areas to see what's happening
pygame.draw.rect(surface, RED, landing_pad_rect, 1)  # 1 = outline only
```

### Slow Down Time

```python
# Temporarily reduce FPS to see what's happening
self.clock.tick(10)  # 10 FPS instead of 60
```

### Test Modules Independently

```python
# Test physics without running the game
python -c "
from physics import apply_gravity
vx, vy = apply_gravity(0, 0)
print(f'After gravity: vy = {vy}')
"
```

---

## 9. Exercises to Try

### Beginner

1. **Change the gravity** - Make it moon-like (lower) or Jupiter-like (higher)
2. **Add a new package name** - Edit the `names` list in `package.py`
3. **Change the star colors** - Make some stars red or blue in `level.py`

### Intermediate

4. **Add a "Heavy" package type** - Falls faster, harder to slow down
5. **Add a fuel pickup** - Floating item that restores fuel when touched
6. **Add wind** - Random horizontal force that changes over time

### Advanced

7. **Add particle effects** - Thrust exhaust particles that fade out
8. **Add sound effects** - Thrust sound, landing sound, crash sound
9. **Add a high score system** - Track best ratings across sessions
10. **Add multiple landing pads** - Deliver to several locations in one run

---

## Key Takeaways

1. **Games are loops** - Input → Update → Draw → Repeat
2. **State machines** organize complex behavior into manageable pieces
3. **Pure functions** make physics predictable and testable
4. **Procedural generation** creates variety from simple rules
5. **Separation of concerns** keeps code maintainable
6. **Constants files** make tuning easy

## Further Reading

- [Game Programming Patterns](https://gameprogrammingpatterns.com/) - Free online book
- [Pygame Documentation](https://pygame.org/docs/)
- [Red Blob Games](https://www.redblobgames.com/) - Visual explanations of game algorithms
- [Lunar Lander History](https://en.wikipedia.org/wiki/Lunar_Lander_(video_game_genre)) - The genre that inspired this game

---

*This document accompanies the Orbital Delivery game, created for CSC 134.*
