/*
csc 134
m1lab
norrisa
8/27/2025
purpose: The "gem" (replace noun) sales program.
*/

// magic words
#include <iostream>
using namespace std;

int main() {
    // start program
    // declare all of our variables ("whiteboards")
    string item_name = "gem"; // replace with your item
    int    num_items = 10; 
    double cost_per  = 0.25;

    // Give our sales pitch
    cout << "Welcome to the " << item_name << " store!" << endl;
    cout << "Each " << item_name << " is $" << cost_per << endl;
    cout << "We have " << num_items << " total." << endl;
    // do the processing
    double total_cost = num_items * cost_per;
    

    // end program
    return 0;
}