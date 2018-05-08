from bcpu import *

# if-them-else
# goto > else if not
    # then part
    # ...
    # >endif
# >else:
    # else part
    # ...
# >endif

ifthenelse1 = '''
Set(r1, 0)

# if-then-else
# goto >endif if not
# r10 is line of endif
Addi(r10, pc, 5)
Movex(pc, r10, r1)
    Set(r2, 2)
    Set(r3, 3)
    Addi(pc, pc, 3)
# >else:
    Set(r2, 0)
    Set(r3, 0)
# >endif
'''

load(ifthenelse1)
printm()
