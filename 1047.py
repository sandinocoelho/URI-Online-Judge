from datetime import timedelta
entry = input().split()
entry = [int(i) for i in entry]
hourBegin = timedelta(0, 0, 0, 0, entry[1], entry[0])
hourEnd = timedelta(0, 0, 0, 0, entry[3], entry[2])
day = timedelta(days=1)

def calculaHora(hourBegin, hourEnd):
    if hourBegin == hourEnd:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    elif hourBegin < hourEnd:
        res = hourEnd - hourBegin
        hours = int((timedelta.total_seconds(res)/60)/60)
        minutes = int((timedelta.total_seconds(res)/60) - (hours*60))
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hours, minutes))
    elif hourBegin > hourEnd:
        res = (day - hourBegin) + hourEnd
        hours = int((timedelta.total_seconds(res) / 60) / 60)
        minutes = int((timedelta.total_seconds(res) / 60) - (hours * 60))
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hours, minutes))

calculaHora(hourBegin,hourEnd)