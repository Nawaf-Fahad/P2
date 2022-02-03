def get_min_max(ints):
    if ints is None or len(ints)==0:
        return None

    if len(ints)==1:
        return (ints[0],ints[0])
    min = ints[0]
    max=ints[0]

    for i in ints:
        if ints[i]>max:
            max=ints[i]
        if ints[i]<min:
            min=ints[i]

    return min,max



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 0)] 
random.shuffle(l)
print ("Pass" if (None == get_min_max(l)) else "Fail")

l = [i for i in range(0, 100000)]  # a list containing 0 - 99999
random.shuffle(l)

print ("Pass" if ((0, 99999) == get_min_max(l)) else "Fail")