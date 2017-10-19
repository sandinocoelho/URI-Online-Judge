from datetime import datetime

entryDayBegin = input().split()
entryHourBegin = input().split(" : ")
entryDayEnd = input().split()
entryHourEnd = input().split(" : ")

dateBegin = datetime(2017, 4, int(entryDayBegin[1]), int(entryHourBegin[0]), int(entryHourBegin[1]), int(entryHourBegin[2]))
dateEnd = datetime(2017, 4, int(entryDayEnd[1]), int(entryHourEnd[0]), int(entryHourEnd[1]), int(entryHourEnd[2]))

duration = str(dateEnd - dateBegin)

if entryDayBegin == entryDayEnd:
    durationTime = str(duration)
    durationTime = durationTime.split(":")
    days = 0
    hours = int(durationTime[0])
    minutes = int(durationTime[1])
    seconds = int(durationTime[2])
else:
    duration = duration.split(" ")
    durationTime = str(duration[2])
    durationTime = durationTime.split(":")
    days = int(duration[0])
    hours = int(durationTime[0])
print("%d hora(s)" %(hours))
print("%d minuto(s)" %(minutes))
print("%d segundo(s)" %(seconds))