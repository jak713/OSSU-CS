## 6.100A PSet 1: Part B
## Name: Julia Kaczmarek
## Time Spent: 15:23 - 15:33 (10 mins)
## Collaborators: -

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################

yearly_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter the portion (decimal, 0.1 = 10%) you save: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise, as decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


portion_down_payment = 0.25
amount_saved = 0
r = 0.05 # Annual rate of return
monthly_salary = yearly_salary/12
number_of_months = 1 #note we start at month 1 because we need some money...
raise_counter = 1
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved<portion_down_payment*cost_of_dream_home:
    amount_saved+=monthly_salary*portion_saved
    amount_saved+=amount_saved*(r/12)
    number_of_months+=1
    raise_counter += 1

    if raise_counter == 6:
        yearly_salary+=yearly_salary*semi_annual_raise
        monthly_salary = yearly_salary/12
        raise_counter=0

print(f"Number of months needed to save up for down payment: {number_of_months}")