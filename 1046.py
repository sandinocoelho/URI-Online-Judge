from math import fabs
import datetime
entry = input().split()
entry = [int(i) for i in entry]

hourBegin = entry[0]
hourEnd = entry[1]

def calculaHora(hourBegin, hourEnd):
    if hourBegin == hourEnd:
        print("O JOGO DUROU 24 HORA(S)")
    elif hourBegin > hourEnd:
        total = fabs((24-hourBegin) + hourEnd)
        print("O JOGO DUROU %d HORA(S)" %total)
    elif hourBegin < hourEnd:
        total = fabs(hourEnd - hourBegin)
        print("O JOGO DUROU %d HORA(S)" % total)

calculaHora(entry[0], entry[1])