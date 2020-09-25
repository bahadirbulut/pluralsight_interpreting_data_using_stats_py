from itertools import combinations 

# Factorial of a number using recursion
def factorial(n):
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)

def combination(x, y):
    x = float(x)
    y = float(y)
    try:
        comb = factorial(x) / (factorial(x-y) * factorial(y))
        return comb
    except Exception:
        print(Exception)
        print("Please make sure that first number is bigger than the second number")
        print("Plus you cannot use negative numbers")


def permutation(x, y):
    x = float(x)
    y = float(y)
    try:
        perm = factorial(x) / factorial(x-y)
        return perm
    except:
        print("Please make sure that first number is bigger than the second number")
        print("Plus you cannot use negative numbers")


x = input("Please enter a positive number for x: ")
y = input("Please enter a positive number for y (y <= x): ")
print(f"Combination({x},{y}): {combination(x, y)}")
print(f"Permutation({x},{y}): {permutation(x, y)}")
