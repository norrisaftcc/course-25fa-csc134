// CSC 134
// M2T1 - Product Sales
// norris
// 9/16/25
// We're going to make the simplest possible
// "checkout" machine. 
#include <iostream>
using namespace std;


int main() {

    // Set up all variables
    string first_name, last_name, full_name; // holds customer name
    string product = "apples"; // change to whatever you like
    double cost_each = 0.99; 
    double total_cost; 


    // Greet the customer
    cout << "Welcome to our " << product << " store!" << endl;
    cout << "What's your first name? ";
    cin >> first_name; 
    cout << "What's your last name? ";
    cin >> last_name;
    full_name = first_name + " " + last_name; 
    cout << "Nice to meet you, " << full_name << endl;

    // Ask how much they'd like to purchase
    

    // Calculate total price
    // Give the result



    return 0; // no errors
}