def find_missing_number(l):
    # sort the list to get the min and the max taking the first and the last item
    l.sort()
    # total list = sum all the numbers between the min and the max of the list
    # difference between the total list and the list will be the missing number
    n = sum(range(l[0], l[len(l)-1] + 1)) - sum(l)
    return n


if __name__ == '__main__':
    mylist = [230, 222, 220, 224, 229, 221, 225, 223, 228, 226]
    print(find_missing_number(mylist))