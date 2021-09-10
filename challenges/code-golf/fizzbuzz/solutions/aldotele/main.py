for i in range(1,101):
    c=[i%3==0,i%5==0]
    print("FizzBuzz" if all(c) else "Fizz" if c[0] else "Buzz" if c[1] else i)