#Write a Python program to get the Fibonacci series between 0 to 50

def fibonacci(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return(fibonacci(number - 2) + fibonacci(number -1))
for value in range(1,10):
   print(fibonacci(value))
