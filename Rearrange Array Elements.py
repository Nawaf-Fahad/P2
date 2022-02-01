def rearrange_digits(input_list):
    if len(input_list) <=1:
        return "there is some issuse with size"
    if input_list is None:
        return "you enter nothing"

    sorted_list = merge_sort(input_list)
    index1 = ''
    index2 = ''
    i=0
    while i < len(input_list):
        if i % 2 == 0:
            index1 += str(sorted_list[i])
        else:
            index2 += str(sorted_list[i])
        i+=1;
    return [int(index1), int(index2)]
    


def merge_sort(list):
    
    list_length = len(list)

    
    if list_length == 1:
        return list

    
    mid_point = list_length // 2

    
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    
    return merge(left_partition, right_partition)

def merge(left, right):
    
    output = []
    i = j = 0

    
    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            
            output.append(left[i])
            
            i += 1
        else:
            output.append(right[j])
            j += 1
    
    output.extend(left[i:])
    output.extend(right[j:])

    return output

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
