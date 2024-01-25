"""Here's a nice nested loop exercise to start the day:

Cleaned up version of loop_exercise without all the print stament to check progress"""

def factorial(n):
    if n <= 0:
        print(n, "is not valid input") 
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

ans = factorial(5)
print(ans)
