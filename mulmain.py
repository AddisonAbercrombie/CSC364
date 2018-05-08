# mul main prog
from bcpu import *

# include
from mulfnlib import *

mainfn = """
#>main()

Set(r2, 2)
Set(r3, 3)

#call mul(r2, r3) -> r4
# push return addr
Addi(r13, pc, ?returnaddr)
Addi(st, st, 1)
Store(st, r13)
# call mul
Set(r13, ?mul % 256)
Seth(r13, ?mul // 256)
Move(pc, r13)
#>returnaddr

Move(r4, r4)
"""
load(mainfn)
run()
printi(R[r4])
