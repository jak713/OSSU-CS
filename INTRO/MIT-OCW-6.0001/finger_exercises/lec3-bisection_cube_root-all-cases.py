cube = float(input("Enter a number whose cube root you would like to find: "))

epsilon = 0.01
num_guesses = 0
low = 0

if 0 < cube < 1:
    high = 1
else:
    high = abs(cube)
    
guess = (high + low)/2.0

while abs(guess**3 - abs(cube)) >= epsilon:
    if guess**3 < abs(cube):
        # look only in upper half search space
        low = guess
    else:
        # look only in lower half search space
        high = guess
    # next guess is halfway in search space
    guess = (high + low)/2.0
    num_guesses += 1
    
print('num_guesses =', num_guesses)

if cube < 0:
    guess = -guess
print(guess, 'is close to the cube root of', cube)
