"""Here's a nice nested loop exercise to start the day:

Please write a program which asks the user to type in an integer number. 
If the user types in a number equal to or below 0, the execution ends. 
Otherwise the program prints out the factorial of the number.

The factorial of a number involves multiplying the number by all the positive integers smaller than itself. 
In other words, it is the product of all positive integers less than or equal to the number. 
For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

Sample output:

Please type in a number: 3
The factorial of the number 3 is 6
Please type in a number: 4
The factorial of the number 4 is 24
Please type in a number: -1"""

def factor(myint: int):
    if myint <= 0:
        print(myint, "is not valid input") 
    else:
        answer = myint
        print("answer", answer)
        for f in range(1, myint + 1):
            print("f", f)
            answer = answer * f
        print("Fatorial of", myint, "=", answer)

factor(5)
