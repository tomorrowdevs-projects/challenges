"""
Divisors of a number
Count the number of divisors of a positive integer `n`.

divisors(4)  // => 3 (1, 2, 4)
divisors(5)  // => 2 (1, 5)
divisors(12) // => 6 (1, 2, 3, 4, 6, 12)
divisors(30) // => 8 (1, 2, 3, 5, 6, 10, 15, 30)
"""
def divisors(n):
    # create a list with all the numbers from 1 to n
    num = list(range(1, n + 1))
    div = []
    # for each number, if n % num == 0: append to the divisors list div
    # else delete the number from the num list
    while len(num) > 0:
        if n % num[-1] == 0:
            div.append(num[-1])
        num.pop()
    #print(div)
    return len(div)

print(divisors(30))
