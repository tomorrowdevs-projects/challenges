"""
Python solution for challenge: "Prime reversion"
To test the function type from CLI: python tests.py
"""

from itertools import combinations_with_replacement


def solve(n1, n2):
    # Create a dictionary of prime numbers into the range n1-n2 (excluded)
    prime_numbers = generate_prime_numbers_in_range(n1, n2)
    # Create the pairs with the prime numbers (dictionary keys) previously generated
    pairs = list(combinations_with_replacement(prime_numbers, 2))
    # Analysis of each single couple
    for pair in pairs:
        # Call to the function product_and_sum_digit_number
        sum_product_number = product_and_sum_digit_number(pair)
        # Check if sum_product_number is a prime number or not
        if sum_product_number in prime_numbers:
            # Incrementation of the occurrences of the prime number already present in the dictionary
            prime_numbers[sum_product_number] += 1
        elif is_prime(sum_product_number):
            # Insertion of the new prime number in the dictionary
            prime_numbers[sum_product_number] = 1
    # Return the sum of the occurrences of prime numbers present in the dictionary
    return sum(prime_numbers.values())


def generate_prime_numbers_in_range(n1, n2):
    """ This function generates a dictionary with the list of prime numbers,
    between an initial value n1 and a final value n2 (excluded)
    """
    prime_numbers = {}
    for number in range(n1, n2):
        # Call to the function that checks whether a number is prime or not
        if is_prime(number):
            prime_numbers[number] = 0
    return prime_numbers


def is_prime(number):
    """ This function check if number is a prime number or not """
    # Check if the number is equal to 2 or 3 and return True. For number <= 1 return False.
    if number <= 3:
        return number > 1
    # Check if the number is divisible for to 2 or 3
    if number % 2 == 0 or number % 3 == 0:
        return False
    # Next divisor is equal 5, because 4 is multiple of 2
    divisor = 5
    while True:
        if divisor ** 2 > number:
            break
        elif number % divisor == 0 or number % (divisor + 2) == 0:
            return False
        # Increment of the divisor, according to the algorithm 6k + 1
        divisor += 6
    return True


def product_and_sum_digit_number(pair):
    # Product between the two numbers that make up the pair
    product = pair[0] * pair[1]
    sum_product = 0
    # Sum of the digits that make up product, starting from the least significant to the most significant
    while True:
        # There are no other digits to sum (end of cycle)
        if not product:
            break
        # Increment of the sum_product with the value of the last digit of the number
        sum_product += product % 10
        # Removing last digit from the number
        product //= 10
    # Return the sum of the digits that compose product
    return sum_product

