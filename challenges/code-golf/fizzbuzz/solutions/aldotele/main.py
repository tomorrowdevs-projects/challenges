f=lambda x:i%x==0
for i in range(1,101):
 print("FizzBuzz" if f(15) else "Fizz" if f(3) else "Buzz" if f(5) else i)