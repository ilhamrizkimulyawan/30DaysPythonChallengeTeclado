employee_name = input("Enter Employee Name: ").strip().title()
hourly_wage = input("Enter Employee's Hourly Wage: ")
hours_worked = input("Enter Employee's Hours worked this week: ")

total_earnings = float(hourly_wage) * float(hours_worked)

print(f"{employee_name} earned ${total_earnings:.2f} this week." )