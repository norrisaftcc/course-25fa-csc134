/*
CSC 134
M6T1 - Loops and Arrays
norrisa
11/10/25

Do the same thing with while and for loops, for reference.
*/

#include <iostream>
using namespace std;

// Function Declarations
void method1();
void method2();

// main
int main() {
    // Count # of Pokemon per day, two different ways
    method1();
    //method2();

    return 0;
}

// function definitions
void method1() {
    // Method one - no arrays
    // Count 5 days Pokemon, get total and average
    cout << "Enter each Pokemon found per day." << endl;
    cout << "Day 0 = Monday, Day 4 = Friday" << endl;
    const int SIZE = 5;
    int count = 0;
    int poke_today;     // current value, to add
    int poke_total = 0; // add up 
    double poke_avg = 0;// average

    while (count < SIZE) {
        cout << "Day " << count << ": ";
        cin >> poke_today;
        poke_total += poke_today;
        count++; // Move to next day
    }
    cout << "Total = " << poke_total << endl;
}

void method2() {
    // Method 2 - with arrays
    const int SIZE = 3;
    int temps[SIZE];

    for (int i=0; i < SIZE; i++) {
        // standard counting loop
        cout << "Enter temp #" << i << ": ";
        cin >> temps[i];
    }
    for (int i=0; i < SIZE; i++) {
        cout << "Temp #" << i << " = " << temps[i] << endl;
    }

    // Same, but with while loop
    int count=0;
    while (count < SIZE) {
        cout << "Temp #" << count << " = " << temps[count] << endl;
        count++; // move to next
    }

    // Finally, with a do while
    count = 0;
    do {
        cout << "Temp #" << count << " = " << temps[count] << endl;
        count++; // move to next
    } while (count < SIZE);
}