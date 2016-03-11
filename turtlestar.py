import turtle

# Ask user for input here.
num_sides_inp = raw_input("Enter an odd number (number of sides): ")
n= int(num_sides_inp)
while n < 5:
    num_sides_inp = raw_input("Number must be at least 5. Enter a new odd number of sides: ")
    n= int(num_sides_inp)

side_len_inp= raw_input("Enter length of each side: ")
side_len= int(side_len_inp)
while side_len < 0:
    side_len_inp = raw_input("Side length must be greater than 0. Enter a new side length: ")
    side_len = int(side_len_inp)


def draw_star (t, n, side_len):
    for i in range(n):
        t.forward(side_len)
        t.left(-45)
# Now create a graphics window.
bob = turtle.Pen()

# Put the rest of your code can go here

for j in range(n):
    draw_star(bob, n, side_len)



# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
