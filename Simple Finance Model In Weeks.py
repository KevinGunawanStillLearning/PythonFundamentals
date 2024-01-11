#Simple Finance Model In Weeks

finance = {
'expenses': [200, 250, 225, 250, 320, 250, 350, 400, 300],
'income': [780, 750, 900, 760, 720, 750, 700, 100, 750]
}
# Calculation of average income and average expenditure
total_expenses = 0
total_income = 0
for cost in finance['expenses']:
    total_expenses += cost
for cost in finance['income']:
    total_income += cost
average_expenses = total_expenses / len(finance['expenses'])
average_income = total_income / len(finance['income'])
print(average_expenses)
print(average_income)