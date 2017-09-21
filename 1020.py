# -*- coding: utf-8 -*-

valueDays = int(input())

days = valueDays
year = 0
month = 0
if valueDays >= 365:
    year = int(days /365)
    days = days - (year*365)
    month = int(days/30)
    days = days % 30
elif valueDays < 365 and valueDays >= 30:
    month = int(days / 30)
    days = days % 30


print("%d ano(s)" %year)
print("%d mes(es)" %month)
print("%d dia(s)" %days)