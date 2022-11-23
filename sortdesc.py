import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

h=[0,0,0,0,0,0,0,0]
highest = 0
hieght = 0
# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        h[i] = mountain_h
        if mountain_h > hieght:
            hieght = mountain_h
            highest = i


    print(highest)
    hieght = 0
