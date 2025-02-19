Monthly_statement= {}

Month = input("Enter name of the month: ")
Monthly_statement["Month"]= Month.upper()

Salary = input("Enter this month's salary in $: ")
if "$" in Salary:
    Salary = float(Salary.replace("$", ""))
else:
    Salary = float(Salary)
Monthly_statement["Salary"] = Salary

Savings_percentage = input("Enter percentage dedicated to savings: ")
if "%" in Savings_percentage:
    Savings_percentage = float(Savings_percentage.replace("%", ""))
else:
    Savings_percentage = float(Savings_percentage)
Savings_amount = Salary * (Savings_percentage/100)
Monthly_statement["Savings"] = Savings_amount

Additional_savings = input("Enter this month's additional savings in $: ")
if "$" in Additional_savings:
    Additional_savings = float(Additional_savings.replace("$", ""))
else :
    Additional_savings = float(Additional_savings)

Rent_percentage = input("Enter percentage dedicated to rent: ")
if "%" in Rent_percentage:
    Rent_percentage = float(Rent_percentage.replace("%", ""))
else :
    Rent_percentage = float(Rent_percentage)
Rent_amount = Salary * (Rent_percentage/100)
Monthly_statement["Rent"] = Rent_amount

Electricity_percentage = input("Enter percentage dedicated to Electricity: ")
if "%" in Electricity_percentage:
    Electricity_percentage = float(Electricity_percentage.replace("%", ""))
else :
    Electricity_percentage = float(Electricity_percentage)

Electricity_amount = Salary * (Electricity_percentage/100)
Monthly_statement["Electricity"] = Electricity_amount

Utilities_total = Savings_amount + Rent_amount + Electricity_amount
Monthly_statement["Utilities total"] = Utilities_total

Remainder = Salary - Utilities_total 
Monthly_statement["Remainder"] = Remainder

Squared_salary = Salary **2
Monthly_statement["Squared Salary"] = Squared_salary

Savings_total = Savings_amount + Additional_savings

Savings_left = Savings_total * (100 - (Additional_savings/Savings_total))/100 

for key, value in Monthly_statement.items():
    if key == "Month":
        print(f"{key} -------------- {value}")
    else:
        print(f"{key} -------------- ${round(value,2)}")
