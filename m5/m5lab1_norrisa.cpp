/*
CSC 134
M5Lab1 - CYOA
norrisa
11/5/25
Uses "procedural programming".
*/

#include <iostream>
using namespace std;

// Function declarations
int getPlayerChoice(int maxChoice); // let player choose options


// main()
int main() {
    int choice;
    int max = 3;
    cout << "TESTING: Choose 1, 2, or 3." << endl;
    choice = getPlayerChoice(max);
    cout << "You chose: " << choice << endl;

    // ending
    return 0;
}

// Function definitions
/**
 * Get a valid choice from the player.
 * example: if maxChoice is 3, they can choose 1, 2, or 3.
 */
int getPlayerChoice(int maxChoice) {
    int choice;
    while (true) {
        cout << "Your choice: ";
        cin >> choice;
        // You can add extra validation if you want.

        // Validate range 
        if (choice >= 1 && choice <= maxChoice) {
            return choice; // same number they enter
        }

        cout << "Please choose between 1 and " << maxChoice << ".\n";
    }
}
