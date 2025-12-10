# Orbital Delivery

A Lunar Lander-style game where you deliver AI-powered packages from orbit to planetary surfaces. Each package has a personality and will rate their delivery experience 1-5 stars based on how they were handled!

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-Educational-orange.svg)

## Table of Contents

- [About](#about)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [How to Play](#how-to-play)
- [Package Types](#package-types)
- [Difficulty Progression](#difficulty-progression)
- [Building a Standalone Executable](#building-a-standalone-executable)
- [Project Structure](#project-structure)
- [Educational Purpose](#educational-purpose)

---

## About

Orbital Delivery is a teaching example created for CSC 134, demonstrating how to structure a Python game with clean, modular architecture. The game combines classic arcade physics with a modern twist: your cargo is sentient AI that will judge your piloting skills!

**Key Features:**
- Classic thrust-and-rotate spacecraft controls
- Two package types with different rating criteria
- Procedurally generated terrain that increases in difficulty
- Humorous AI-generated reviews based on your performance
- Progressive difficulty with lateral offset challenges

---

## Tech Stack

### Python 3.8+
The core programming language. Python was chosen for readability and accessibility to students learning programming concepts.

### Pygame
A popular library for making games in Python. Pygame handles:
- **Window creation** - Opening a game window
- **Drawing** - Shapes, text, and eventually sprites
- **Input** - Keyboard and mouse events
- **Game loop timing** - Maintaining consistent frame rates

Pygame is a wrapper around SDL (Simple DirectMedia Layer), a cross-platform multimedia library used by many commercial games.

### Why This Stack?
1. **Beginner-friendly** - No complex build systems or compilers
2. **Cross-platform** - Runs on Windows, Mac, and Linux
3. **Visual results fast** - See your code running immediately
4. **Industry-relevant concepts** - Game loops, state machines, and physics apply to any game engine

---

## Installation

### Prerequisites
- Python 3.8 or higher ([Download Python](https://python.org/downloads))
- pip (comes with Python)

### Step 1: Clone or Download
```bash
# If using git:
git clone https://github.com/norrisaftcc/course-25fa-csc134.git
cd course-25fa-csc134/m8/delivery_game/orbital_delivery

# Or download and extract the ZIP file, then navigate to the folder
```

### Step 2: Install Pygame
```bash
pip install pygame
```

Or if you have multiple Python versions:
```bash
python3 -m pip install pygame
```

### Step 3: Verify Installation
```bash
python -c "import pygame; print(f'Pygame {pygame.version.ver} installed successfully!')"
```

---

## Running the Game

```bash
# Navigate to the game directory
cd orbital_delivery

# Run the game
python main.py
```

On some systems you may need:
```bash
python3 main.py
```

---

## How to Play

### Controls

| Key | Action |
|-----|--------|
| **W** | Main thruster (fires in direction ship is pointing) |
| **A** | Rotate counter-clockwise |
| **D** | Rotate clockwise |
| **SPACE** | Start game / Continue to next delivery |
| **ESC** | Quit / Return to menu |

### Game Flow

1. **Orbit Phase** - Read your package info and see what they care about
2. **Descent Phase** - Navigate through terrain and land on the green pad
3. **Rating Phase** - Receive your star rating and read the package's review
4. **Repeat** - Each successful delivery increases difficulty!

### Tips for Success

- **Watch the velocity indicator** - Green means safe landing speed, yellow is caution, red means crash
- **Manage your fuel** - The gauge shows remaining thrust capacity
- **Plan your descent** - At higher levels, you start offset from the pad
- **Use terrain wisely** - Hills can block your path but also provide reference points

---

## Package Types

### Fragile Packages
- **What they care about:** Smooth handling
- **How they rate:** Based on total acceleration (delta-v) experienced
- **Strategy:** Use gentle, controlled bursts of thrust
- **Examples:** Delicate Vase, Antique Clock, Grandma's Ashes

### Urgent Packages
- **What they care about:** Speed of delivery
- **How they rate:** Based on time from descent start to landing
- **Strategy:** Fall fast, brake hard at the end (but don't crash!)
- **Examples:** Vital Organs, Pizza (HOT), Unstable Isotope

---

## Difficulty Progression

Each successful delivery increases the challenge:

| Level | Pad Width | Ship Offset | Terrain |
|-------|-----------|-------------|---------|
| 1 | 100px | None (above pad) | Nearly flat |
| 3 | 90px | 120px lateral | Gentle hills |
| 5 | 80px | 240px lateral | Moderate terrain |
| 8+ | 60px | 300px (max) | Challenging hills |

---

## Building a Standalone Executable

Want to share your game without requiring players to install Python? Use **PyInstaller** to create a standalone `.exe` (Windows) or app bundle (Mac).

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Create the Executable

Navigate to the `orbital_delivery` folder and run:

```bash
# Single executable file (slower to start, but one file)
pyinstaller --onefile --windowed main.py --name OrbitalDelivery

# Or a folder with all dependencies (faster startup)
pyinstaller --onedir --windowed main.py --name OrbitalDelivery
```

**Flags explained:**
- `--onefile` - Bundle everything into a single .exe
- `--onedir` - Create a folder with the .exe and dependencies
- `--windowed` - Don't show a console window (for GUI apps)
- `--name` - Name of the output executable

### Step 3: Find Your Build

After PyInstaller finishes, find your executable in:
```
orbital_delivery/
├── dist/
│   └── OrbitalDelivery.exe    # Your distributable!
├── build/                      # Temporary build files (can delete)
└── OrbitalDelivery.spec        # Build configuration
```

### Step 4: Distribute

The `dist/` folder contains everything needed to run the game. You can:
- Zip it and share directly
- Upload to [itch.io](https://itch.io) as a downloadable game
- Share on game jams

### Troubleshooting PyInstaller

**"Module not found" errors:**
```bash
pyinstaller --onefile --windowed --hidden-import pygame main.py
```

**Missing assets (if you add images/sounds later):**
```bash
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
```

**For Mac users:** Replace `--windowed` with `--windowed --osx-bundle-identifier com.yourname.orbitaldelivery`

---

## Project Structure

```
orbital_delivery/
├── main.py              # Entry point, game loop, state machine
├── constants.py         # All tuning values in one place
├── physics.py           # Pure functions for gravity, thrust, collision
├── ship.py              # Ship state, rendering, fuel management
├── package.py           # Package types, rating logic, review generation
├── level.py             # Landing pad, terrain generation, difficulty
├── ui.py                # HUD, menus, rating screens
├── README.md            # This file
└── Behind_The_Scenes.md # Technical deep-dive for students
```

### Module Responsibilities

| Module | Single Responsibility |
|--------|----------------------|
| `main.py` | Game loop and state transitions |
| `constants.py` | Configuration values (no logic) |
| `physics.py` | Math calculations (no rendering) |
| `ship.py` | Ship behavior and appearance |
| `package.py` | Rating algorithms and reviews |
| `level.py` | World generation |
| `ui.py` | Everything the player reads |

---

## Educational Purpose

This project demonstrates several programming concepts:

### Design Patterns
- **State Machine** - Game phases (orbit → descent → rating) as explicit states
- **Single Responsibility** - Each module does one thing well
- **Data-Driven Design** - Tuning values separate from logic

### Programming Concepts
- **Pure Functions** - Physics calculations take input, return output, no side effects
- **Encapsulation** - Ship class manages its own state
- **Separation of Concerns** - Rendering separate from logic

### Game Development Concepts
- **Game Loop** - Update → Draw → Repeat at 60 FPS
- **Delta Time** - Frame-rate independent physics (conceptually)
- **Collision Detection** - Point-vs-terrain and point-vs-rectangle

---

## Credits

- **Concept:** Classic Lunar Lander (Atari, 1979)
- **Created for:** CSC 134, Fall 2025
- **Tech:** Python + Pygame

---

## See Also

- [Behind_The_Scenes.md](Behind_The_Scenes.md) - Technical deep-dive for CS students
- [Pygame Documentation](https://pygame.org/docs/)
- [PyInstaller Manual](https://pyinstaller.org/en/stable/)
