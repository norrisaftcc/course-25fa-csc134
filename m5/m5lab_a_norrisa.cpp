/*
================================================================================
STAGE 1: CHARACTER SELECTION ONLY
Exercise 3 Concept: Arrays + Loop + Search
================================================================================

WHAT THIS DEMONSTRATES:
- Array declaration and initialization
- Parallel arrays (keeping related data together)
- Looping through arrays to display
- Array index vs human numbering (0-2 vs 1-3)
- Input validation

BUILD THIS FIRST, TEST IT, THEN MOVE TO STAGE 2
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================================
// CHARACTER DATA (Parallel Arrays)
// ============================================================================
// TEACHING POINT: Arrays let us store related data together
// Common pattern: use a const for SIZE, then set up the arrays all SIZE in size.
// That way, you don't have to resize or keep track if you add things.
// it's const, declared out side of functions, so anyone can see it.
const int NUM_CLASSES = 3;

string classNames[NUM_CLASSES] = {"Warrior", "Mage", "Rogue"};
string classEmojis[NUM_CLASSES] = {"⚔️", "🔮", "🗡️"};
int classMaxHP[NUM_CLASSES] = {120, 80, 100};
int classAttack[NUM_CLASSES] = {8, 12, 10};
string classDescriptions[NUM_CLASSES] = {
    "High HP, moderate damage - survives longer",
    "Low HP, high damage - glass cannon",
    "Balanced HP and damage - versatile"
};

// ============================================================================
// DISPLAY FUNCTION
// ============================================================================
// TEACHING POINT: This is the "show inventory" pattern from M5LAB_A Ex 3

void displayCharacterSelection() {
    cout << "\n╔════════════════════════════════════════╗\n";
    cout << "║     ⚡ CHOOSE YOUR HERO ⚡            ║\n";
    cout << "╚════════════════════════════════════════╝\n\n";
    
    // Loop through array - notice i < NUM_CLASSES (not <=)
    for (int i = 0; i < NUM_CLASSES; i++) {
        // Display as 1, 2, 3 (human numbering) not 0, 1, 2 (array indexing)
        cout << (i + 1) << ". " << classEmojis[i] << " " << classNames[i] << "\n";
        cout << "   HP: " << classMaxHP[i] 
             << " | Attack: " << classAttack[i] << "\n";
        cout << "   " << classDescriptions[i] << "\n\n";
    }
}

// ============================================================================
// INPUT VALIDATION FUNCTION
// ============================================================================
// TEACHING POINT: Must check if choice is within array bounds

int getCharacterChoice() {
    int choice;
    bool validChoice = false;
    
    while (!validChoice) {
        cout << "Enter your choice (1-" << NUM_CLASSES << "): ";
        cin >> choice;
        
        // Valid choices are 1, 2, 3 (not 0, 4, etc.)
        if (choice >= 1 && choice <= NUM_CLASSES) {
            validChoice = true;
        } else {
            cout << "❌ Invalid choice. Try again.\n";
        }
    }
    
    // Convert human numbering (1-3) to array index (0-2)
    return choice - 1;
}

// ============================================================================
// MAIN - STAGE 1
// ============================================================================

int main() {
    cout << "╔═══════════════════════════════════════════╗\n";
    cout << "║  🏛️  GREEK MYTH ROGUELIKE (STAGE 1) 🏛️   ║\n";
    cout << "╚═══════════════════════════════════════════╝\n";
    
    // Display all characters
    displayCharacterSelection();
    
    // Get player's choice
    int playerClassIndex = getCharacterChoice();
    
    // Retrieve data from arrays using the index
    string playerName = classNames[playerClassIndex];
    string playerEmoji = classEmojis[playerClassIndex];
    int playerMaxHP = classMaxHP[playerClassIndex];
    int playerAttack = classAttack[playerClassIndex];
    
    // Show confirmation
    cout << "\n✅ You have chosen: " << playerEmoji << " " << playerName << "\n";
    cout << "   Max HP: " << playerMaxHP << "\n";
    cout << "   Attack: " << playerAttack << "\n\n";
    
    cout << "🎯 Stage 1 Complete! Character selection works.\n";
    cout << "Next: Add encounter loop (Stage 2)\n\n";
    
    return 0;
}

/*
================================================================================
DISCUSSION QUESTIONS FOR STUDENTS (After running Stage 1):
================================================================================

1. "How many arrays are we using?" (5 parallel arrays)
2. "What does the [i] mean?" (Index - which element we're accessing)
3. "Why do we add 1 when displaying?" (Humans count from 1, arrays from 0)
4. "What happens if I enter 0?" (Validation rejects it)
5. "What happens if I enter 4?" (Validation rejects it)
6. "How would we add a 4th class?" (Add to each array, change NUM_CLASSES)

KEY TAKEAWAY: Arrays let us organize related data, loops let us work with it.
This is the same pattern you'll use for inventory systems, enemy databases,
level progression, and countless other game features.

================================================================================
*/