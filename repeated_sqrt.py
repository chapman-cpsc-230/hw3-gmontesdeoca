from math import sqrt
for n in range(1,60):
    r=2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2
print "%d times sqrt and **2: %.16f" % (n, r)

# This program takes a number between 1 and 60 and sets the value
# of the number equal to 2. The program then takes the square root of
# 2 in the for loop, and following that raises r (2) to the second
# power. The action is repeated 59 times.
# The range in the program causes round off error and as a result the
# program contains a bug. The answer should instead be 2.


from math import sqrt
for n in range(1,25):
    r=2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2
print "%d times sqrt and **2: %.16f" % (n, r)

# The program can be run and produce the correct result without
#being affected by round off error in the range (1,25)
