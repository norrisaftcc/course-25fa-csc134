/*
CSC 134
M3T1 - Area of Rectangles
Simple comparison.
norrisa
9/17/25
*/

#include <iostream>
using namespace std;

int main() {

    // Get info on the two rectangles
    double length1, length2, width1, width2;
    double area1, area2;
    cout << "Enter the length and width of two rectangles." << endl;
    cout << "First rectangle." << endl;
    cout << "Length: ";
    cin  >> length1;
    cout << "Width: ";
    cin  >> width1;
    cout << endl;
    cout << "Second rectangle." << endl;
    cout << "Length: ";
    cin  >> length2;
    cout << "Width: ";
    cin  >> width2;

    // Calculate the area
    area1 = length1 * width1;
    area2 = length2 * width2;

    // Print the output
    cout << "First rectangle area  = " << area1 << endl;
    cout << "Second rectangle area = " << area2 << endl;


    return 0; // no errors
}