// M5LAB2
// CSC 134
// norrisa
// 11/3/25
// Completing "Bob's" half-finished program.
// Ask user for length and width of rectangle
// then calculate and print the area.
// (Use functions.)

#include <iostream>
using namespace std;

// Declare (Write the prototypes for)
// the getLength,
// getWidth, getArea, and displayData
// functions here.
// The Declaration "promises" these functions will exist if called.

double getLength(); // get the length
double getWidth();  // get the width
double getArea(double length, double width);   // *calculate* the area 
void   displayData(double length, double width, double area); // display the output

int main()
{
	// This program calculates the area of a rectangle.
	// TODO: fix any syntax errors
	
   double length,    // The rectangle's length
          width,     // The rectangle's width
          area;      // The rectangle's area
          
   // Get the rectangle's length.
   length = getLength();
   
   // Get the rectangle's width.
   width = getWidth()
   
   // Get the rectangle's area.
   area = getArea();
   
   // Display the rectangle's data.
   displayData(length, width, area);
          
   return 0;
}

//***************************************************
// TODO: write the getLength, getWidth, getArea,    *
// and displayData functions below.                 *
//********************************
// Remember, the Definition is fulfilling the "promise" of the Declarations.

//getLength - Asks the user to enter a rectangle's length, and return that value as a double.
double getLength() {
    cout << "Not implemented." << endl;
    return 0.0;
}


//getWidth - Asks the user to enter a rectangle's width, and return that value as a double.
double getWidth() {
    cout << "Not implemented." << endl;
    return 0.0; 
}

//getArea - This function should take two arguments, length and width. It will calculate the area and return that value as a double.
double getArea(double length, double width) {
    cout << "Not implemented." << endl;
    return 0.0;
}

// displayData - Void function, simply outputs the values in a readable format.
void   displayData(double length, double width, double area) {
    cout << "TODO: Display the data" << endl;
}