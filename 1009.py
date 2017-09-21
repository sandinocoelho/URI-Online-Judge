employe = input()
salary = float(input())
sells = float(input())
bonus = (sells/100) * 15
salaryBonus = (salary + bonus)


print("TOTAL = R$ %.2f" %salaryBonus)