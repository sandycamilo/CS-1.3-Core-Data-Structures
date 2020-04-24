# f(n) = f(n-1) + f(n-2)
# n is the nth fib number in the fib sequence
# 0, 1 

def fib(n):
    # base case
    if n <= 1:
        return n 
    else: # recursive case
        return fib(n-1) + fib(n-2)

print(fib(13))