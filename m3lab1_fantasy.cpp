#include <iostream>
using namespace std;

// ========== FUNCTION PROTOTYPES ==========
// Declare all your "rooms" up here
void tavern();      // Starting location
void forest();      // A possible path
void castle();      // Another path
void gameOver();    // An ending
void victory();     // Another ending

// ========== MAIN FUNCTION ==========
int main()
{
    cout << "==================================" << endl;
    cout << "     WELCOME TO YOUR ADVENTURE   " << endl;
    cout << "==================================" << endl;
    cout << endl;
    
    // Start the adventure!
    tavern();
    
    cout << "\n=== THE END ===" << endl;
    return 0;
}

// ========== LOCATION FUNCTIONS ==========
// Each function is one "node" in your story

void tavern()
{
    cout << "\nYou wake up in a dusty tavern." << endl;
    cout << "The bartender says there's trouble in the kingdom." << endl;
    cout << "Will you help? (1 = Yes, 2 = No): ";
    
    int choice;
    cin >> choice;
    
    if (choice == 1)
    {
        cout << "\n'Brave soul! Head to the forest!'" << endl;
        forest();  // Go to forest function
    }
    else
    {
        cout << "\n'Coward! Get out of my tavern!'" << endl;
        gameOver();  // Go to game over
    }
}

void forest()
{
    // TODO: Add your forest scene here!
    cout << "\n[Forest scene not yet written]" << endl;
}

void castle()
{
    // TODO: Add your castle scene here!
    cout << "\n[Castle scene not yet written]" << endl;
}

void gameOver()
{
    cout << "\n💀 GAME OVER 💀" << endl;
    cout << "Your adventure ends here." << endl;
}

void victory()
{
    cout << "\n🏆 VICTORY! 🏆" << endl;
    cout << "You saved the kingdom!" << endl;
}