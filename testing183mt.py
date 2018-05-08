# MT All Test Grading
from bcpu import *

from mt183all5asm import *

testall = []

# testing Q1
try: 
    load(mtQ1)
    # r6 = r5 - 7 * r3 + 800
    tg = 0
    Set(r5, 5)
    p5 = 5
    Set(r3, 3)
    p3 = 3
    runfast()
    tg = 5+tg if geti(R[6]) == (p5 - 7 * p3 + 800) else tg
    Set(r0, 0)
    Set(r5, 50)
    Sub(r5, r0, r5)
    p5 = -50
    Set(r3, 30)
    p3 = 30
    runfast()
    tg = 5+tg if geti(R[6]) == (p5 - 7 * p3 + 800) else tg
    testall += [tg]
except:
    testall += [0]

# testing Q2
try: 
    load(mtQ2)
    # r6 = rotate_right(r2)

    tg = 0

    R[2] = 0b0011_0000_1111_0011
    runfast()
    tg = 5+tg if R[6] == 0b1001_1000_0111_1001 else tg

    R[2] = 0b1111_0000_1111_0000
    runfast()
    tg = 5+tg if R[6] == 0b0111_1000_0111_1000 else tg

    testall += [tg]
except:
    testall += [0]

# testing Q3
try: 
    load(mtQ3)
    # r4 = abs(r2) // abs(r3)
    # r5 = abs(r2) % abs(r3)
    # r2, r3 are integer inputs that can be positve, nagative, or zero. 
    # r4, r5 are outputs where the returned r4 and r5 need to meet the following:
    # if r3 == 0: r4 = r5 = 0
    # NEED to fix sign of r4 and r5 as below:
    # r5 has the same sign as r2
    # r4 is positive when r2 and r3 have the same signs, otherwise negative. 

    tg = 0

    Set(r0, 0)
    Set(r2, 17)
    Sub(r2, r0, r2)
    Set(r3, 0)
    runfast()
    tg = 2+tg if (R[4] == 0) and (R[5] == 0) else tg

    Set(r0, 0)
    Set(r2, 17)
    Sub(r2, r0, r2)
    Set(r3, 3)
    Sub(r3, r0, r3)
    runfast()
    tg = 3+tg if (R[4] == 5) and (geti(R[5]) == -2) else tg

    Set(r2, 5) 
    Set(r0, 0)
    Set(r3, 3)
    Sub(r3, r0, r3)
    runfast()
    tg = 5+tg if (geti(R[4]) == -1) and (R[5] == 2) else tg

    testall += [tg]
except:
    testall += [0]


# testing Q4
try: 
    load(mtQ4)

    tg = 0

    p2 = 2
    p3 = 3

    p6 = 6
    p7 = 7
    if (p2 >= 0) and (p3 > p2):
        p6 = p2
        p7 = -(p2 + p3)

    Set(r2, 2)
    Set(r3, 3)
    runfast()
    tg = 5+tg if (geti(R[6]) == p6) and (geti(R[7]) == p7) else tg

    p2 = 3
    p3 = 2

    p6 = 6
    p7 = 7
    if (p2 >= 0) and (p3 > p2):
        p6 = p2
        p7 = -(p2 + p3)

    Set(r2, 3)
    Set(r3, 2)
    runfast()
    tg = 5+tg if (geti(R[6]) == p6) and (geti(R[7]) == p7) else tg

    testall += [tg]
except:
    testall += [0]

# testing Q5
try: 
    load(mtQ5)

    tg = 0

    p2 = 2
    p3 = 3

    p6 = 6
    p7 = 7
    if (p2 >= 0) or (p3 > p2):
        p6 = p2
        p7 = -(p2 + p3)

    Set(r2, 2)
    Set(r3, 3)
    runfast()
    tg = 5+tg if (geti(R[6]) == p6) and (geti(R[7]) == p7) else tg

    p2 = -2
    p3 = -3

    p6 = 6
    p7 = 7
    if (p2 >= 0) or (p3 > p2):
        p6 = p2
        p7 = -(p2 + p3)

    Set(r0, 0)
    Set(r2, 2)
    Set(r3, 3)
    Sub(r2, r0, r2)
    Sub(r3, r0, r3)
    runfast()
    tg = 5+tg if (geti(R[6]) == p6) and (geti(R[7]) == p7) else tg

    testall += [tg]
except:
    testall += [0]


# done all test
print("===================")
print(myName, myTechID, myTechEmail)
print("total:", sum(testall))
i = 1
for g in testall:
    print(f"Q{i} = {g}")
    i += 1
