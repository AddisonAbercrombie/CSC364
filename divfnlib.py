from bcpu import *

Addr.divfn = 300

divfn = """
#>div(r2, r3) -> (r4, r5):
# r4 = r2 // r3
# r5 = r2 % r3
# +, -, or 0
# use r0, 1, r0...13

Set(r4, 0)
Set(r5, 0)

# if r3 == 0: # divide by 0
# goto >end
Set(r10, ?end -1)
Add(r10, pc, r10)
Movez(pc, r10, r3)
# if r2 == 0: goto >end
Movez(pc, r10, r2)

Set(r0, 0)
Move(r12, r2) # save for fix sign
Move(r13, r3)

# abs
Addi(r10, pc, ?endif2)
Movep(pc, r10, r2)
    Sub(r2, r0, r2)
#>endif2
Addi(r10, pc, ?endif3)
Movep(pc, r10, r3)
    Sub(r3, r0, r3)
#>endif3

# bitwise div
Set(r9, 15) # i 15...0
# skip leading 0
Addi(r10, pc, ?dorest)
#>skip
Moven(pc, r10, r2)
    Add(r2, r2, r2)
    Subi(r9, r9, 1)
    Subi(pc, pc, ?skip)
#>dorest

Addi(r8, pc, ?endmovebit)
Addi(r11, pc, ?endif4)
Addi(r10, pc, ?endwhile)

#>while r9 >= 0:
# goto >endwhile if r9 < 0
Moven(pc, r10, r9)
    Add(r4, r4, r4) # << 1
    Add(r5, r5, r5) # << 1
    # move bits from r2 to r5
    Movep(pc, r8, r2)
    Addi(r5, r5, 1)
    #>endmovebit
    # if r5 >= r3:
    # goto >endif4 if r5 < r3
    Sub(r1, r5, r3)
    Moven(pc, r11, r1)
        Sub(r5, r5, r3)
        Addi(r4, r4, 1)
    #>endif4
    # next i
    Subi(r9, r9, 1)
    Add(r2, r2, r2) # check next bit
    # goto >while
    Subi(pc, pc, ?while)
#>endwhile

# fix sign
Addi(r10, pc, ?endif5)
Movep(pc, r10, r12)
    Sub(r5, r0, r5)
    Sub(r4, r0, r4)
#>endif5
Addi(r10, pc, ?endif6)
Movep(pc, r10, r13)
    Sub(r4, r0, r4)
#>endif6

#>end
# return
Load(r13, st)
Subi(st, st, 1)
Move(pc, r13)

#>enddiv
"""

load(divfn, Addr.divfn)
run()
