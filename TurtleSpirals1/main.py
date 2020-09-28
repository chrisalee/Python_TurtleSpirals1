from turtle import *

# Playing around with the numbers in the forward and left commands, you can see that in both lines, smaller values make for a smoother and tighter spiral (see the example below). Decimal values below 1 are also allowed!

for i in range(80):
    forward(3 * i)
    left(45)

for i in range(300):
    forward(0.05 * i)
    left(10)

bye()
