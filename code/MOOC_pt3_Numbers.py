'''Please write a program which asks the user for a number. 
The program then prints out all integer numbers greater than zero but smaller than the input.'''

def numbers(myint):
    for i in range(myint):
        print(i)

myint = int(input("Please enter an integer: "))

numbers(myint)
