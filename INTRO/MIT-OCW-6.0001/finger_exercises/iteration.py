"""
The program workings:
    1. Take in 10 integers from user input.
    2. Print the largest odd number that was entered.
    2*. If no odd number entered, print a statement saying so.
"""

nums = []
for i in range(10):
    input_num = int(input("Input a number: "))
    nums.append(input_num)

print(f"The ten numbers you gave me are {nums}")

largest_odd = float('-inf')
for i in nums:
    if i%2!=0 and i>largest_odd:
        largest_odd = i

print(f"According to my calculations... The largest odd number is {largest_odd}")
