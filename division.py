# r4 = r2 // r3
# r5 = r2 % r3
# r2, r3 are positive
from bcpu import *

# testing data
p2 = p2p = 0 # numerator
p3 = p3p = 0 # denominator

if p3 == 0:
    p4 = -1
    p5 = -1
else:
    p4 = 0 # quotient
    p5 = r2 # remainder
    while p2 >= p3:
        p2 = p2 - p3
        p4 = p4 + 1
    p5 = p2

print(p2p, p3p, p4, p5)

div = '''
# if p3 == 0:
# goto >else if p3 != 0
Addi(r10, pc, 7) # >else
Movex(pc, r10, r3)
    Set(r0, 0)
    Set(r4, 1) # p4 = -1
    Sub(r4, r0, r4)
    Move(r5, r4) # p5 = -1
    # goto >endif
    Addi(pc, pc, 9)
# >else:
    Set(r4, 0) # p4 = 0 # quotient
    Move(r5, r2) #p5 = r2 # remainder
    # >while p5 >= p3:
    # goto >endwhile if p5 < p3
    Sub(r9, r5, r3)
    Addi(r10, pc, 5) # >endwhile
    Moven(pc, r10, r9)
        Addi(r4, r4, 1) # p4 = p4 + 1
        Sub(r5, r5, r3) # p5 = p5 - p3
        # goto >while
        Subi(pc, pc, 5)
    # >endwhile
# >endif
Move(r4, r4)
Move(r5, r5)
'''

load(div)
# testing data
Set(r2, 200) # p2 = p2p = 0 # numerator
Set(r3, 3) # p3 = p3p = 0 # denominator
run()
