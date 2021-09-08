# PRIME REVERSION CHALLENGE

def range_to_list(lower, upper):
    """
    :param lower: integer
    :param upper: integer 
    :return: a list of integers
    """
    if lower >= 0 and upper <= 10001:
        return list(range(lower, upper))
    else:
        raise ValueError("upper bound cannot exceed 10000")


def find_primes(numbers):
    """
    :param numbers: list of integers
    :return: a list of prime integers
    """
    primes = []
    for num in numbers:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


def find_couples(primes):
    """
    :param primes: list of prime integers
    :return: a list of tuples with two integers each
    """
    couples = []
    i = 0
    for i in range(len(primes)):
        couple = (primes[i], primes[i])
        couples.append(couple)
        for j in range(i+1, len(primes)):
            couple = (primes[i], primes[j])
            couples.append(couple)
    return couples


def count_reversions(couples):
    """
    :param couples: list of tuples with two integers each
    :return: an integer
    """
    inner_sums = []
    for couple in couples:
        product = couple[0] * couple[1]
        product_as_str = str(product)
        # using map to convert each element of the product to an integer
        inner_sum = sum(list(map(int,product_as_str)))
        inner_sums.append(inner_sum)
    # after calculating the sums, I invoke the function to filter prime numbers
    primes_among_sums = find_primes(inner_sums)
    return len(primes_among_sums)


def solve(numbers):
    """
    :param lower: integer
    :param upper: integer
    :return: integer
    """
    primes = find_primes(numbers)
    couples = find_couples(primes)
    prime_reversions = count_reversions(couples)
    return prime_reversions


if __name__ == '__main__':
    x = 1
    y = 100
    numbers = range_to_list(x, y)
    solution = solve(numbers)
    print(solution)
