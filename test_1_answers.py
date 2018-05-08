from bcpu import *

AQ1 = """
Set(r0, 0)
Set(r3, 44)
Seth(r3, 1)
Sub(r3, r0, r3)
Set(r4, 42)
Set(r6, 244)
Seth(r6, 1)
Sub(r5, r4, r3)
Add(r5, r5, r6)
Move(r5, r5)

"""
load(AQ1, 100)
run(100)


AQ2 = """
Set(r2, 3)
Set(r3, 5)
Set(r4, 0)

Sub(r5, r3, r2)
Addi(r10, pc, 3)
Moven(pc, r10, r5)
    Set(r4, 10)
Move(r4, r4)

"""
load(AQ2, 200)
run(200)

AQ3 = """
Set(r2, 0)
Set(r3, 0)

Addi(r10, pc, 6)
Subi(r5, r2, 11)

Movez(pc, r10, r5)
    Add(r3, r3, r2)
    Addi(r2, r2, 1)
    Subi(pc, pc, 4)
Move(r3, r3)

"""

load(AQ3, 300)
run(300)

AQ4 = """
Set(r2, 9)
Set(r3, 3)
Set(r4, 0)

Addi(r10, pc, 6)

Sub(r8, r2, r3)
Moven(pc, r10, r8)
    Sub(r2, r2, r3)
    Addi(r4, r4, 1)
    Subi(pc, pc, 4)
Move(r5, r2)
Move(r4, r4)
Move(r5, r5)


"""

load(AQ4, 400)
run(400)

AQ5 = """
Set(r0, 0)

Set(r2, 2)
Sub(r2,r0,r2) #-r2
Set(r3, 3)
Sub(r3, r0, r3) #-r3
Set(r4, 0)

# if r3 < 0: r3 = -r3; r2 = -r2

Addi(r11, pc, 4)
Movep(pc, r11, r3) #if r3 >= 0 goto endif
    Sub(r3, r0, r3)
    Sub(r2, r0, r2)

Addi(r10, pc, 5)
Movez(pc, r10, r3)
    Add(r4, r4, r2)
    Subi(r3, r3, 1)
    Subi(pc, pc, 3)
Move(r4, r4)

"""

load(AQ5, 500)
run(500)
