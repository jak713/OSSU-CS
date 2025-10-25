"""
The program should work as following:
    1.Ask the user to enter a number 'x'
    2.Ask the user to enter a number 'y'
    3.Print x**y
    4.Print log (base 2) of x
"""

import numpy as np

while True:
    x = float(input("Enter number 'x': "))
    y = float(input("Enter number 'y': "))

    x_powerof_y = x**y
    log_x = np.log2(x)

    print("x**y is: ", x_powerof_y)
    print("log (base 2) of x is: ", log_x, "\n")

    quit = str(input("Type 'q' to quit. Enter to continue. "))

    if quit == "q":
        print("Quitting.")
        break
    else:
        continue
