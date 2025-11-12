# CSC 134 - Week 9 Lab: Introduction to Vectors

## Student Handout: RPG Inventory System with std::vector

-----

## 📦 What You’re Building Today

An RPG inventory system that demonstrates the power of vectors over arrays. You’ll be able to:

- Add items dynamically (no size limits!)
- Remove items easily
- Sort your inventory
- Search for items
- Use STL algorithms

-----

## 🔧 Complete Starter Code

Copy this code into a new C++ file (e.g., `inventory_system.cpp`):

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>  // For STL algorithms like sort() and find()
using namespace std;

// Global inventory vector - accessible to all functions
// (In real apps, this would be in a class, but this is great for learning!)
vector<string> inventory;

// Function prototypes
void addItem(const string& item);
void removeItem(const string& item);
void displayInventory();
void sortInventory();
bool hasItem(const string& item);
void displayMenu();

int main() {
    cout << "=== RPG INVENTORY SYSTEM WITH VECTORS ===" << endl;
    cout << "Watch how vectors handle dynamic data!\n" << endl;
    
    // Add some starting items
    addItem("Health Potion");
    addItem("Iron Sword");
    addItem("Wooden Shield");
    addItem("Mana Potion");
    addItem("Ancient Key");
    
    displayInventory();
    
    // Demonstrate sorting
    cout << "\n--- Sorting inventory alphabetically ---" << endl;
    sortInventory();
    displayInventory();
    
    // Demonstrate searching
    string searchItem = "Iron Sword";
    if (hasItem(searchItem)) {
        cout << "\n✓ You have a " << searchItem << "!" << endl;
    } else {
        cout << "\n✗ You don't have a " << searchItem << "." << endl;
    }
    
    // Demonstrate removal
    cout << "\n--- Removing Wooden Shield ---" << endl;
    removeItem("Wooden Shield");
    displayInventory();
    
    // Try to remove something that doesn't exist
    cout << "\n--- Trying to remove Diamond Armor ---" << endl;
    removeItem("Diamond Armor");
    
    // Interactive menu (optional - uncomment to use)
    // char choice;
    // do {
    //     displayMenu();
    //     cin >> choice;
    //     cin.ignore();  // Clear newline from input buffer
    //     
    //     string itemName;
    //     switch(choice) {
    //         case '1':
    //             cout << "Enter item name: ";
    //             getline(cin, itemName);
    //             addItem(itemName);
    //             break;
    //         case '2':
    //             cout << "Enter item name to remove: ";
    //             getline(cin, itemName);
    //             removeItem(itemName);
    //             break;
    //         case '3':
    //             displayInventory();
    //             break;
    //         case '4':
    //             sortInventory();
    //             displayInventory();
    //             break;
    //         case '5':
    //             cout << "Enter item to search for: ";
    //             getline(cin, itemName);
    //             if (hasItem(itemName)) {
    //                 cout << "✓ Found!" << endl;
    //             } else {
    //                 cout << "✗ Not found." << endl;
    //             }
    //             break;
    //     }
    // } while (choice != '6');
    
    return 0;
}

// Add an item to the inventory
void addItem(const string& item) {
    inventory.push_back(item);  // Vector grows automatically!
    cout << "Added: " << item << endl;
}

// Remove an item from the inventory
void removeItem(const string& item) {
    // Use STL find() to search for the item
    auto it = find(inventory.begin(), inventory.end(), item);
    
    if (it != inventory.end()) {
        inventory.erase(it);  // Vector shrinks automatically!
        cout << "Removed: " << item << endl;
    } else {
        cout << "ERROR: " << item << " not found in inventory." << endl;
    }
}

// Display all items in the inventory
void displayInventory() {
    cout << "\n=== INVENTORY (" << inventory.size() << " items) ===" << endl;
    
    // Check if inventory is empty
    if (inventory.empty()) {
        cout << "Your inventory is empty." << endl;
        return;
    }
    
    // Display each item with a number
    for (size_t i = 0; i < inventory.size(); i++) {
        cout << i + 1 << ". " << inventory[i] << endl;
    }
}

// Sort the inventory alphabetically
void sortInventory() {
    sort(inventory.begin(), inventory.end());
    cout << "Inventory sorted alphabetically." << endl;
}

// Check if an item exists in the inventory
bool hasItem(const string& item) {
    return find(inventory.begin(), inventory.end(), item) != inventory.end();
}

// Display menu for interactive mode
void displayMenu() {
    cout << "\n--- INVENTORY MENU ---" << endl;
    cout << "1. Add item" << endl;
    cout << "2. Remove item" << endl;
    cout << "3. Display inventory" << endl;
    cout << "4. Sort inventory" << endl;
    cout << "5. Search for item" << endl;
    cout << "6. Quit" << endl;
    cout << "Choice: ";
}
```

-----

## 💻 How to Compile and Run

### Using g++ (command line):

```bash
g++ -std=c++11 inventory_system.cpp -o inventory
./inventory
```

### Using Visual Studio Code:

1. Open the file in VS Code
1. Press `Ctrl+Shift+B` (Windows/Linux) or `Cmd+Shift+B` (Mac)
1. Select “C++: g++ build active file”
1. Run in terminal

### Using Code::Blocks or other IDE:

1. Create a new project
1. Add the .cpp file
1. Build and Run (F9)

-----

## 🎯 Expected Output

```
=== RPG INVENTORY SYSTEM WITH VECTORS ===
Watch how vectors handle dynamic data!

Added: Health Potion
Added: Iron Sword
Added: Wooden Shield
Added: Mana Potion
Added: Ancient Key

=== INVENTORY (5 items) ===
1. Health Potion
2. Iron Sword
3. Wooden Shield
4. Mana Potion
5. Ancient Key

--- Sorting inventory alphabetically ---
Inventory sorted alphabetically.

=== INVENTORY (5 items) ===
1. Ancient Key
2. Health Potion
3. Iron Sword
4. Mana Potion
5. Wooden Shield

✓ You have a Iron Sword!

--- Removing Wooden Shield ---
Removed: Wooden Shield

=== INVENTORY (4 items) ===
1. Ancient Key
2. Health Potion
3. Iron Sword
4. Mana Potion

--- Trying to remove Diamond Armor ---
ERROR: Diamond Armor not found in inventory.
```

-----

## 🔍 Key Concepts to Understand

### 1. Vector Declaration

```cpp
vector<string> inventory;  // Creates an empty vector of strings
```

**Compare to array:**

```cpp
const int SIZE = 100;
string inventory[SIZE];  // Fixed size, wastes memory
```

### 2. Adding Elements

```cpp
inventory.push_back("Health Potion");  // Adds to end, grows automatically
```

**Try with array:** You’d need to track size manually and check for overflow.

### 3. Removing Elements

```cpp
auto it = find(inventory.begin(), inventory.end(), item);
inventory.erase(it);  // Removes and shifts everything automatically
```

**Try with array:** Manual loop to find, manual shifting of all elements after.

### 4. Size Tracking

```cpp
inventory.size()   // Always accurate
inventory.empty()  // Check if empty
```

**Try with array:** You maintain a separate `int currentSize` variable everywhere.

### 5. Iterators

```cpp
inventory.begin()  // Points to first element
inventory.end()    // Points PAST last element (used as "not found" marker)
```

-----

## 🚀 Practice Challenges

### Challenge 1: Count Item Types (Easy)

Add a function that counts how many potions are in the inventory:

```cpp
int countPotions() {
    // Use count_if with a lambda function
    // Hint: Check if item contains the word "Potion"
}
```

### Challenge 2: Display Items Starting With Letter (Medium)

```cpp
void displayItemsStartingWith(char letter) {
    // Loop through inventory
    // Display only items that start with the given letter
}
```

### Challenge 3: Find Most Valuable Item (Medium)

Create a vector of item values and find the most expensive item:

```cpp
vector<string> items = {"Sword", "Potion", "Shield"};
vector<int> values = {100, 25, 75};

// Write a function that finds and displays the most valuable item
```

### Challenge 4: Remove All Potions (Hard)

```cpp
void removeAllPotions() {
    // Use remove_if with a lambda to remove ALL items containing "Potion"
    // Hint: remove_if + erase = the "erase-remove idiom"
}
```

### Challenge 5: Party Health Tracker (Project)

Create a complete new program using vectors:

- `vector<string> partyNames` for character names
- `vector<int> partyHP` for health points
- Functions: `addMember()`, `healAll()`, `damageParty()`, `getAverageHP()`, `displayParty()`

-----

## 📚 Important Vector Methods to Know

|Method           |What It Does                 |Example                 |
|-----------------|-----------------------------|------------------------|
|`push_back(item)`|Add to end                   |`vec.push_back(5);`     |
|`pop_back()`     |Remove from end              |`vec.pop_back();`       |
|`size()`         |Get number of elements       |`int n = vec.size();`   |
|`empty()`        |Check if empty               |`if (vec.empty()) {...}`|
|`clear()`        |Remove all elements          |`vec.clear();`          |
|`at(index)`      |Access with bounds check     |`vec.at(0)`             |
|`[index]`        |Access without check (faster)|`vec[0]`                |
|`front()`        |First element                |`vec.front()`           |
|`back()`         |Last element                 |`vec.back()`            |
|`erase(iterator)`|Remove element               |`vec.erase(it);`        |

-----

## 🎨 Extension Ideas (For After You Finish)

1. **Add Item Quantities**: Instead of `vector<string>`, use a struct or pair to track quantities
1. **Weapon Categories**: Separate vectors for weapons, armor, consumables
1. **Rarity System**: Add rare/common/legendary item types
1. **Weight Limit**: Track total weight, limit inventory size
1. **Save/Load**: Write inventory to a file, load it back
1. **Search Improvements**: Partial matching (search “pot” finds “Potion”)

-----

## ⚠️ Common Mistakes to Avoid

1. **Forgetting `#include <algorithm>`**
- You need this for `sort()`, `find()`, `count_if()`, etc.
1. **Not checking if vector is empty before accessing**
   
   ```cpp
   if (!inventory.empty()) {
       cout << inventory[0];  // Safe!
   }
   ```
1. **Using `inventory.end()` as a valid index**
- `.end()` points PAST the last element (it’s a sentinel)
- It’s used for “not found” checks, not for accessing data
1. **Forgetting to capture lambda variables**
   
   ```cpp
   // Wrong:
   [](const string& s) { return s[0] == letter; }  // letter not captured!
   
   // Right:
   [letter](const string& s) { return s[0] == letter; }  // letter captured
   ```
1. **Modifying vector while iterating (use remove_if pattern)**
   
   ```cpp
   // Wrong:
   for (auto it = vec.begin(); it != vec.end(); ++it) {
       vec.erase(it);  // Iterator becomes invalid!
   }
   
   // Right: Use erase-remove idiom (we'll learn this later)
   ```

-----

## 📝 Submission Checklist

When you submit this lab, make sure you have:

- [ ] Complete working code that compiles without errors
- [ ] Code runs and produces expected output
- [ ] At least ONE challenge completed (your choice)
- [ ] Comments explaining what your code does
- [ ] Your name and the date at the top of the file
- [ ] (If you used AI): Your prompts saved in a separate text file

-----

## 💡 Discussion Questions (Think About These)

1. When would you still choose an array over a vector?
1. What happens behind the scenes when a vector grows?
1. Why is removing from the middle of a vector potentially slow?
1. How does `find()` know when to stop searching?
1. What’s the difference between `vec[i]` and `vec.at(i)`?

-----

## 🌟 Bonus: The Power of STL Algorithms

Try these one-liners (after you’ve got the basics working):

```cpp
// Reverse the entire inventory
reverse(inventory.begin(), inventory.end());

// Check if ANY items start with 'M'
bool hasM = any_of(inventory.begin(), inventory.end(),
                   [](const string& s) { return s[0] == 'M'; });

// Count total characters in all item names
int totalChars = accumulate(inventory.begin(), inventory.end(), 0,
                            [](int sum, const string& s) { return sum + s.length(); });

// Create a vector of item lengths
vector<int> lengths;
transform(inventory.begin(), inventory.end(), back_inserter(lengths),
          [](const string& s) { return s.length(); });
```

These are advanced concepts - don’t worry if they look confusing now. By the end of the semester, you’ll understand every part of these statements!

-----

## 📞 Need Help?

- **Compilation errors?** Check that you have `#include <algorithm>` at the top
- **Logic errors?** Add `cout` statements to trace what’s happening
- **Segmentation fault?** Probably accessing an invalid index - use `.at()` to get better error messages
- **AI allowed?** Yes! But make sure you understand the code and save your prompts

-----

**Good luck, and welcome to the world of STL containers!** 🎮✨

*Remember: The best way to learn is to experiment. Break things, fix them, and understand why they broke in the first place.*