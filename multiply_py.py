# r4 = r2 * r3
# where r2, r3 could be negative or positive

# testing
p2 = 2 # counter
p3 = 3

# fix sign
if p2 < 0:
    p2 = -p2
    p3 = -p3

# multipy by adding
p4 = 0
while p2 > 0:
    p4 = p4 + p3
    p2 = p2 - 1

print(p4)
