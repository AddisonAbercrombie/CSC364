from bcpu import *

print('Setting initial bits')
Set(r0, 0)
Set(r1, 1)
Set(r2, 0b10010110)
Seth(r2, 0b11101100)
Set(r3, 0b00100101)
Seth(r3, 0b11100000)

print('Setting r4 = r2 - r3')
Sub(r4, r2, r3) # r4 = r2 - r3
print('r2 == r3')
Movez(r10, r1, r4) # r2 == r3
Set(r10, 0)
print('r2 != r3')
Movex(r10, r1, r4) # r2 != r3
Set(r10, 0)
print('r2 >= r3')
Movep(r10, r1, r4) # r2 >= r3
Set(r10, 0)
print('r2 < r3')
Moven(r10, r1, r4) # r2 < r3
Set(r10, 0)
print('Setting r4 = r3 - r2')
Sub(r4, r3, r2) # r4 = r3 - r2
print('r3 <= r2')
Movep(r10, r1, r4) # r3 >= r2
Set(r10, 0)
print('r2 > r3')
Moven(r10, r1, r4) # r2 > r3

