import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
lx, ly, x, y = [int(i) for i in input().split()]
dir = ""
n = 0
s = 0
e = 0
w = 0

if ly - y < 0:
    n = -(ly - y)
elif ly - y > 0:
    s = ly - y

if lx - x < 0:
    w = -(lx - x)
elif lx - x > 0:
    e = lx - x
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    dir = ""

    if n > 0:
        dir+="N"
        n = n - 1
    elif s > 0:
        dir+="S"
        s = s - 1

    if w > 0:
        dir+="W"
        w = w - 1
    elif e > 0:
        dir+="E"
        e = e - 1


    print(dir)