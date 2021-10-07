def find_missing_number(l):
    # total list = sum all the numbers between the min and the max of the list
    # difference between the total list and the list will be the missing number
    n = sum(range(min(l), max(l) + 1)) - sum(l)
    return n


if __name__ == '__main__':
    mylist = [230, 222, 220, 224, 229, 221, 225, 223, 228, 226]
    print(find_missing_number(mylist))