"""
CSC 134
M2LAB2 - Python Turtle
norrisa
9/10/25
Purpose: Make some interesting shapes.
"""


import turtle as t
import random
# Make it faster!
t.speed(0) # 0 = fastest, 1 = slowest, 6 = normal
# Make it prettier!
t.bgcolor("black")
t.pencolor("white")
t.pensize(3)

# Basic: Square
for i in range(4):
    t.forward(100)
    t.right(90)
# Evolving: Spiral
for i in range(200):
    t.forward(i * 2) # Gets bigger each time!
    t.right(121) # Not quite 90... see what happens!
# Your turn: What if the angle changed too?

# Turtle with boundaries
for step in range(500):
    t.forward(5)
    # The turtle asks: "Am I too far right?"
    if t.xcor() > 200:
        t.left(135)
    # The turtle asks: "Am I too far left?"
    if t.xcor() < -200:
        t.right(135)
