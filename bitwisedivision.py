# bonus.py file
# Do NOT change the file name

myName = 'Abercrombie, Addison'
myTechID = '10235455'
myTechEmail = 'aha028@latech.edu'

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

Set(r12,22) #used for while loop, lines to skip too big.
Set(r13,21) #used for while loop, lines to skip too big.

# r6 = abs(r3) #'M'
Movep(r6,r3,r3)
Addi(r11,pc,4)
Movep(pc,r11,r3)
    Not(r6,r3)
    Addi(r6,r6,1)


# r7 = abs(r2) #'Q'
Movep(r7,r2,r2)
Addi(r11,pc,4)
Movep(pc,r11,r2)
    Not(r7,r2)
    Addi(r7,r7,1)

# r5 = 0 #'A'
Set(r5,0)

# #handling zeroes
# if r3 == 0:
Addi(r11,pc,5)
Movex(pc,r11,r3)
#     r8 = 0 #'N'
    Set(r8,0)
#     r4 = r5 = 0
    Set(r4,0)
    Set(pc, 58)
# else:
#     r8 = 16 #number of bits in dividend
     Set(r8,16)


# while r8 != 0:
Add(r11,pc,r12)
Movez(pc,r11,r8)


# #     if r5 < 0:
    Addi(r11,pc,9)
    Moven(pc,r11,r5)
#         Shift AQ (Shift A, If Q is negative > add 1 to A, Shift Q)
        Add(r5,r5,r5)
        Addi(r11,pc,3)
        Movep(pc,r11,r7)
            Addi(r5,r5,1)
        Add(r7,r7,r7)
#         r5 = r5 - r6
        Sub(r5,r5,r6)
        Addi(pc,pc,7)


#     else:
#         Shift AQ
        Add(r5,r5,r5)
        Addi(r11,pc,3)
        Movep(pc,r11,r7)
            Addi(r5,r5,1)
        Add(r7,r7,r7)
#         r5 = r5 + r6
        Add(r5,r5,r6)


#     if r5 < 0:
        Addi(r11,pc,3)
        Moven(pc,r11,r5)
#         r7 += 1
            Addi(r7,r7,1)
#     r8 -= 1
        Subi(r8,r8,1)
        Sub(pc,pc,r13)
        


# if r5 < 0:
Addi(r11,pc,3)
Movep(pc,r11,r5)
#     r5 += r6
    Add(r5,r5,r6)

Move(r4,r7)

#make sure r4 and r5 are set


# #handling negatives
# if r2 < 0:
Addi(r11,pc,9)
Movep(pc,r11,r2)
#     r5 = -r5
    Not(r5,r5)
    Addi(r5,r5,1)
#     if r3 > 0:
    Addi(r11,pc,4)
    Moven(pc,r11,r3)
#         r4 = -r4
        Not(r4,r4)
        Addi(r4,r4,1)
    Addi(pc,pc,7)
# else:
#     if r2 > 0:
Addi(r11,pc,6)
Moven(pc,r11,r2)
#         if r3 < 0:
    Addi(r11,pc,4)
    Movep(pc,r11,r3)
#             r4 = -r4
        Not(r4,r4)
        Addi(r4,r4,1)



Move(r4,r4)
Move(r5,r5)

"""
