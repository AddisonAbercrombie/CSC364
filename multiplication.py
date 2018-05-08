from bcpu import *

mul = '''
# fix sign
# if r2 > 0:
# goto >endif if r2 >= 0
Addi(r10, pc, 4) # >endif
Movep(pc, r10, r2)
    Sub(r2, r0, r2) # p2 = -p2
    Sub(r3, r0, r3) # p3 = -p3
# >endif
# mul by adding
Set(r4, 0) # p4 = 0
# >while p2 > 0:
# goto >endwhile if p2 <= 0
Addi(r10, pc, 6) # >endwhile
Sub(r9, r0, r2)
Movep(pc, r10, r9)
    Add(r4, r4, r3) # p4 = p4 + p3
    Subi(r2, r2, 1) # p2 = p2 -1
    #update var
    Subi(pc, pc, 4)
# >endwhile
Move(r4, r4)
'''

load(mul)
printm()
