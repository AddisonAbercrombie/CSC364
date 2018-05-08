# bcpu mtQ

from bcpu import *

# AQ1
print("AQ1", "=========")
# create ASM code for the simple arithmetic:
p3 = -300
p4 = 42
p5 = p4 - p3 + 500
print(p5)


# AQ2
print("AQ2", "=========")
# creat ASM code for the following py code

x = 3  # test case
y = 5  # test case
# other test cases should be used

z = 0
if x <= y:
    z = 10
print(z)


# AQ3
print("AQ3", "=========")
# create ASM code for to implement the following py code

sumx = 0
for x in range(11):
    sumx = sumx + x
print(sumx)

# AQ4
print("AQ4", "=========")
# write an ASM program for division
# test cases
n = 9
d = 4
# other test cases should be used

q = n//d # interger division (q is the integer part)
r = n%d # interger division (r is the remainder part)
# where n and d are positive intergers
# if d == 0: q = 0; r = 0
print(q)
print(r)

# AQ5
print("AQ5", "=========")
# write an ASM program for multiplication
# test cases
n = 9
c = -4
# other test case should for used.

p = n*c
# where n and d are intergers that can be positive or negative
# Your program should be able to handle the positive (including 0)
# and negative numbers
print(p)



