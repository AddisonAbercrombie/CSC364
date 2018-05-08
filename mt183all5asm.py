# mt183all5asm.py file
from bcpu import *

myName = 'Freeman, Grant'
myTechID = '10233162'
myTechEmail = 'gwf004@latech.edu'

mtQ1 = """
# r6 = r5 - 7 * r3 + 800
# r5, r3 are integer inputs that will be passed to this routine
# r6 is the output to be returned
Set(r7, 7)
Set(r1, 1)
Set(r4, 0)
#>while p1 < 0b1000000000000000:
# goto >endwhile if p1 == 0
Addi(r10, pc, ?endwhile)
Movez(pc, r10, r1)
    And(r9, r1, r3)
    Set(r0, 0)
    Movex(r0, r7, r9)
    Add(r4, r4, r0)
    Add(r1, r1, r1)
    Add(r7, r7, r7)
    Subi(pc, pc, ?while)
#>endwhile
Sub(r9, r5, r4)
Set(r11, 0b00100000)
Or(r9, r9, r11)
Seth(r9, 0b11)
Move(r9, r9)


"""

mtQ2 = """
# r6 = rotate_right(r2)
# r2 is an integer input
# r6 is the output that is bitwise rotate right once of r2
# HINT: rotate left 15 times results in rotate right once
Set(r14, 15) # p15 = 15

#>while p15 > 0:
# goto >endwhile if p15 <= 0
Addi(r10, pc, ?endwhile)
Movez(pc, r10, r14)
    Set(r1, 1)
    Moven(r0, r1, r2)
    Add(r2, r2, r2)
    Or(r2, r2, r0)
    Set(r0, 0)
    Subi(r14, r14, 1)
    Subi(pc, pc, ?while)
#>endwhile
"""

mtQ3 = """
# r4 = abs(r2) // abs(r3)
# r5 = abs(r2) % abs(r3)
# r2, r3 are integer inputs that can be positive, negative, or zero. 
# r4, r5 are outputs where the returned r4 and r5 need to meet the following:
# if r3 == 0: r4 = r5 = 0
# NEED to fix sign of r4 and r5 as below:
# r5 has the same sign as r2
# r4 is positive when r2 and r3 have the same signs, otherwise negative. 

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

"""

mtQ4 = """
# r2, r3 are inputs
# r6, r7 are outputs

# p6 = 6
# p7 = 7
# if (p2 >= 0) and (p3 > p2):
#    p6 = p2
#    p7 = -(p2 + p3)

# translate the above code to ASM keeping the structure (only one thenpart)
Addi(r10, pc, ?endif) # if (p2 >= 0)
Moven(pc, r10, r2)
# goto >endif if p2 <= p3
Sub(r9, r2, r3)
Addi(r10, pc, ?endif)
Movep(pc, r10, r9)
    Move(r6, r2) #    p6 = p2
    Add(r11, r2, r3)
    Set(r0, 0)
    Sub(r7, r0, r11) #    p7 = -(p2 + p3)
#>endif
Move(r6, r6)
Move(r7, r7)

"""

mtQ5 = """
# r2, r3 are inputs
# r6, r7 are outputs

# p6 = 6
# p7 = 7
# if (p2 >= 0) or (p3 > p2):
#    p6 = p2
#    p7 = -(p2 + p3)

# translate the above code to ASM keeping the structure (only one thenpart)
Addi(r10, pc, ?endif) # if (p2 >= 0)
Moven(pc, r10, r2)
# goto >endif if p2 <= p3
Sub(r9, r2, r3)
Addi(r10, pc, ?endif)
Movep(pc, r10, r9)
    Move(r6, r2) #    p6 = p2
    Add(r11, r2, r3)
    Set(r0, 0)
    Sub(r7, r0, r11) #    p7 = -(p2 + p3)
#>endif
Move(r6, r6)
Move(r7, r7)

"""
