"""
The program works in this way:
    1. Three variables x,y,z are assigned by user input. 
    2. If none are an odd number, return and print a statement.
    3. Otherwise, compare x,y,z to find the largest number and print.
"""

def assign_xyz():
    x = int(input("Enter value for x: "))
    y = int(input("Enter value for y: "))
    z = int(input("Enter value for z: "))
    return x,y,z

def find_largest_odd(x,y,z):
    if x%2==0 and y%2==0 and z%2==0:
        print("Nothing odd here")
    elif x>y and x>z:
        print(f"x ({x}) is the largest odd")
    elif y>z:
        print(f"y ({y}) is the largest odd")
    else:
        print(f"z ({z}) is the largest odd")
    return

x,y,z = assign_xyz()
find_largest_odd(x,y,z)
