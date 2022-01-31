def sqrt(x):
 
    if x < 2:        
        return x
 
   
    result = 0
 

    start = 1
    end = x // 2
 
    while start <= end:
 
    
        mid = (start + end) // 2
        sqr = mid*mid
 
        
        if sqr == x:
            return mid
 
       
        elif sqr < x:
            
            start = mid + 1
 
            
            result = mid
 
        
        else:
            
            end = mid - 1
 

    return result

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")