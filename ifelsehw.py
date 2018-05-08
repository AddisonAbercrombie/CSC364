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

Set(r0, 0)
Set(r1, 1)
Set(r2, 0b11010011)
Set(r3, 0b10001010)

ifthenelse = '''
# if-then-else
# goto >endif if not
# r10 is line of endif
Sub(r4, r2, r3)
Addi(r10, pc, 5)
Moven(pc, r10, r4)
    Set(r2, 2)
    Set(r3, 3)
    Addi(pc, pc, 3)
# >else:
    Set(r2, 0)
    Set(r3, 0)
# >endif
'''

load(ifthenelse)
printm()
run()
printr()
