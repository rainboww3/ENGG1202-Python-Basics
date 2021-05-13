#task 1
from rsa import *
value = 100
n = 30360138080141                                                                  
e = 5510009                                                                         
code = rsaencrypt( value, n, e )
print( value, "=>", code )

#task 2
from rsa import *
code = 15251238784560
n = 30360138080141                                                                  
d = 24201026397005
value = rsadecrypt( code, n, d )
print( code, "=>", value )

#task 3
from rsa import *
n = 493                                                                  
e = 11
d = rsahack( n, e )
print( n, ",", e, "=>", d )
