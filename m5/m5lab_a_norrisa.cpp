/*
M5LAB_A - norrisa's version
part 1 for now: healing loop
10/28/25
*/

#include <iostream>
using namespace std;

/*
The Pattern You're Learning:
while (not there yet) {
move closer
show progress
}
Step-by-Step Build:
Step 1: Set up your variables
int health = 30;
int maxHealth = 100;
Step 2: Add the basic loop
while (health < maxHealth) {
// we'll fill this in next
}
Step 3: Heal inside the loop

*/

int main() {
    // TODO: Put the healing code into its own function.
    int maxHP   = 100;
    int hp      = 30;
    const int healing = 10;

    cout << "Resting until healed." << endl;
    while (hp < maxHP) {
        hp += healing;  
        cout << "HP: " << hp << "/" << maxHP << endl;
    }
    cout << "Fully rested." << endl;

}