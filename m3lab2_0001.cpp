/*
M3LAB2 - Letter Grades (changed to Game Mechanics Test)
CSC 134
norrisa
9/29/25
*/

#include <iostream>
#include <cstdlib>  // for rand() and srand()
#include <ctime>    // for time()

using namespace std;

// to make things easier, we'll write the code in a function
// DECLARE the functions here
void letter_grader();
void combat();

int main() {

    letter_grader();
    // combat();
    return 0;
}

// DEFINE the other functions here

void letter_grader() {
    // input a number grade
    // respond with a letter grade
    double num_grade;
    string letter_grade;
    cout << "Enter a number grade 0-100: ";
    cin >> num_grade;

    // Create the if statements
    letter_grade = "A";

    // Output the answer
    cout << "A number grade of " << num_grade << " is: " << letter_grade;
    cout << endl << endl;

}