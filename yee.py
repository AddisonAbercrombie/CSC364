# bonus.py file
# Do NOT change the file name


divBQ = """
# r4 = abs(r2) // abs(r3)
# r5 = abs(r2) % abs(r3)
# r2, r3 are integer inputs that can be positive, negative, or zero. 
# r4, r5 are outputs where the returned r4 and r5 need to meet the following:
# if r3 == 0: r4 = r5 = 0
# NEED to fix sign of r4 and r5 as below:
# r5 has the same sign as r2
# r4 is positive when r2 and r3 have the same signs, otherwise negative. 

# *** Must use less than 600 steps in the worst-case

Set(r12, 104)
Movep(pc, r12, r2)
Addi(r7, r7, 1)
Sub(r2, r0, r2)
Set(r12, 108)
Movep(pc, r12, r3)
Addi(r7, r7, 1)
Sub(r3, r0, r3)
Seth(r10, 32768//256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Seth(r10, 16384//256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Seth(r10, 8192//256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D 0
Or(r4, r4, r10)   # Q(i) := 1
Seth(r10, 4096//256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Seth(r10, 2048//256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Seth(r10, 1024//256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Seth(r10, 512//256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Seth(r10, 256//256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Seth(r10, 128//256)                 # clear high register
Set(r10, 128%256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Set(r10, 64%256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Set(r10, 32%256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Set(r10, 16%256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Set(r10, 8%256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Set(r10, 4%256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Set(r10, 2%256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Set(r10, 1%256)
Add(r5, r5, r5)      # R := R << 1
And(r6, r10, r2)       # R(0) := n(i)
Addi(r9, pc, 3)
Movez(pc, r9, r6)           # if t != 0:
Addi(r5, r5, 1)
Sub(r8, r5, r3)
Addi(r9, pc, 4)
Moven(pc, r9, r8)       #if R >= d:
Sub(r5, r5, r3)   # R := R − D
Or(r4, r4, r10)   # Q(i) := 1
Subi(r7, r7, 1)
Addi(r11, pc, 4)
Movex(pc, r11, r7)
Sub(r4, r0, r4)
Sub(r5, r0, r5)
Addi(r11, pc, 4)
Movex(pc, r11, r3)
Set(r4, 0)
Set(r5, 0)

"""
