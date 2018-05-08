from bcpu import *

Addr.mulfn = 300

mul = """
#>mul(r2, r3) -> r4:
# fix sign
# if p2 < 0:
# goto >endif if p2 >= 0
Addi(r10, pc, 5)
Movep(pc, r10, r2)
    Set(r0, 0)
    Sub(r2, r0, r2) # p2 = -p2
    Sub(r3, r0, r3) # p3 = -p3
# >endif

# mul
Set(r1, 1) # p1 = 1
Set(r4, 0) # p4 = 0

# while p1 < 0b10000000000000000:
# goto >endwhile if p1 == 0
Addi(r10, pc, 9)
Movez(pc, r10, r1)
    And(r9, r1, r2)# p9 = p1 & p2
    Set(r0, 0) # p0 = 0
    Movex(r0, r3, r9) # p0 = p3 if p9 != 0 else p0
    Add(r4, r4, r0) # p4 = p4 + p0
    Add(r1, r1, r1) # p1 = p1 + p1 # shift left
    Add(r3, r3, r3) # p3 = p3 + p3 # shift left
    Subi(pc, pc, 7)
# >endwhile
Move(r4, r4)

# return
Load(r13, st)
Subi(st, st, 1)
Move(pc, r13)
"""

load(mul)

"""
R[2] = getb(-4)
R[3] = getb(3)
runfast()
printi(R[r4])
"""
