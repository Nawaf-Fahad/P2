


def rotated_array_search(input_list, number):
    if len(input_list) ==0:

        return "there is some issuse";
    mid = len(input_list)//2

    if input_list[mid] < input_list[mid-1]:
        mid -= 1

    first_half= bs(input_list[mid + 1:], number)
    last_half = bs(input_list[:mid + 1], number)

    if first_half != -1:
        first_half += mid + 1
        return first_half

    if last_half != -1:
        return last_half

    return -1
    
def bs(list, num):
    first = 0
    last = len(list)-1

    while first <= last:

        mid = int((last + first)/2)
        if list[mid] == num:
            return mid
        elif list[mid] > num:
            last = mid - 1

        elif list[mid] < num:
            first = mid+1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4,8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])