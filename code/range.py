"""Test using range() for loops"""

# when you use range for a loop as below,
# it will start with 0 and end just before myint
# Example:
#   basic(2) will print 0 1
#   starts at 0 but does not include 2

#   better(2) will print 1 2 
#   range(1, myint + 1) tells it to start at 1 and adds one to myint so it will include 2
#   for i in range(3, myint + 3): would print 3 4 as it would start at 3 and end before 5

#   amazing(2,4) will print 4 5
#       the myint is 2 and is how many iterations the loop will do
#       the start is 4 and tells it to start the range at 4 and stop before 6

def basic(myint):
    for i in range(myint):
        print(i)

def better(myint):
    for i in range(1, myint + 1):
        print(i)

def amazing(myint, start):
    for i in range(start, myint + start):
        print(i)

#basic(2)
#better(2)        
amazing(2, 4)
