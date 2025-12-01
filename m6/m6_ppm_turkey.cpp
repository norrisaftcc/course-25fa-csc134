#include <iostream>
#include <fstream>
#include <cmath> // Needed for sqrt and pow to draw circles

using namespace std;

int main() {
    // 1. Define image dimensions
    const int width = 256;
    const int height = 256;

    // 2. Open the file
    ofstream img("turkey.ppm");

    if (!img.is_open()) {
        cerr << "Error: Could not open file." << endl;
        return 1;
    }

    // 3. PPM Header
    img << "P3" << endl;
    img << width << " " << height << endl;
    img << "255" << endl;

    // 4. Generate Pixel Data
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            
            // Default Background: Light Blue (Sky)
            int r = 135;
            int g = 206;
            int b = 235;

            // Geometry calculations
            // Calculate distance from center points for circular shapes
            // Note: (0,0) is top-left
            
            // --- TAIL FEATHERS (The Fan) ---
            // A large semi-circle behind the turkey
            int tail_cx = 128;
            int tail_cy = 160;
            double tail_dist = sqrt(pow(x - tail_cx, 2) + pow(y - tail_cy, 2));
            
            // If inside the outer arc AND above the center point (semi-circle)
            if (tail_dist < 100 && y < tail_cy + 20) {
                // Stripe pattern for feathers based on angle or distance
                // Simple concentric bands:
                if (tail_dist > 80) { r = 255; g = 0; b = 0; }       // Red tips
                else if (tail_dist > 60) { r = 255; g = 165; b = 0; }// Orange middle
                else { r = 139; g = 69; b = 19; }                    // Brown base
            }

            // --- LEGS ---
            // Simple orange vertical lines
            if (y > 210 && y < 240) {
                // Left leg
                if (x > 110 && x < 115) { r = 255; g = 140; b = 0; }
                // Right leg
                if (x > 141 && x < 146) { r = 255; g = 140; b = 0; }
            }
            // Feet
            if (y >= 240 && y < 245) {
                if ((x > 100 && x < 125) || (x > 131 && x < 156)) {
                    r = 255; g = 140; b = 0; 
                }
            }

            // --- BODY ---
            // A circle in the lower center
            int body_cx = 128;
            int body_cy = 170;
            double body_dist = sqrt(pow(x - body_cx, 2) + pow(y - body_cy, 2));

            if (body_dist < 50) {
                r = 139; g = 69; b = 19; // SaddleBrown
            }

            // --- HEAD/NECK ---
            // A smaller circle on top of the body
            int head_cx = 128;
            int head_cy = 100;
            double head_dist = sqrt(pow(x - head_cx, 2) + pow(y - head_cy, 2));

            if (head_dist < 25) {
                r = 160; g = 82; b = 45; // Sienna
            }

            // --- EYES ---
            // Left Eye White
            if (x > 115 && x < 123 && y > 90 && y < 98) { r = 255; g = 255; b = 255; }
            // Left Pupil
            if (x > 119 && x < 121 && y > 92 && y < 96) { r = 0; g = 0; b = 0; }
            
            // Right Eye White
            if (x > 133 && x < 141 && y > 90 && y < 98) { r = 255; g = 255; b = 255; }
            // Right Pupil
            if (x > 135 && x < 137 && y > 92 && y < 96) { r = 0; g = 0; b = 0; }

            // --- BEAK ---
            // Yellow Triangle (approximate with pixel check)
            if (x > 124 && x < 132 && y > 100 && y < 110) {
                r = 255; g = 215; b = 0; // Gold
            }

            // --- WATTLE ---
            // Red dangly bit
            if (x > 128 && x < 134 && y > 110 && y < 125) {
                r = 220; g = 20; b = 60; // Crimson
            }

            img << r << " " << g << " " << b << "\n";
        }
    }

    img.close();
    cout << "Gobble gobble! 'turkey.ppm' generated." << endl;
    return 0;
}