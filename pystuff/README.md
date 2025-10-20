Here are some of the prompts I used:

here's a bouncing ball but it just leaves the screen:
<code>
please update this so that the ball bounces off the edges like your favorite dvd screen saver

saved changes from test.py to bounce.py

next version:

Can you make this have several balls of different colors all bouncing at once?

This is bounceclaude.py

-----
final version, make the balls bounce off each other also, if possible

response: bouncemulti.py

Done! Now the balls bounce off each other realistically. This adds several important concepts:
Nested loops:

for i in range(len(balls)): with for j in range(i + 1, len(balls)): - checks each pair of balls exactly once (efficient collision detection pattern)

More complex if statements:

Collision detection: checking if distance < sum of radii
Only resolving collisions when balls are moving toward each other
Preventing division by zero

Additional functions:

get_distance() - uses the Pythagorean theorem
check_ball_collision() - returns boolean based on distance check
resolve_ball_collision() - implements simplified elastic collision physics

Math operations:

Distance calculation with math.sqrt()
Dot product for velocity projection
Vector normalization

The collision physics uses a simplified elastic collision model (assuming equal mass). The nested loop pattern for checking all pairs is a classic algorithm concept that translates directly to C++.

-----
LAST ONE
! This lunar lander simulator demonstrates all the key concepts:
If statements:

Fuel availability checks
Thrust direction logic
Safe vs. crashed landing conditions
Velocity-based color coding
Boundary collision detection

Loops:

Main game loop (while running)
Event processing loop

Functions:

create_lander() - initializes lander state
apply_gravity() - simulates moon gravity
apply_thrust() - handles user input with fuel consumption
check_landing() - determines landing success/failure
Multiple drawing functions

Physics:

Continuous gravity acceleration
Thrust in three directions (up, left, right)
Safe landing requires low total velocity AND low horizontal velocity
Fuel consumption

Controls:

W: Main thrust (upward)
A: Left thrust
D: Right thrust
R: Reset

Goal: Land gently with velocity under 2.0 and minimal horizontal speed. The HUD shows your velocity in red if too fast, green if safe. Try to land smoothly!
