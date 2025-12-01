#include <iostream>
using namespace std;

// CSC 134
// M7T1 - Restaurant Rating
// norrisa
// 12/1/25
// Use Restaurant class to store user ratings

// for comparison...
/*
struct Rest_struct {
    string name;
    double rating;
}
*/

class Restaurant {
  private:
    string name;    // the name
    double rating;  // 0 to 5 stars

  public:
	// constructor 
	Restaurant(string n, double r) {
		name = n;
		rating = r;
	}
	// getters and setters
    void setName(string n) {
        name = n; 
    }
    void setRating(double r) {
        // only valid ratings allowed
        if (r >=0 && r <=5) {
            rating = r; // 0 - 5 stars
        }
        
    }
    string getName() const {
        return name;
    }
    double getRating() const {
        return rating;
    }
  
};

int main() {
    cout << "M7T1 - Restaurant Reviews" << endl;


    // if it were a struct...
    //breakfast.name = "Biscuitville";
    //breakfast.rating = 3.5;

    // but with a class...
    Restaurant breakfast   = new Restaurant("Biscuitville", 3.5);
    Restaurant lunch       = new Restaurant("Mi Casita", 4.0);

    // We'll use a new function, printInfo(), to display Restaurant info
    breakfast.printInfo();
    lunch.printInfo();

    return 0;

}