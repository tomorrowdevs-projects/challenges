def is_palindrome_int(int1: int) -> bool:
    int1 = str(int1)
    int2 = int1

    i = 0
    j = len(int2) - 1

    while j >= 0:
        if int1[i] != int2[j]:
            return False
        i = i + 1
        j = j - 1

    return True
