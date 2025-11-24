#include <iostream>
#include <fstream>

using namespace std;

int main() {
    // 1. Define image dimensions (Must be at least 100x100)
    const int width = 400;
    const int height = 400;

    // 2. Open the file using ofstream
    ofstream img("robot.ppm");

    // Check if file opened successfully
    if (!img.is_open()) {
        cerr << "Error: Could not open file for writing." << endl;
        return 1;
    }

    // 3. Write the PPM Header
    // P3 = ASCII color, width height, 255 = max color value
    img << "P3" << endl;
    img << width << " " << height << endl;
    img << "255" << endl;

    // 4. Use nested loops to generate pixel data
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            
            int r = 0, g = 0, b = 0;

            // Logic to draw "Boxes" based on x and y coordinates
            
            // Background Color (Dark Grey)
            r = 30; g = 30; b = 30; 

            // The Head (Large Silver Box)
            if (x > 50 && x < 350 && y > 50 && y < 350) {
                r = 200; g = 200; b = 200;
            }

            // The Left Eye (Red Box)
            if (x > 100 && x < 160 && y > 120 && y < 180) {
                r = 255; g = 50; b = 50;
            }

            // The Right Eye (Red Box)
            if (x > 240 && x < 300 && y > 120 && y < 180) {
                r = 255; g = 50; b = 50;
            }

            // The Mouth (Green Rectangle Box)
            if (x > 120 && x < 280 && y > 250 && y < 300) {
                r = 50; g = 255; b = 50;
            }

            // An Antenna (Blue Box on top)
            if (x > 180 && x < 220 && y > 20 && y < 50) {
                r = 50; g = 100; b = 255;
            }

            // Write the RGB triplet to the file
            img << r << " " << g << " " << b << "\n";
        }
    }

    // Close the file
    img.close();

    cout << "Success! 'robot.ppm' has been created." << endl;
    return 0;
}