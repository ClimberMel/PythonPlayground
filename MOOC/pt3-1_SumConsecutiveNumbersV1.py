'''Please write a program which asks the user to type in a limit. 
The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) 
until the sum is at least equal to the limit set by the user.
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
'''

limit = int(input("Please enter a limit: "))
current_sum = 0     # initialize sum
current_number = 1  # set stating number

while current_sum < limit:
    current_sum += current_number
    current_number += 1
    #print(current_sum) # use to show progress or to debug

print(f"The sum of consecutive numbers up to the limit {limit} is: {current_sum}")
