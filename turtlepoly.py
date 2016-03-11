"""
File: turt.py

Copyright (c) 2016 Gabi Montes De Oca

License: MIT

Using turtle program to draw shapes
"""

import turtle

# Ask user for input here.
num_sides_inp = raw_input("Enter number of sides: ")
n= int(num_sides_inp)

side_len_inp= raw_input("Enter length of each side: ")
side_len= int(side_len_inp)

# Now create a graphics window.
bob = turtle.Pen()

# Put the rest of your code can go here
for side in range(n):
    bob.forward(side_len)
    bob.left(360.0/n)
# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
