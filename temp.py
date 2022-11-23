import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lowest = 5527
neg = 0
same = 0
n = int(input())  # the number of temperatures to analyse
a = [n]
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t > 0:
        a = t
        if a < lowest:
            lowest = a
        if a == lowest:
            same = 1
    elif t < 0:
        a = -t
        if a < lowest:
            lowest = a
            neg = 1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
if n == 0:
    print("0")
elif neg == 1:
    if same == 1:
        print(lowest)
    else:
        print(-lowest)

else:
    print(lowest)