# Recursion is the programming technique that a function calls itself to solve a problem
# Finding factorial of number and fibonacci are the problems coming under recursion

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
       return fib(n-1) + fib(n-2)

print(fib(6))
