# Orbital Delivery

A Lunar Lander-style game where you deliver AI-powered packages from orbit to planetary surfaces. Packages rate their delivery experience 1-5 stars based on how they were handled!

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## Running the Game

```bash
cd orbital_delivery
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| W | Main thruster (upward force relative to ship) |
| A | Rotate counter-clockwise |
| D | Rotate clockwise |
| SPACE | Start game / Continue |
| ESC | Quit / Return to menu |

## Gameplay

1. **Orbit Phase**: See your package info and what it cares about
2. **Descent Phase**: Use thrust and rotation to land on the green pad
3. **Rating Phase**: Your package rates the delivery and leaves a review!

## Package Types

### Fragile
- Cares about: **Smooth handling**
- Tracks total acceleration (delta-v) during descent
- Use gentle, controlled thrust for best ratings

### Urgent
- Cares about: **Speed**
- Tracks delivery time
- Get down fast for best ratings (but don't crash!)

## File Structure

```
orbital_delivery/
├── main.py        # Entry point, game loop
├── constants.py   # Tuning values and configuration
├── physics.py     # Pure physics functions
├── ship.py        # Ship state and rendering
├── package.py     # Package rating and review system
├── level.py       # Landing zones and terrain
└── ui.py          # HUD, menus, screens
```

## Tips

- Watch your velocity indicator - green is safe, red means crash
- Fragile packages hate sudden movements - use short, gentle bursts
- Urgent packages want speed - try falling fast, then braking at the end
- Don't run out of fuel mid-descent!

## Educational Purpose

This game demonstrates:
- **Separation of Concerns**: Each module handles one thing
- **Pure Functions**: Physics calculations have no side effects
- **State Machine**: Game phases as explicit states
- **Data-Driven Design**: All tuning values in constants.py
