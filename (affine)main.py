#task 1
from affine import *
text="Attack!"
a = 9
b = 13
cipher = afencode( text, a, b)
print( text, "=>", cipher )

#task 2
from affine import *
cipher = "Nccnfz!"
a = 9
b = 13
text = afdecode( cipher, a, b )
print( cipher, "=>", text )
