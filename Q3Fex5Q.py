# bcpu FinalQ
# *** Your Name
# *** Your Student ID
# *** Your Tech email addr. 

from bcpu import *

# AQ1
print("AQ1", "=========")
# define an ASM function (subroutine) for multiply two numbers (positive or negative)
mul = """

"""
load(mul, 100)

# define an ASM function for divsion
div = """

"""
load(div, 200)

# create ASM main program for the simple arithmetic:
p = 300//15 + 15*-5
print(p)

# this main program call the div and mul functions to do the caculations. 
main1 = """

"""
load(main1, 1000)
# run(1000)

# AQ2
print("AQ2", "=========")
# create an ASM main program to create an array, size 16
# starting at data storage location 0
# initialize all the 16 location to 8.

array16 = """

"""
load(array16, 2000)
# run(2000) 
# printd()

# AQ3
print("AQ3", "=========")
# create an ASM main program to send the 16 bits of a register (R6) to 16 array locations
# Bit 15 of R6 send to data storage location 0, bit 14 of R6 send to location 1, and so on
# till bit 0 of R6 send to location 15.

# Note that R6 is given below, before the run
send2array = """


"""
load(send2array, 3000)
# test case, other test cases should be tried. 
R[6] = 0b1111001100001111
# run(3000)
print(bin(R[6]))
# printd()


# AQ4
print("AQ4", "=========")
# input/output processing
# assuming data storage location 200 is used for input
# and location 210 is used for output

# create an ASM main program to test input bit and set output bits
# test whether bit 2 of data storage location 200 is 1
# Keep all bits of location 200 unchange
# if yes, set bit 3 and bit 2 of data storage location 210 to both 1
# if no, set bit 3 and bit 2 of data storage location 210 to both 0
# Keep the all other bits in 210 unchange
testset = """

"""
load(testset, 4000)
# test case, other test cases should be tried. 
D[200] = 0b1100
D[210] = 0b110111
# run(4000)
print(bin(D[200]))
print(bin(D[210]))


# AQ5
print("AQ5", "=========")
# create an ASM main program to store
# 100, 111, 110, 101
# to data storage location 100, 101, 102, and 103

done = """

"""
load(done, 5000)
# run(5000)
# printd()
print('done')



