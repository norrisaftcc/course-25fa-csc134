#include <iostream>
using namespace std;


int main() {

    int health = 50;
    int maxHealth = 100;

    cout << "Resting to recover..." << endl;

    while (health < maxHealth)
    {
        health = health + 10;
        cout << "Health: " << health << "/" << maxHealth << endl;
    }

    cout << "Fully recovered!" << endl;

    cout << "FOR LOOP:" << endl;
    for (int foo = 1; foo <= 10; foo = foo + 1) {
        cout << foo << endl;
    }

    cout << "=== CHARACTER STATS ===" << endl;

    for (int i = 1; i <= 5; i++)
    {
        cout << "Stat " << i << ": " << (i * 2 + 10) << endl;
    }

    cout << "======================" << endl;

    // array of pc's equipment
    const int MAX_ITEMS = 5;
    string equipment[MAX_ITEMS] = {
    "Iron Sword",
    "Leather Armor", 
    "Health Potion",
    "Magic Ring",
    "Rope"
    };

    for (int i = 0; i < MAX_ITEMS; i++) {
        cout << equipment[i] << endl;
    }
    string searchItem = "Health Potion";
    bool found = false;

    for (int i = 0; i < 5; i++)
    {
        if (equipment[i] == searchItem)
        {
            cout << "Found " << searchItem << " at slot " << (i+1) << endl;
            found = true;
        }
    }

    if (!found)
    {
        cout << searchItem << " not found!" << endl;
    }
}
