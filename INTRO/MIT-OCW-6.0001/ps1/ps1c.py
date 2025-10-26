## 6.100A PSet 1: Part C
## Name: Julia Kaczmarek
## Time Spent: 15:45 - 16:48
## Collaborators: - 

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_house = 800000
down_payment_percentage = 0.25
months_required = 36
leeway = 100

high = 1
low = 0
r = (high+low)/2
steps = 0
amount_saved = initial_deposit*(1+(r/12))**months_required
print(f"So far we have {amount_saved}")
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
cost_downpayment = cost_of_house*down_payment_percentage
print(f"The downpayment we need is {cost_downpayment}")

if cost_downpayment-leeway<=initial_deposit:
    r = 0
else:
    while abs(cost_downpayment-amount_saved) > leeway:

        amount_saved = initial_deposit* (1+(r/12))**months_required

        if amount_saved < cost_downpayment-leeway:
            low = r
        else:
            high = r
        
        r = (high+low)/2
        steps += 1
        if r == 1 and amount_saved<=cost_downpayment-leeway:
            r=None
            break

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")