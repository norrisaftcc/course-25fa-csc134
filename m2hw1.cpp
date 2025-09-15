/*
M2HW1
CSC 134
norrisa
9/15/25
Complete 2,3,or 4 questions.
*/
#include <iostream>
#include <iomanip> // for setprecision
using namespace std;

// for reasons we'll learn later,
// put the other functions above main()

void question1() {
    cout << "Question 1" << endl;

}

void question2() {
    cout << "Question 2" << endl;

}

int main() {
    // Call each question as its own function

    question1();
    question2();

    cout << "Example of printing out correct money values" << endl;
    double cost = 8.0; 
    // magic words for 2 decimal places
    cout << setprecision(2) << fixed; // requires "#include <iomanip>"
    cout << "The cost is: $" << cost << endl;

    return 0;
}