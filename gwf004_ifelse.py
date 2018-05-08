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

ifthenelse = '''
Set(r0, 0)
Set(r1, 0b11010011)
Set(r2, 0b10001010)
# if-then-else
# goto >endif if not
# r10 is line of endif
Sub(r3, r1, r2)
Addi(r10, pc, 5)
Moven(pc, r10, r4)
    Set(r4, 2)
    Set(r5, 3)
    Addi(pc, pc, 3)
    # >endif
# >else:
    Set(r4, 0)
    Set(r5, 0)
# >endif
'''

load(ifthenelse)
printm()
run()
printr()
