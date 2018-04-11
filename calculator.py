#IPPP Spring 2018
#Varsha Sivaram
#Homework Assignment 2

#Q2
#Making a calculator
#Importing all modules
import mortgage

#Creating input functions
home_value = float(input("Home Value: "))
down_payment = float(input("Downpayment: "))
term = float(input("Term in years: "))
interest_rate = float(input("Interest Rate: "))

#Calculating loan amount
def loan(home_value, down_payment):
    return(home_value - down_payment)
l = float(loan(home_value, down_payment))

#Calculating monthly periods
def monthly_period(term):
    return(term*12)
p = float(monthly_period(term))

#Calculating monthly interest rate
def monthly_rate(interest_rate):
    return((interest_rate/100)/12)
r = float(monthly_rate(interest_rate))

#Calculating mortgage payment
m = float(mortgage.mortgage_payment(l, p, r))
final_mortgage_payment = round(m, 2)
print("Monthly payment: ", final_mortgage_payment)

#end
