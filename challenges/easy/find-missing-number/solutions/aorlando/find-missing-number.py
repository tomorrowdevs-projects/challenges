def findMissingNumber(list_of_numbers):
    
    ordered_list = sorted(list_of_numbers)
    first_elem = ordered_list[0]
    last_elem = ordered_list[-1]
    
    # Use the Gauss trick to compute the sum of the first and last element whitout iterating the list
    # https://it.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%C2%B7_%C2%B7_%C2%B7
    gauss_first_elem = (first_elem * (first_elem + 1)) / 2
    gauss_last_elem = (last_elem * (last_elem + 1)) / 2

    # The actual sum of the elements passed from list that contains the missing number
    sum_of_actual_elem = sum(ordered_list)

    result = int(((gauss_last_elem - sum_of_actual_elem) - gauss_first_elem) + first_elem)

    return result


test1 = findMissingNumber([2, 1, 4, 6, 5])
test2 = findMissingNumber([200, 203, 201, 204, 199])
test3 = findMissingNumber([187, 185, 188, 184, 183])
test4 = findMissingNumber([7, 8, 10, 12, 11])
test5 = findMissingNumber([1000, 999, 1002, 1003])

print(f"Missing number test1: {test1}")
print(f"Missing number test1: {test2}")
print(f"Missing number test1: {test3}")
print(f"Missing number test1: {test4}")
print(f"Missing number test1: {test5}")