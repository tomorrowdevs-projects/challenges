import itertools

# this function verify if a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# this function creates the pairs of prime numbers
def prime_pairs(x, y):
    prime_numbers = []
    # for each number in the given range I check if it is prime and append them to the prime_number list
    for i in range(x, y):
        if is_prime(i):
            prime_numbers.append(i)
    # create a list with all the possible combinations of prime numbers without duplicates
    prime_pairs = list(itertools.combinations_with_replacement(prime_numbers, 2))
    return prime_pairs

# this is the core function that calculate the reversion
def prime_reversion(x, y):
    result = []
    # take all the possible unique pairs with the given numbers
    pairs = prime_pairs(x, y)
    # multiply the numbers in the list and check how many digits the number have, to sum every digit
    # ex (7,7) will give 49 as a result so that I can sum 4+9
    # (3,3) = since 3*3 = 9 this will not be considered because I cannot sum a single digit
    pairs_product = [a * b for a, b in pairs if len(str(a*b)) > 1]

    # for each product in the list I take each number and sum to each other
    # ex 49 will be 4 + 9
    for n in pairs_product:
        sum = 0
        for i in range(len(str(n))):
            # since n is int I need to make it a string so that I can extract the single digit
            # then I make it an int again to sum it
            sum += int(str(n)[i])
        # if the sum of the numbers is a prime number I can add it to the result list
        if is_prime(sum):
            result.append(sum)
    # return the number of elements in the result list of prime numbers
    return len(result)


def main():
   while True:
    try:
        num1 = int(input("Enter the first number of the range: "))
        num2 = int(input("Enter the second number of the range: "))
        print(prime_reversion(num1, num2))
        break
    except ValueError:
        print("You didn't enter correct numbers, try again.")


if __name__ == '__main__':
    main()
