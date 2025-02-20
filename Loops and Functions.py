
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
        if "$" in Additional_salary:
            Additional_salary = float(Additional_salary.replace("$", ""))
        else:
            Additional_salary = float(Additional_salary)
        Month_dict["Salary"] += Additional_salary

    else:
        #Salary 
        Salary = input("Enter this month's salary in $: ")
        if "$" in Salary:
            Salary = float(Salary.replace("$", ""))
        else:
            Salary = float(Salary)
        Monthly_statement["Salary"] = Salary

        #Savings
        Savings_percentage = input("Enter percentage dedicated to savings: ")
        if "%" in Savings_percentage:
            Savings_percentage = float(Savings_percentage.replace("%", ""))
        else:
            Savings_percentage = float(Savings_percentage)
        Savings_amount = Salary * (Savings_percentage/100)
        Monthly_statement["Savings"] = Savings_amount

        #Rent
        Rent_percentage = input("Enter percentage dedicated to rent: ")
        if "%" in Rent_percentage:
            Rent_percentage = float(Rent_percentage.replace("%", ""))
        else :
            Rent_percentage = float(Rent_percentage)
        Rent_amount = Salary * (Rent_percentage/100)
        Monthly_statement["Rent"] = Rent_amount
        Monthly_statement["Annual Rent"] = Rent_amount * 12

        # Electricity
        Electricity_percentage = input("Enter percentage dedicated to Electricity: ")
        if "%" in Electricity_percentage:
            Electricity_percentage = float(Electricity_percentage.replace("%", ""))
        else :
            Electricity_percentage = float(Electricity_percentage)
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
