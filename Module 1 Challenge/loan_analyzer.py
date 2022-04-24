# move imports to beginning of file
import csv
from pathlib import Path

#use loans below to caculate total number of loans, sum of loans
loan_costs = [500, 600, 200, 1000, 450]
# use len function to loan costs above then print number of loans in sentence using print with fstring
number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} number of loans.")

# use sum function to calculate total then print sum of loans in sentence using print with fstring
sum_of_loans = sum(loan_costs)
print(f"The total of all loans is {sum_of_loans}")

#create average loan price variable by divinding sum of loans by number of loans then print in sentence using f string
average_loan_price = (sum_of_loans / number_of_loans)
print(f"The Average loan amount is {average_loan_price}")

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# future_value= 1000
# remaining_months = 9
# discount_rate = .20
# create x and y variable to equal future value and remaining months with get() from loan above
x = loan.get("future_value")
y = loan.get("remaining_months")
# establish future value = x and remaining months = y 
#print x and y
future_value = x
remaining_months = y
print(x)
print(y)

#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
# Use present value formula with monthly version
# create variable for discount rate with given information of 20%
# print fair value of loan in sentence by completeing present value formula monthly version
discount_rate = .20
present_value = x / (1 + discount_rate/12) **y
print(f"Fair Value is {present_value: .2f}")

# create if-else statement to determine the loans fair
# use get() for loan price to determine if present value is >=
# If present value is >= print sentence the loan is worth buying
# Else, present value < print sentence the loan is not worth the price.
if present_value > loan.get("loan_price"):
    print("The Loan is worth buying")
else:
    print("The Loan is not worth the price")


# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# define new function to calculate present value including parameters future_value, remaining_months, annual_discount_rate
# use present value formula with new given information above ( present value formula printed earlier)
# return present value

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) **remaining_months
    print("pv", present_value)
    return present_value


# create variable for annual_discount_rate with info given at 20%
# create variable of cost of new loan to equal new function of calcutated present value created above with information of new loan above
# print sentence with f string saying The present value of new loan and use cost_of_new_loan variable as answer
# round 2 decimals using : .2f at end of cost_of_new_loan variable
annual_discount_rate = .2
cost_of_new_loan=calculate_present_value(new_loan["future_value"], annual_discount_rate ,new_loan["remaining_months"])
print(f"The present value of the new loan is: {cost_of_new_loan: .2f}")


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# create empy list called inexpensive_loans
# create inexpensive_loans variable and equal it to []
inexpensive_loans = []

# use for loop through loans in list above for loans $500 or less
# if loan price from list above <= 500 append loan to inexpensive_loans variable created earlier
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

# print sentence telling us which loans were append to inexpensive_loans List
print("The list is: ", inexpensive_loans)

# set output header to equal loan_price, remaining_months, repayment_intervals, future_value
# set output file path by output_path variable to equal Path("inexsensive_loans.csv") to create new csv file
# use with open to output path to open csv file
# create csvwriter variable and use .writerow method to write row of data, this being the header
# use for loop to get data of loans from inexpensive_loans, then .writerow method to print values of those loans
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

output_path = Path("inexpensive_loans.csv")
with open(output_path, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
