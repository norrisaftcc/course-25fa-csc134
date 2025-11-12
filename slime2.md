# Slime Roulette: Program Explanation Handout

## CSC 134 - Week 9 | Understanding the Code Structure

-----

## 🎯 What This Program Does

**Slime Roulette** is a turn-based game where you and an opponent take turns firing a super soaker loaded with water and slime cartridges. You can see how many of each type are loaded, but not which one fires next!

- 🔵 **Water** = Safe (get another turn if you fire at yourself)
- 🟢 **Slime** = Lose a point
- First player to reach 0 points loses

-----

## 📋 Program Structure Overview

```
┌─────────────────────────────────────────────────┐
│           GLOBAL VARIABLES                       │
│  (Shared data accessible to all functions)      │
│  - superSoaker (vector of cartridges)           │
│  - playerScore, opponentScore                   │
│  - currentPlayer, gameOver                      │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│              MAIN FUNCTION                       │
│  1. Setup game                                   │
│  2. Main game loop (player/opponent turns)      │
│  3. Check if game is over                       │
│  4. Reload if super soaker is empty             │
│  5. Display winner                              │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│           HELPER FUNCTIONS                       │
│  - Setup & Display functions                    │
│  - Turn logic functions                         │
│  - Game mechanics functions                     │
└─────────────────────────────────────────────────┘
```

-----

## 🔧 Global Variables Explained

These variables are declared **outside** any function, so **all functions** can access and modify them:

```cpp
vector<char> superSoaker;
```

**Purpose:** Stores the cartridges (‘W’ for water, ‘S’ for slime)  
**Why vector?** We need to easily add, remove, and shuffle cartridges  
**Who uses it:** `loadSuperSoaker()`, `fireShot()`, `displaySuperSoaker()`

```cpp
int playerScore = 3;
int opponentScore = 3;
```

**Purpose:** Track how many points each player has  
**Starting value:** 3 points each  
**Who modifies:** `playerTurn()`, `opponentTurn()` (decreases when hit by slime)

```cpp
string currentPlayer = "Player";
```

**Purpose:** Whose turn is it?  
**Possible values:** “Player” or “Opponent”  
**Who changes:** `playerTurn()`, `opponentTurn()` (switches based on results)

```cpp
bool gameOver = false;
```

**Purpose:** Should the game loop continue?  
**Who checks:** Main loop  
**Who changes:** `checkGameOver()` (sets to true when someone reaches 0 points)

-----

## 🎮 How the Game Flows

### Phase 1: Setup (happens once per round)

```cpp
setupGame()
├── superSoaker.clear()              // Empty any old cartridges
├── Generate random counts           // 2-4 water, 2-3 slime
├── loadSuperSoaker(water, slime)   // Add cartridges to vector
└── shuffleSuperSoaker()            // Randomize order
```

**Key Function: `loadSuperSoaker(int waterCount, int slimeCount)`**

```cpp
void loadSuperSoaker(int waterCount, int slimeCount) {
    // Add water cartridges
    for (int i = 0; i < waterCount; i++) {
        superSoaker.push_back('W');  // Vector grows automatically!
    }
    
    // Add slime cartridges  
    for (int i = 0; i < slimeCount; i++) {
        superSoaker.push_back('S');
    }
}
```

**What happens:** Fills the global `superSoaker` vector with the right mix of cartridges

-----

### Phase 2: Main Game Loop

```cpp
while (!gameOver) {
    if (currentPlayer == "Player") {
        playerTurn();        // Your turn
    } else {
        opponentTurn();      // AI's turn
    }
    
    checkGameOver();         // Did someone reach 0?
    
    if (superSoaker.empty() && !gameOver) {
        setupGame();         // Reload for next round
    }
}
```

**The loop continues until `gameOver` becomes `true`**

-----

### Phase 3: Taking a Turn

#### Player’s Turn Flow:

```
playerTurn()
├── Display current scores and cartridge counts
├── Ask: Fire at [1] yourself or [2] opponent?
├── fireShot() → removes cartridge from vector
├── Check result:
│   ├── Water?
│   │   ├── At self? → Keep your turn
│   │   └── At opponent? → Switch turns
│   └── Slime?
│       ├── At self? → Lose 1 point, switch turns
│       └── At opponent? → Opponent loses 1 point, switch turns
└── Update currentPlayer
```

**Key Function: `fireShot()`**

```cpp
char fireShot() {
    if (superSoaker.empty()) {
        return 'E';  // Empty
    }
    
    // Get first cartridge
    char cartridge = superSoaker.front();
    
    // Remove it from the vector (this is the "shot")
    superSoaker.erase(superSoaker.begin());
    
    return cartridge;  // Return 'W' or 'S'
}
```

**What this does:**

1. Checks if vector is empty (return ‘E’ for error)
1. Gets the **first** cartridge (the one about to fire)
1. **Removes** it from the vector (using `erase()`)
1. Returns what was fired (‘W’ or ‘S’)

**Why this matters:** This is the core mechanic! Each shot permanently removes a cartridge from the vector.

-----

### Phase 4: Checking Game Over

```cpp
void checkGameOver() {
    if (playerScore <= 0 || opponentScore <= 0) {
        gameOver = true;  // Modifies global variable
    }
}
```

**Simple but essential:** Checks if anyone has lost all their points. If so, sets the global `gameOver` flag to true, which stops the main loop.

-----

## 🔍 Understanding Vector Operations

### Key Operations Used in This Program:

**1. Adding to the end:**

```cpp
superSoaker.push_back('W');  // Adds water cartridge to end
```

**2. Removing from the front:**

```cpp
superSoaker.erase(superSoaker.begin());  // Removes first cartridge
```

**3. Getting the first element (without removing):**

```cpp
char next = superSoaker.front();  // Peek at first cartridge
```

**4. Checking size:**

```cpp
if (superSoaker.empty()) { ... }       // Is it empty?
int count = superSoaker.size();        // How many cartridges?
```

**5. Counting specific elements:**

```cpp
int waterCount = 0;
for (char cartridge : superSoaker) {   // Range-based for loop
    if (cartridge == 'W') waterCount++;
}
```

**6. Shuffling:**

```cpp
random_shuffle(superSoaker.begin(), superSoaker.end());
```

-----

## 🎨 Display Functions Explained

### `displayGameState()`

```cpp
void displayGameState() {
    cout << "┌─────────────────────────────────────┐" << endl;
    cout << "│  Player: " << playerScore << " points   Opponent: " 
         << opponentScore << " points  │" << endl;
    cout << "└─────────────────────────────────────┘" << endl;
}
```

**What it does:** Shows current scores in a nice box  
**Global variables it reads:** `playerScore`, `opponentScore`  
**Does it modify anything?** No - just displays

-----

### `displaySuperSoaker(bool showContents)`

```cpp
void displaySuperSoaker(bool showContents) {
    // Count water and slime
    int waterCount = 0;
    int slimeCount = 0;
    for (char cartridge : superSoaker) {
        if (cartridge == 'W') waterCount++;
        else slimeCount++;
    }
    
    // Display counts
    cout << "🔵 " << waterCount << " water, ";
    cout << "🟢 " << slimeCount << " slime" << endl;
    
    // Optional: show actual order (for debugging)
    if (showContents) {
        for (char cartridge : superSoaker) {
            cout << (cartridge == 'W' ? "🔵" : "🟢") << " ";
        }
    }
}
```

**What it does:** Shows how many of each cartridge type remain  
**Parameter:** `showContents` - if true, reveals the actual order (cheating!)  
**Global variables it reads:** `superSoaker`

-----

## 🤖 AI Opponent Logic

```cpp
void opponentTurn() {
    // Simple AI: random choice
    int choice = 1 + rand() % 2;  // 50/50 chance
    
    if (choice == 1) {
        cout << "Opponent fires at themselves!" << endl;
    } else {
        cout << "Opponent fires at you!" << endl;
    }
    
    char result = fireShot();  // Fire and see what happens
    
    // Same logic as player turn for handling results
    // ...
}
```

**AI Strategy:** Completely random (50% self, 50% opponent)  
**Could be improved:** Smart AI would calculate odds based on remaining cartridges

-----

## 🔄 Turn Switching Logic

**The Rules:**

- Fire **water** at **self** → **Keep your turn** (you’re safe!)
- Fire **water** at **opponent** → **Switch turns** (they’re safe)
- Fire **slime** at **anyone** → **Switch turns** (someone got hit)

**In code:**

```cpp
if (result == 'W') {  // Water
    if (choice == 1) {
        // Fired at self - keep turn
        // currentPlayer stays the same
    } else {
        // Fired at opponent - switch
        currentPlayer = "Opponent";
    }
} else {  // Slime
    // Always switch after slime
    currentPlayer = "Opponent";
    
    // Also decrease appropriate score
    if (choice == 1) {
        playerScore--;
    } else {
        opponentScore--;
    }
}
```

-----

## 📊 Data Flow Diagram

```
┌──────────────┐
│  setupGame() │ → Creates cartridges → superSoaker vector
└──────────────┘

┌──────────────┐
│ playerTurn() │ → Reads: playerScore, opponentScore, superSoaker
└──────────────┘   Modifies: playerScore or opponentScore, currentPlayer
                   Calls: fireShot()

┌──────────────┐
│  fireShot()  │ → Reads: superSoaker
└──────────────┘   Modifies: superSoaker (removes one cartridge)
                   Returns: 'W' or 'S'

┌──────────────────┐
│ checkGameOver() │ → Reads: playerScore, opponentScore
└──────────────────┘   Modifies: gameOver
```

-----

## 💡 Why Global Variables Work Here

**Reasons this design makes sense:**

1. **Shared Game State:** Multiple functions need access to scores, cartridges, etc.
1. **Learning Tool:** Easy to see how data flows between functions
1. **Small Program:** Under 300 lines - manageable size for globals
1. **Natural Model:** Mirrors how game state actually works in engines

**Functions that READ global variables:**

- `displayGameState()` - reads scores
- `displaySuperSoaker()` - reads cartridges
- `checkGameOver()` - reads scores

**Functions that MODIFY global variables:**

- `loadSuperSoaker()` - adds to cartridges
- `fireShot()` - removes from cartridges
- `playerTurn()` / `opponentTurn()` - modify scores and currentPlayer
- `checkGameOver()` - sets gameOver flag

-----

## 🎯 Key Concepts Demonstrated

### 1. Vector as Dynamic Array

The super soaker cartridges grow and shrink as needed - no fixed size!

### 2. Game Loop Pattern

```cpp
while (!gameOver) {
    // Take turn
    // Check conditions
    // Update state
}
```

This is how most games work!

### 3. Function Decomposition

Instead of one giant `main()` function, we break it into logical pieces:

- Setup functions
- Display functions
- Turn logic functions
- Utility functions

### 4. State Management

Global variables represent the “state” of the game at any moment.

-----

## 🐛 Common Questions

**Q: Why does `fireShot()` use `erase(begin())` instead of `pop_back()`?**  
A: We remove from the **front** because that’s the “next shot.” If we used `pop_back()`, we’d remove from the end, which doesn’t make sense for a gun barrel!

**Q: What if I want to peek at the next shot without removing it?**  
A: Use `superSoaker.front()` to see it, but don’t call `erase()`. This would be “cheating” though!

**Q: Why shuffle after loading?**  
A: So players can’t predict the order. Random order makes the game suspenseful!

**Q: Can I have more than 2 players?**  
A: Sure! You’d need to store player data differently (maybe a vector of Player structs), but the concept is the same.

**Q: Why use `random_shuffle` instead of `shuffle`?**  
A: `random_shuffle` is simpler for beginners. Modern C++ prefers `shuffle` with a random engine, but `random_shuffle` works fine for learning.

-----

## 📝 Quick Reference: What Each Function Does

|Function              |Purpose                  |Reads                         |Modifies               |
|----------------------|-------------------------|------------------------------|-----------------------|
|`setupGame()`         |Initialize round         |-                             |`superSoaker`          |
|`loadSuperSoaker()`   |Add cartridges           |-                             |`superSoaker`          |
|`shuffleSuperSoaker()`|Randomize order          |`superSoaker`                 |`superSoaker`          |
|`displayGameState()`  |Show scores              |`playerScore`, `opponentScore`|-                      |
|`displaySuperSoaker()`|Show cartridges          |`superSoaker`                 |-                      |
|`fireShot()`          |Remove & return cartridge|`superSoaker`                 |`superSoaker`          |
|`playerTurn()`        |Handle player’s turn     |All game state                |Scores, `currentPlayer`|
|`opponentTurn()`      |Handle AI’s turn         |All game state                |Scores, `currentPlayer`|
|`checkGameOver()`     |Check win condition      |Scores                        |`gameOver`             |

-----

## 🚀 Understanding This Program Prepares You For:

- ✅ **Object-Oriented Programming** (next: put these globals in a Game class!)
- ✅ **Pass-by-reference** (alternative to globals)
- ✅ **STL containers** (you’re already using vector!)
- ✅ **Game development patterns** (state, loops, turn logic)
- ✅ **Data structure manipulation** (adding, removing, searching)

-----

## 🎓 Summary

**The Big Picture:**

1. Global variables store the game state
1. Functions read and modify that state
1. The main loop orchestrates turns
1. Vectors make cartridge management easy
1. Everything works together to create a complete game!

**Key Insight:**  
This program shows how multiple functions can work together by sharing data through global variables. Later, you’ll learn about classes and objects, which provide a better way to organize shared data - but the concepts are the same!

-----

**Happy Coding! May your shots be water and your opponent’s be slime! 💦😄**