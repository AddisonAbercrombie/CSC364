from bcpu import *

#testing the label

p4 = 0
p2 = 15

while p2 > 0:
    p4 = p4 + p2
    p2 = p2 - 1
    print(p2)

print(p4)

while1='''
Set(r4, 0) # p4 = 0
Set(r2, 15) # p2 = 15

#>while p2 > 0:
# goto >endwhile if p2 <= 0
Set(r0, 0)
Sub(r9, r0, r2)
Addi(r10, pc, ?endwhile)
Movep(pc, r10, r9)
    Add(r4, r4, r2) # p4 = p4 + p2
    Subi(r2, r2, 1) # p2 = p2 - 1
    # goto >while
    Subi(pc, pc, ?while)
#>endwhile
Move(r4, r4)
'''
load(while1)
printm()
run()
