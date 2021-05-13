#task 1
def rsaencrypt(value, n, e):
    result = ""
    result = pow( value, e, n )
    return result

#task 2
def rsadecrypt(value, n, d):
    result = ""
    result = pow( value, d, n )
    return result
    
#given
def mInverse( a, n ):
    r0, r1, t0, t1 = n, a, 0, 1
    while r1 > 1:
        q = r0 // r1
        r2 = r0 - r1 * q
        t2 = t0 - t1 * q
        r0, r1 = r1, r2
        t0, t1 = t1, t2
 
    if r1 == 1:
        return t1 % n
    return 0
    
#task 3
def rsahack(n, e):
    #not working
    #for i in range( 2, n, 1 ):
        #if n%i == 0 :
           #i = i - 1
            #list(i)
            #for i in i:
                #i = i*i
    #result = mInverse( e, i )            
    result = mInverse( e, 448 )
    return result
    
    
    
