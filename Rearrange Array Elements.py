def rearrange_digits(input_list):
    if input_list is None or len(input_list) == 0:#
        return -1, -1
    
    if len(input_list) == 1 :
        return input_list[0], 0
    
    input_list = merge_sort(input_list)
    input_list.reverse()
    num1 = ""
    num2 = ""
    for i in range(len(input_list)):
        if i %2 ==0:
            num1 +=str(input_list[i])
        if i %2 ==1:
            num2 +=str(input_list[i])
    return int(num1), int(num2)
    


def merge_sort(list):
    
    list_length = len(list)

    
    if list_length <= 1:
        return list

    
    mid_point = list_length // 2

    
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    
    return merge(left_partition, right_partition)

def merge(left, right):
    
    output = []
    i = j = 0

    
    while i < len(left) and j < len(right):
        
        if left[i] > right[j]:
            
            output.append(right[j])
            j+=1
        else:
            output.append(left[i])
            i += 1
    
    output+=left[i:]
    output+=right[j:]

    return output

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([None, [-1, -1]])
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[], [-1, -1]])

test_function([[0, 0], [0, 0]])
test_function([[0, 0, 1, 1, 5, 5], [510, 510]])
test_function([[9,8,7,6,5,4,3,2,1,0,0], [975310, 86420]])


