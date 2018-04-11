#IPPP Spring 2018
#Varsha Sivaram
#Homework Assignment 2

#Q3
#Editing the calculator for different downpayments
#Importing all modules
import mortgage
import math

#Creating input functions
home_value = float(input("Home Value: "))
min_down_payment = int(input("Minimum Downpayment: "))
max_down_payment = int(input("Maximum Downpayment: "))
term = float(input("Term in years: "))
interest_rate = float(input("Interest Rate: "))

    #Calculating loan amount
for down_payment in range(min_down_payment, max_down_payment, 1000):
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

    #Calculating morgtage values
    m = mortgage.mortgage_payment(l, p, r)
    m = round(m, 2)
    print (down_payment, m)

#end
