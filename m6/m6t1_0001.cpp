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
    method2();

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
    poke_avg = (double) poke_total / SIZE;
    cout << "Average = " << poke_avg << endl;
}

void method2() {
    // Method 2 uses two arrays:
    // Names of the days
    // # pokemon found on the days

    const int SIZE = 5;
    string days[SIZE] = {"M", "T", "W", "Th", "F"}; // initialized
    int pokemon[SIZE]; // not initialized
    int poke_total = 0;
    double poke_avg = 0.0;

    for (int i=0; i < SIZE; i++) {
        cout << "# on " << days[i] << ": ";
        cin >> pokemon[i];
    }
    // print output in "tabular" (table) format
    cout << "Day\tPokemon" << endl;
    for (int i=0; i < SIZE; i++) {
        cout << days[i] << "\t" << pokemon[i] << endl;
        // find the total
        poke_total += pokemon[i];
    }
    // find total, print results
    poke_avg = (double) poke_total / SIZE;
    cout << "Total = " << poke_total << endl;
    cout << "Average = " << poke_avg << endl;

}