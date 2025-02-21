
def filter_out(x,y):
    if y in x:
         x= x.replace(y,"")
    return float(x)

Months = []
Monthly_statement= {}
Reentry = ""
while Reentry == "y" or "Y":
    Month = input("Enter name of the month: ")
    Monthly_statement["Month"]= Month.upper()
    Month_dict = next((entry for entry in Months if entry["Month"]==Month.upper()), None)

    if Month_dict:
        print(f"Found existing entry for {Month}")
        Additional_salary = input("Enter this month's additional salary in $: ")
        Additional_salary= filter_out(Additional_salary,"$")
        Month_dict["Salary"] += Additional_salary

    else:
        #Salary 
        Salary = input("Enter this month's salary in $: ")
        Salary= filter_out(Salary,"$")
        Monthly_statement["Salary"] = Salary

        #Savings
        Savings_percentage = input("Enter percentage dedicated to savings: ")
        Savings_percentage= filter_out(Savings_percentage,"%")
        Savings_amount = Salary * (Savings_percentage/100)
        Monthly_statement["Savings"] = Savings_amount

        #Rent
        Rent_percentage = input("Enter percentage dedicated to rent: ")
        Rent_percentage= filter_out(Rent_percentage,"%")
        Rent_amount = Salary * (Rent_percentage/100)
        Monthly_statement["Rent"] = Rent_amount
        Monthly_statement["Annual Rent"] = Rent_amount * 12

        # Electricity
        Electricity_percentage = input("Enter percentage dedicated to Electricity: ")
        Electricity_percentage= filter_out(Electricity_percentage,"%")
        Electricity_amount = Salary * (Electricity_percentage/100)
        Monthly_statement["Electricity"] = Electricity_amount
        Monthly_statement["Annual Eelectricity"] = Electricity_amount * 12

        #Utitilies 
        Utilities_total = Savings_amount + Rent_amount + Electricity_amount
        Monthly_statement["Utilities total"] = Utilities_total

        #Remainder
        Remainder = Salary - Utilities_total 
        Monthly_statement["Remainder"] = Remainder

        #Squared salary
        Squared_salary = Salary **2
        Monthly_statement["Squared Salary"] = Squared_salary

        Months.append(Monthly_statement)

    for key, value in Monthly_statement.items():
                if key == "Month":
                    print(f"{key} -------------- {value}")
                else:
                    print(f"{key} -------------- ${value:.2f}")
    Reentry = input("Would you like to add another entry(y for yes and n for no)? ")                       

def filter_out(x,y):
    if y in x:
        x=float(x.replace(y,""))
    else:
        x=float(x)
