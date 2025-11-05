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
int  getPlayerChoice(int maxChoice); // let player choose options
void showChoices(string choice1, string choice2, string choice3);  // display the player choice menus
// Story choices
void game_start();
const int MAX = 3; // max possible choices per node


// main()
int main() {
    /*
    int choice;
    int max = 3;
    showChoices("1","2","3");
    choice = getPlayerChoice(max);
    cout << "You chose: " << choice << endl;
    */
    // Start the game
    game_start();


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

void showChoices(string choice1, string choice2, string choice3) {
    // A quick menu. If a choice is empty ("") it's not shown
    // but there must always be at least one choice.
    // Example: showChoices("run","fight","hide");
    cout << "---- MAKE YOUR CHOICE ----" << endl;
    int num = 1;
    cout << num << ". " << choice1 << endl;
    num++;

    if (choice2 != "") {
        cout << num << ". " << choice2 << endl;
        num++;
    }

    if (choice3 != "") {
        cout << num << ". " << choice3 << endl;
        num++;
    }

}

//////////////////////////////////////////////////////////
// Story-related functions
// Each story choice leads to a new function
// with new text, and new choices.
//////////////////////////////////////////////////////////

// Game start
void game_start() {
    /* Every node of the story does this:
        - describe what's going on using the R"(message)" 
                cout method.
        - showChoices() with up to 3 strings included
        - getPlayerChoice() with the max set to up to 3
        - if statements to branch to other nodes

    */
   int choice;
   // R for Raw -- print every line as is until it ends
   cout << R"(You're standing in front of the spooky old house again. 
    It's almost Thanksgiving but their Halloween decorations 
    are still up.

    You think you see a light in the back...?
    )";
    // show choices
    showChoices("Go check the front door.",
                "Walk around back and check the garden",
                "Forget it and go home.");
    // make choices
    choice = getPlayerChoice(MAX);
    // branch from here
    // in your program, call another story function!
    if (choice == 1) {
        cout << "Going in the front." << endl;
        // game_front_door(); 
    }
    if (choice == 2) {
        cout << "Headed around back..." << endl;
    }
    if (choice == 3) {
        cout << "Forget it, let's get pizza." << endl;
    }
}