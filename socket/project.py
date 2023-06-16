msg = 'rGMTLIVrHIQSGIEWIVGIEWIV' #encrypted msg  
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  
      
for k in range(len(LETTERS)):  
    transformation = ''  
    for s in msg:  
        if s in LETTERS:  
            n = LETTERS.find(s)  
            n = n - k  
            if n < 0:  
                n = n + len(LETTERS)  
                transformation = transformation + LETTERS[n]  
      
            else:  
                transformation = transformation + s  
    print('Hacking k #%s: %s' % (k, transformation))  