# CSC 134 - Week 9: Slime Roulette

## Understanding Parameter Passing: Global Variables, Pass-by-Value, and Pass-by-Reference

-----

## 🎯 The Game: Slime Roulette

Welcome to **Slime Roulette** - a work-safe interpretation of the popular game mechanic!

**Game Setup:**

- A super soaker is loaded with X cartridges
- 🔵 **Blue cartridges** contain harmless water (safe!)
- 🟢 **Green cartridges** contain embarrassing slime (lose a point!)
- You can see how many of each type are in the gun, but **not which one fires next**
- Each turn: Choose to fire at **yourself** or your **opponent**
- If you fire water at yourself, you get another turn!
- First to 0 points loses

**Programming Focus:**
This assignment demonstrates **three ways to pass data to functions**:

1. **Global variables** (what we’re using)
1. **Pass-by-value** (makes a copy)
1. **Pass-by-reference** (modifies the original)

-----

## 💻 Complete Game Code (Global Variable Approach)

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <random_device>
#include <ctime>
using namespace std;

// ============================================================================
// GLOBAL VARIABLES - Accessible to all functions
// ============================================================================
// The super soaker's cartridges ('W' = Water, 'S' = Slime)
vector<char> superSoaker;

// Player scores
int playerScore = 3;
int opponentScore = 3;

// Game state
string currentPlayer = "Player";
bool gameOver = false;

// ============================================================================
// FUNCTION PROTOTYPES
// ============================================================================
void setupGame();
void loadSuperSoaker(int waterCount, int slimeCount);
void shuffleSuperSoaker();
void displayGameState();
void displaySuperSoaker(bool showContents);
char fireShot();
void playerTurn();
void opponentTurn();
void checkGameOver();

// ============================================================================
// MAIN GAME LOOP
// ============================================================================
int main() {
    srand(time(0));  // Seed random number generator
    
    cout << "╔════════════════════════════════════════╗" << endl;
    cout << "║     SLIME ROULETTE: SUPER SOAKER      ║" << endl;
    cout << "║    The Work-Safe Russian Roulette     ║" << endl;
    cout << "╚════════════════════════════════════════╝" << endl;
    cout << "\nRules:" << endl;
    cout << "🔵 Blue cartridges = Harmless water (you get another turn!)" << endl;
    cout << "🟢 Green cartridges = Slime (lose a point!)" << endl;
    cout << "First to 0 points loses!\n" << endl;
    
    setupGame();
    
    // Main game loop
    while (!gameOver) {
        if (currentPlayer == "Player") {
            playerTurn();
        } else {
            opponentTurn();
        }
        
        checkGameOver();
        
        // If super soaker is empty, reload for next round
        if (superSoaker.empty() && !gameOver) {
            cout << "\n💦 Super soaker is empty! Reloading for next round..." << endl;
            cout << "Press Enter to continue...";
            cin.ignore();
            cin.get();
            setupGame();
        }
    }
    
    // Game over
    cout << "\n╔════════════════════════════════════════╗" << endl;
    cout << "║            GAME OVER!                  ║" << endl;
    cout << "╚════════════════════════════════════════╝" << endl;
    
    if (playerScore <= 0) {
        cout << "💚 You got slimed! Opponent wins!" << endl;
    } else {
        cout << "🎉 You win! Opponent got slimed!" << endl;
    }
    
    return 0;
}

// ============================================================================
// GAME SETUP FUNCTIONS
// ============================================================================

void setupGame() {
    // Clear any existing cartridges
    superSoaker.clear();
    
    // Load the super soaker with random cartridges
    int waterCount = 2 + rand() % 3;  // 2-4 water cartridges
    int slimeCount = 2 + rand() % 2;  // 2-3 slime cartridges
    
    loadSuperSoaker(waterCount, slimeCount);
    shuffleSuperSoaker();
    
    cout << "\n🔫 Super soaker loaded!" << endl;
    displaySuperSoaker(false);  // Show counts but not order
}

void loadSuperSoaker(int waterCount, int slimeCount) {
    // Add water cartridges
    for (int i = 0; i < waterCount; i++) {
        superSoaker.push_back('W');
    }
    
    // Add slime cartridges
    for (int i = 0; i < slimeCount; i++) {
        superSoaker.push_back('S');
    }
}

void shuffleSuperSoaker() {
    // Shuffle the cartridges so players don't know the order
    random_shuffle(superSoaker.begin(), superSoaker.end());
}

// ============================================================================
// DISPLAY FUNCTIONS
// ============================================================================

void displayGameState() {
    cout << "\n┌─────────────────────────────────────┐" << endl;
    cout << "│  Player: " << playerScore << " points   Opponent: " << opponentScore << " points  │" << endl;
    cout << "└─────────────────────────────────────┘" << endl;
}

void displaySuperSoaker(bool showContents) {
    int waterCount = 0;
    int slimeCount = 0;
    
    // Count each type using a range-based for loop
    for (char cartridge : superSoaker) {
        if (cartridge == 'W') waterCount++;
        else slimeCount++;
    }
    
    cout << "Super Soaker contents: ";
    cout << "🔵 " << waterCount << " water, ";
    cout << "🟢 " << slimeCount << " slime";
    cout << " (" << superSoaker.size() << " total)" << endl;
    
    // For debugging/demonstration - show actual order
    if (showContents) {
        cout << "Actual order: ";
        for (char cartridge : superSoaker) {
            cout << (cartridge == 'W' ? "🔵" : "🟢") << " ";
        }
        cout << endl;
    }
}

// ============================================================================
// CORE GAME MECHANICS
// ============================================================================

char fireShot() {
    // Fire the next cartridge (remove from front of vector)
    // This is why we use a vector - easy to remove from front!
    
    if (superSoaker.empty()) {
        return 'E';  // Empty!
    }
    
    // Get the first cartridge
    char cartridge = superSoaker.front();
    
    // Remove it from the super soaker
    superSoaker.erase(superSoaker.begin());
    
    return cartridge;
}

// ============================================================================
// TURN LOGIC
// ============================================================================

void playerTurn() {
    displayGameState();
    displaySuperSoaker(false);
    
    cout << "\n>>> YOUR TURN <<<" << endl;
    cout << "Fire at: [1] Yourself  [2] Opponent" << endl;
    cout << "Choice: ";
    
    int choice;
    cin >> choice;
    
    // Input validation
    while (choice != 1 && choice != 2) {
        cout << "Invalid choice. Enter 1 or 2: ";
        cin >> choice;
    }
    
    cout << "\n💦 *SPLASH!* ";
    char result = fireShot();
    
    if (result == 'W') {
        cout << "🔵 Water! " << endl;
        if (choice == 1) {
            cout << "You're wet but safe! You get another turn!" << endl;
            // Player keeps their turn (currentPlayer stays "Player")
        } else {
            cout << "Opponent is soaked but unharmed." << endl;
            currentPlayer = "Opponent";  // Switch turns
        }
    } else if (result == 'S') {
        cout << "🟢 SLIME!" << endl;
        if (choice == 1) {
            cout << "You got slimed! -1 point!" << endl;
            playerScore--;
        } else {
            cout << "Opponent got slimed! -1 point!" << endl;
            opponentScore--;
        }
        currentPlayer = "Opponent";  // Switch turns after slime
    }
}

void opponentTurn() {
    displayGameState();
    displaySuperSoaker(false);
    
    cout << "\n>>> OPPONENT'S TURN <<<" << endl;
    cout << "Press Enter to see opponent's choice...";
    cin.ignore();
    cin.get();
    
    // Simple AI: 50/50 chance to fire at self or player
    int choice = 1 + rand() % 2;
    
    if (choice == 1) {
        cout << "Opponent fires at themselves!" << endl;
    } else {
        cout << "Opponent fires at you!" << endl;
    }
    
    cout << "\n💦 *SPLASH!* ";
    char result = fireShot();
    
    if (result == 'W') {
        cout << "🔵 Water!" << endl;
        if (choice == 1) {
            cout << "Opponent is wet but gets another turn!" << endl;
            // Opponent keeps their turn
        } else {
            cout << "You're soaked but unharmed." << endl;
            currentPlayer = "Player";  // Switch turns
        }
    } else if (result == 'S') {
        cout << "🟢 SLIME!" << endl;
        if (choice == 1) {
            cout << "Opponent got slimed! -1 point!" << endl;
            opponentScore--;
        } else {
            cout << "You got slimed! -1 point!" << endl;
            playerScore--;
        }
        currentPlayer = "Player";  // Switch turns after slime
    }
}

void checkGameOver() {
    if (playerScore <= 0 || opponentScore <= 0) {
        gameOver = true;
    }
}
```

-----

## 🎓 What Makes This Work: Global Variables

In this program, we use **global variables** for game state:

```cpp
vector<char> superSoaker;    // The cartridges
int playerScore = 3;         // Player's points
int opponentScore = 3;       // Opponent's points
string currentPlayer = "Player";
bool gameOver = false;
```

**Why global variables work here:**

- ✅ Multiple functions need to read/modify the same data
- ✅ Represents persistent “game state” throughout the program
- ✅ Simple to understand for beginners
- ✅ Mirrors how many game engines actually work (global game state)

**The functions just access these directly:**

```cpp
void fireShot() {
    superSoaker.erase(superSoaker.begin());  // Modifies global vector
}

void checkGameOver() {
    if (playerScore <= 0) {  // Reads global variables
        gameOver = true;      // Modifies global variable
    }
}
```

-----

## 📚 AFTERWORD: Alternative Approaches

### Understanding the Three Parameter Passing Methods

The game above uses **global variables** - but there are two other ways to pass data to functions. Let’s explore all three approaches with examples from our game.

-----

## METHOD 1: Global Variables (What We Used)

**Concept:** Data is declared outside all functions and is accessible everywhere.

```cpp
// Global variable
vector<char> superSoaker;

void fireShot() {
    // Directly accesses and modifies the global vector
    superSoaker.erase(superSoaker.begin());
}

int main() {
    superSoaker.push_back('W');
    fireShot();  // No parameters needed!
    cout << superSoaker.size();  // Modified by fireShot()
}
```

**Pros:**

- ✅ Simple to understand
- ✅ No need to pass data around
- ✅ Great for persistent game state
- ✅ Natural for systems that share data (like our game)

**Cons:**

- ❌ Any function can change the data (hard to track bugs)
- ❌ Functions are less reusable (tied to specific global names)
- ❌ Not considered “best practice” in large programs

**When to use:**

- Learning about functions
- Small programs with shared state
- Game state that many systems need to access

-----

## METHOD 2: Pass-by-Value (Makes a Copy)

**Concept:** The function receives a **copy** of the data. Changes inside the function **don’t affect** the original.

### Example: Checking if player can win

```cpp
// Pass-by-value: receives COPIES of the scores
bool canPlayerWin(int pScore, int oScore, vector<char> cartridges) {
    // These are copies - modifying them won't change the originals
    int slimeCount = 0;
    for (char c : cartridges) {
        if (c == 'S') slimeCount++;
    }
    
    // Can player win if opponent gets hit by all remaining slime?
    return (oScore - slimeCount) <= 0;
}

int main() {
    int playerScore = 2;
    int opponentScore = 2;
    vector<char> superSoaker = {'S', 'S', 'W'};
    
    bool canWin = canPlayerWin(playerScore, opponentScore, superSoaker);
    
    // playerScore, opponentScore, and superSoaker are UNCHANGED
    cout << superSoaker.size();  // Still 3!
}
```

**Pros:**

- ✅ Safe - original data can’t be accidentally modified
- ✅ Function is “pure” - doesn’t have side effects
- ✅ Easy to reason about - what goes in is separate from what comes out
- ✅ Great for calculations and queries

**Cons:**

- ❌ Creates copies (slow for large vectors!)
- ❌ Can’t modify the original data (even if you want to)
- ❌ Uses more memory

**When to use:**

- Querying data without modifying it
- Mathematical calculations
- When you need to protect original data
- For small data types (int, char, bool)

-----

## METHOD 3: Pass-by-Reference (Modifies the Original)

**Concept:** The function receives a **reference** to the original data. Changes inside the function **DO affect** the original.

### Example: Firing a shot with pass-by-reference

```cpp
// Pass-by-reference: receives references (note the &)
char fireShot(vector<char>& cartridges, int& currentScore, bool firingAtSelf) {
    //                              ^                 ^
    //                         These & symbols mean "reference"
    
    if (cartridges.empty()) {
        return 'E';
    }
    
    // Get and remove the first cartridge
    char result = cartridges.front();
    cartridges.erase(cartridges.begin());  // Modifies the ORIGINAL vector!
    
    // If it's slime and firing at self, update score
    if (result == 'S' && firingAtSelf) {
        currentScore--;  // Modifies the ORIGINAL score!
    }
    
    return result;
}

int main() {
    vector<char> superSoaker = {'S', 'W', 'S'};
    int playerScore = 3;
    
    char result = fireShot(superSoaker, playerScore, true);
    
    // superSoaker and playerScore ARE CHANGED!
    cout << superSoaker.size();  // Now 2! (one removed)
    cout << playerScore;         // Now 2! (decreased by fireShot)
}
```

**Pros:**

- ✅ Can modify the original data
- ✅ No copying (efficient for large vectors)
- ✅ Function can “return” multiple values by modifying references
- ✅ This is what you usually want for game state modifications

**Cons:**

- ❌ Function can change data unexpectedly
- ❌ Harder to reason about - function has “side effects”
- ❌ Need to be careful about what you pass

**When to use:**

- Need to modify the original data
- Working with large data structures (vectors, arrays)
- Functions that update multiple pieces of state
- Most real-world game programming

-----

## 🔄 Converting Slime Roulette to Pass-by-Reference

Here’s how the key function would look with pass-by-reference instead of globals:

```cpp
// ============================================================================
// PASS-BY-REFERENCE VERSION
// ============================================================================

// All the game state is now passed as references
void playerTurn(vector<char>& cartridges, int& pScore, int& oScore, string& currentPlayer) {
    cout << "\n>>> YOUR TURN <<<" << endl;
    cout << "Fire at: [1] Yourself  [2] Opponent" << endl;
    
    int choice;
    cin >> choice;
    
    // Fire the shot and modify the vectors/scores
    char result = cartridges.front();
    cartridges.erase(cartridges.begin());  // Modifies original cartridges
    
    if (result == 'W') {
        cout << "🔵 Water!" << endl;
        if (choice == 2) {
            currentPlayer = "Opponent";  // Modifies original currentPlayer
        }
    } else {
        cout << "🟢 SLIME!" << endl;
        if (choice == 1) {
            pScore--;  // Modifies original pScore
        } else {
            oScore--;  // Modifies original oScore
        }
        currentPlayer = "Opponent";
    }
}

int main() {
    vector<char> superSoaker = {'W', 'S', 'W', 'S'};
    int playerScore = 3;
    int opponentScore = 3;
    string currentPlayer = "Player";
    
    // Pass everything by reference
    playerTurn(superSoaker, playerScore, opponentScore, currentPlayer);
    
    // All the original variables have been modified!
    cout << "Super soaker now has: " << superSoaker.size() << " cartridges" << endl;
    cout << "Player score: " << playerScore << endl;
}
```

**Key differences from global approach:**

- Must pass all needed data as parameters
- Use `&` to indicate pass-by-reference
- More verbose but more explicit about dependencies
- Better for testing (can call function with different test data)

-----

## 📊 Comparison Chart: When to Use Each Method

|Scenario                           |Global     |Pass-by-Value|Pass-by-Reference|
|-----------------------------------|-----------|-------------|-----------------|
|**Shared game state**              |✅ Great    |❌ Awkward    |✅ Great          |
|**Small programs (<200 lines)**    |✅ Fine     |✅ Good       |✅ Good           |
|**Pure calculations**              |❌ Overkill |✅ Perfect    |❌ Overkill       |
|**Modifying data structures**      |✅ Works    |❌ Can’t do it|✅ Perfect        |
|**Large vectors/arrays**           |✅ Good     |❌ Slow copies|✅ Efficient      |
|**Testing functions independently**|❌ Hard     |✅ Easy       |✅ Easy           |
|**Understanding data flow**        |❌ Hidden   |✅ Clear      |⚠️ Medium         |
|**Preventing accidental changes**  |❌ No safety|✅ Very safe  |❌ Can change     |

-----

## 🎯 Real-World Usage Patterns

### Professional C++ Games:

```cpp
// Typically use a mix of all three:

// Global for truly shared systems
AudioEngine globalAudio;  // Everyone needs audio

// Pass-by-const-reference for reading (can't modify)
void displayHealth(const Player& player) {
    cout << player.getHealth();  // Can read but not change
}

// Pass-by-reference for modifying
void takeDamage(Player& player, int amount) {
    player.reduceHealth(amount);  // Can modify
}

// Pass-by-value for small data and calculations
int calculateDamage(int baseDamage, float multiplier) {
    return static_cast<int>(baseDamage * multiplier);
}
```

### Modern Best Practice:

1. **Avoid global variables** when possible (use classes/objects instead)
1. **Pass-by-const-reference** for reading large objects (`const vector<T>&`)
1. **Pass-by-reference** for modifying objects (`vector<T>&`)
1. **Pass-by-value** for small types (int, char, bool, small structs)

-----

## 💡 Discussion Questions

1. **Why does pass-by-value create a copy?** What happens to that copy after the function ends?
1. **What’s the `&` symbol doing?** How does it make pass-by-reference work?
1. **Memory consideration:** If `superSoaker` has 1000 cartridges, what happens when you:
- Use a global variable?
- Pass by value?
- Pass by reference?
1. **Safety vs. Convenience:** Global variables are convenient but can cause bugs. Can you think of a bug that might occur in our game because everything is global?
1. **Const-correctness:** There’s actually a fourth option: **pass-by-const-reference** (`const vector<char>&`). When would you use this? (Hint: when you want efficiency but also safety)

-----

## 🚀 Practice Challenges

### Challenge 1: Convert to Pass-by-Reference

Take ONE function from the global variable version (like `displayGameState()` or `checkGameOver()`) and rewrite it to use pass-by-reference instead.

```cpp
// Your version:
void displayGameState(/* what parameters go here? */) {
    // Implementation
}
```

### Challenge 2: Add a “Peek” Function

Write a function that uses **pass-by-value** to check if the next shot will be slime, WITHOUT removing it from the super soaker:

```cpp
bool isNextShotSlime(vector<char> cartridges) {
    // Implement this - remember, it's pass-by-value so you can't 
    // modify the original!
}
```

### Challenge 3: Make It Reusable

Create a **standalone** version of `fireShot()` that takes parameters instead of using globals:

```cpp
// Returns the cartridge type ('W', 'S', or 'E' for empty)
// Modifies the cartridges vector by reference
char fireShot(vector<char>& cartridges) {
    // Implement this
}
```

### Challenge 4: Const-Reference Challenge

Write a function that displays the super soaker state but guarantees it won’t modify it:

```cpp
void displaySuperSoaker(const vector<char>& cartridges) {
    // The 'const' means you CAN'T modify cartridges
    // Try to erase something - it won't compile!
}
```

-----

## ⚠️ Common Mistakes

### Mistake 1: Forgetting the `&`

```cpp
// Wrong - this is pass-by-value (makes a copy)
void removeFirst(vector<char> vec) {
    vec.erase(vec.begin());
}

// Right - this is pass-by-reference (modifies original)
void removeFirst(vector<char>& vec) {
    vec.erase(vec.begin());
}
```

### Mistake 2: Thinking Pass-by-Value Modifies the Original

```cpp
void changeName(string name) {
    name = "Bob";  // Only changes the COPY, not the original
}

int main() {
    string myName = "Alice";
    changeName(myName);
    cout << myName;  // Still "Alice"!
}
```

### Mistake 3: Not Realizing Global Variables Are Dangerous

```cpp
vector<int> scores;  // Global

void resetScores() {
    scores.clear();  // Oops! Just cleared everyone's scores
}

void displayScores() {
    // Assumes scores has data... but resetScores() might have cleared it!
}
```

-----

## 🎓 Key Takeaways

### About Global Variables:

- ✅ Perfect for learning and small programs
- ✅ Natural for game state
- ⚠️ Use sparingly in larger programs
- ⚠️ Make it clear what functions modify them (comments!)

### About Pass-by-Value:

- ✅ Safe and predictable
- ✅ Great for small data and calculations
- ❌ Slow for large data structures
- 💡 “Can I break anything by changing this?” → No!

### About Pass-by-Reference:

- ✅ Efficient for large data
- ✅ Necessary when you need to modify data
- ⚠️ Be careful - function can change your data!
- 💡 “Can I break anything by changing this?” → Yes!

-----

## 📝 Submission Requirements

For this assignment, submit:

1. **Working Slime Roulette game** (using global variables)
1. **One challenge completed** (your choice)
1. **Short reflection** (3-5 sentences) answering:
- When would you use pass-by-value vs pass-by-reference?
- What’s one advantage and one disadvantage of global variables?
1. **Code comments** explaining your design choices

-----

## 🎮 Have Fun!

This game is meant to be fun AND educational. Play a few rounds, then think about how the data flows through the program. Understanding parameter passing is one of the most important concepts in programming!

**Remember:** There’s no single “correct” approach. Different situations call for different tools. The key is understanding the trade-offs and choosing wisely.

Now go forth and may the odds be ever in your favor… just watch out for that slime! 💦🟢

-----

*“In programming, as in water gun battles, it’s not about avoiding mess entirely - it’s about knowing where the mess comes from and cleaning it up systematically.”* 😄