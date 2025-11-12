#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <random>
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
    cout << "║    The Work-Safe Dare-Ya Roulette     ║" << endl;
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
    superSoaker.clear(); // empty the vector
    
    // Load the super soaker with random cartridges
    int waterCount = 1 + rand() % 3;  // 1-3 water cartridges
    int slimeCount = 1 + rand() % 2;  // 1-2 slime cartridges
    
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
    
    // pop_back() would remove the last one
    // removing the first one takes 2 steps as follows
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