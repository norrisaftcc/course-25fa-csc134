/*
CSC 134
M5T1 - Basic Functions
norrisa
10/22/25

Purpose: Demo void and value-returning functions.
*/
#include <iostream>
using namespace std;

// Function Declarations (Definitions are at the bottom)
void say_hello(); // says hi

int get_the_answer(); // provides the answer to everything

double double_a_number(); // num times two

int main() {
    // This program does nothing useful!
    double my_num;
    int    another_num;

    cout << "Welcome to the best program ever!" << endl;
    cout << "Please enter a number (with or without decimal place)." << endl;
    cin >> my_num;
    my_num = my_num * 2;
    cout << "Double the number is: " << my_num << endl;

}