employees = int(input())
hours = int(input())
valueHour = float(input())

salary = (hours * valueHour * employees) / employees

print("NUMBER = %d" %employees)
print("SALARY = U$ %.2f" %salary)