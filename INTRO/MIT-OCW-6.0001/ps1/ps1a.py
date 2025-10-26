## 6.100A PSet 1: Part A
## Name: Julia Kaczmarek
## Time Spent: 10 ish mins? maybe 5
## Collaborators: - 

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter the portion (decimal, 0.1 = 10%) you save: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25
amount_saved = 0
r = 0.05 # Annual rate of return
monthly_salary = yearly_salary/12
number_of_months = 1


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
# yearly salary need to be turned to monthly since i am determining number of months

while amount_saved<portion_down_payment*cost_of_dream_home:
    amount_saved+=monthly_salary*portion_saved
    amount_saved+=amount_saved*(r/12)
    number_of_months+=1

print(f"Number of months needed to save up for down payment: {number_of_months}")