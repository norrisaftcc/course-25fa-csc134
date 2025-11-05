/*
CSC 134
M5Lab1 - CYOA
norrisa
11/5/25
Uses "procedural programming".
*/


// ============================================================================
// GAME LOGIC FUNCTIONS
// ============================================================================
// These functions handle the mechanics of running the game.

/**
 * Get a valid choice from the player.
 *
 * @param maxChoice Highest valid choice number
 * @return Zero-based index of the chosen option
 *
 */
int getPlayerChoice(int maxChoice) {
    int choice;
    while (true) {
        cout << "Your choice: ";
        cin >> choice;

        // Validate range (remember: player sees 1-N, we need 0-(N-1))
        if (choice >= 1 && choice <= maxChoice) {
            return choice;
        }

        cout << "Please choose between 1 and " << maxChoice << ".\n";
    }
}
