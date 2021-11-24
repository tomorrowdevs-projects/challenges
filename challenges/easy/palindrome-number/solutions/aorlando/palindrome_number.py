# "Is a plindrome number" challenge TD

def isPalindrome(number):
    if number < 0:
        return False
    elif number < 10:
        return True
    
    to_string = str(number)
    tail = -1
    for val in range(len(to_string)):
        if to_string[val] == to_string[tail]:
            tail -= 1
            continue
        else:
            return False

    return True


def main():
    test1 = isPalindrome(121)
    test2 = isPalindrome(-121)
    test3 = isPalindrome(10)
    test4 = isPalindrome(-100533894103)
    test5 = isPalindrome(1234321)
    
    print(test1)
    print(test2)
    print(test3)
    print(test4)
    print(test5)
    

if __name__ == "__main__":
    main()
 