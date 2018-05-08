from bcpu import *

# if-then
# goto >endif if not
    # thenpart
    # ...
# >endif

ifthen1 = """
Set(r2, 0)
Set(r3, 0)
Set(r1, 1)
Addi(r10, pc, 4)
Movex(pc, r10, r1)
    Set(r2, 2)
    Set(r3, r3)
# >endif
"""

load(ifthen1)
printm()

run()
printr()
