#task 1
def afencode(text, a, b):
    
    list(text)
    result=""
    for ch in text:
        
        if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            result += chr(((a*(ord(ch)-65)+b)%26)+65)
            
        elif ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            result += chr(((a*(ord(ch)-97)+b)%26)+97)
            
        else:
            result += ch
            
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
    
#task 2    
def afdecode(cipher, a, b):
    
    list(cipher)
    result=""
    n = 26
    ainv = mInverse( a, n )       
    for ch in cipher:
        
        if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            result += chr(((ainv*((ord(ch)-65)-b))%26)+65)
            
        elif ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            result += chr(((ainv*((ord(ch)-97)-b))%26)+97)
            
        else:
            result += ch
            
    return result
            
            
            
