# check if a number is a prime number
def isPrime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False

    return True


# check if a pair can be reverted in a prime number
def revert2prime(m, n: tuple) -> bool:
    molt = m * n
    result = 0

    # sum each digit in the number casting the number like a string
    for i in str(molt):
        result += int(i)

    return isPrime(result)


def primeReversion(x, y: tuple) -> int:
    # create a list of prime numbers in a range (x,y)
    primeList = []
    for i in range(x, y):
        if isPrime(i):
            primeList.append(i)

    # count how many combinations are prime reversions
    count = 0
    for index, first in enumerate(primeList):
        for sub_index, second in enumerate(primeList[index:]):
            if revert2prime(first, second):
                count += 1

    return count


print(primeReversion(0, 20))
print(primeReversion(2, 200))
print(primeReversion(2, 300))
print(primeReversion(100, 200))
