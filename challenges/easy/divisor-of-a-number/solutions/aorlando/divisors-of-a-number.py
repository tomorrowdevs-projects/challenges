def divisors_of_number(number):
    divisor = 0
    mytuple = tuple()
    for n in range(1, number+1):
        if number % n == 0:
            divisor += 1
            mytuple += (n,)
    return f"{number} have {divisor} divisors => {mytuple}"


test1 = divisors_of_number(36)
test2 = divisors_of_number(47)
test3 = divisors_of_number(3)
test4 = divisors_of_number(1)
test5 = divisors_of_number(276)

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
