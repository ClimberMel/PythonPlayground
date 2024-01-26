'''Please write a new version of the program in the previous exercise. 
In addition to the result it should also print out the calculation performed:

Sample output:
Limit: 2
The consecutive sum: 1 + 2 = 3

Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21
'''

limit = int(input("Please enter a limit: "))
current_sum = 1     # initialize sum
current_number = 1  # set starting number
answer = str(current_sum) # Initialize the first number in answer string

while current_sum < limit:
    current_number += 1
    current_sum += current_number
    answer += " + " + str(current_number)

print(f"The consecutive sum: {answer} = {current_sum}")
