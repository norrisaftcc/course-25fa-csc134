/*
M3T2 - Craps Part 1
CSC 134
norrisa
9/22/25
Beginning of the craps game.
*/

#include <iostream>
#include <cstdlib>
#include <ctime>


using namespace std;

// DECLARE Helper Functions 
int roll();

// main
int main() {
    //int num = roll();
    //cout << num << endl;
    // MAIN CRAPS CYCLE
    // For now:
    /*
    - roll 2d6 (2-12)
    - branch based on win, lose, or point
    - rest comes later
    */
    int roll1;
    int roll2;
    int point;      // roll if it doesn't immediately win/lose

    // Roll the dice
    roll1 = roll();
    roll2 = roll();
    int sum = roll1+roll2;
    cout << "ROLL: " << sum << endl;
    // win on 7 or 11
    if ( (sum == 7) || (sum == 11) ) {
        cout << "🎲 Seven or Eleven -- You win!" << endl;
    }
    // lose on 2, 3, 12
    else if ( (sum == 2) || (sum == 3) || (sum == 12) ) {
        cout << "🎲 2,3,12 -- Sorry, you lose." << endl;
    }
    else {
        // set the point
        point = sum;
        cout << "🎲 Rolled a point. " << endl;
        cout << "Your point is: " << point << endl;
    }


    return 0;
}

// DEFINE Helper Functions
int roll() {
    // rolls a six sided die
    // TODO
    return 6;

}