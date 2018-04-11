#IPPP Spring 2018
#Varsha Sivaram
#Homework Assignment 2

## Q4

#Creating input functions
import mortgage
import math


home_value = float(input("Home Value: "))
interest_rate = float(input("Interest Rate: "))
term = float(input("Term in years: "))
d_monthly_payment = float(input("Desired monthly payment: "))

#Calculating monthly periods
def monthly_period(term):
    return(term*12)
p = float(monthly_period(term))

#Calculating monthly interest rate
def monthly_rate(interest_rate):
    return((interest_rate/100)/12)
r = float(monthly_rate(interest_rate))

#Setting the range for down_payment
min_down_payment = 0
max_down_payment = home_value

#Running a bisection function to find the value of the Downpayment
while True:
    d = (min_down_payment + max_down_payment)/2
    Fl = mortgage.mortgage_payment(home_value - d, p, r)

    if abs(Fl - d_monthly_payment) < 1:
        break

    elif Fl < d_monthly_payment:
        #print("max is reduced")
        max_down_payment = d

    else:
        #print("min is increased")
        min_down_payment = d

print("Downpayment: ", round(d, 2))
#end
