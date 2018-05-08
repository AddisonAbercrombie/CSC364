# bcpu startup
from bcpu import *

# test bit 4 of r3, if that is 1, set r2 = 1
# else set r2 = 0

# making sure all of our bits are the way we want them
Set(r3, 0b00111100)
Set(r2, 0)
Set(r1, 1)

# seting mask
Set(r4, 0b10000)

# checking bit 4
And(r5, r3, r4)

# changing r2
Movex(r2, r1, r5)

print(R[r2])
