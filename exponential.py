from bcpu import *

# r4 = r2 ** r3

p2 = 5
p3 = 3
p4 = p2
p5 = 0
p3 = p3 - 1

while p3 > 0:
    while p4 > 0:
        p5 = p5 + p2
        p4 = p4 - 1
    p4 = p5
    p5 = 0
    p3 = p3 - 1

print(p4)

pow1 = '''
Set(r2, 5) # p2 = 5
Set(r3, 3) # p3 = 3
Move(r4, r2) # p4 = p2
Set(r5, 0) # p5 = 0
Subi(r3, r3, 1) # p3 = p3 - 1

#>while p3 > 0:
# goto >endwhile if p3 <= 0
Addi(r10, pc, 11)
Movez(pc, r10, r3)
    #>while p4 > 0:
    # goto >endwhile if p4 <= 0
    Addi(r10, pc, 5)
    Movez(pc, r10, r4)
        Add(r5, r5, r2) # p5 = p5 + p2
        Subi(r4, r4, 1) # p4 = p4 - 1
        Subi(pc, pc, 3)
    #>endwhile
    Move(r4, r5) # p4 = p5
    Set(r5, 0) # p5 = 0
    Subi(r3, r3, 1) # p3 = p3 - 1
    Subi(pc, pc, 10)
#>endwhile

Move(r4, r4)
'''
load(pow1)
printm()
run()
