/*
CSC 134
While vs. For
norrisa
11/10/25

Do the same thing with while and for loops, for reference.
*/

#include <iostream>
using namespace std;

int main() {
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

    return 0;
}

