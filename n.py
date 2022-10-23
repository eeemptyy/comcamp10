minn = int(input())
hr = int(input())

totalMins = hr*60 + minn
basedMin = totalMins

state = ['1st Phase', '2nd Phase', '3rd Phase', 'REM Phase']

c = 0
while totalMins > 0:
    if c == 0:
        totalMins -= 5
    elif c == 1:
        totalMins -= 15
    elif c == 2:
        totalMins -= 60
    elif c == 3:
        totalMins -= 10
    elif c == 4:
        c = -1
    c += 1

if c==5:
    c = 1
if basedMin == 0:
    print('Awake')
else:
    print(state[c-1])