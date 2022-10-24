# A
inp2 = input()
inp3 = input()
inp4 = input()
inp5 = input()

a = 1
b = 0
c = 0
for i in range(5):
    inp1 = input()

    if inp1 == 'A':
        t = a
        a = b
        b = t
    elif inp1 == 'B':
        t = b
        b = c
        c = t
    elif inp1 == 'C':
        t = a
        a = c
        c = t

if a:
    print(1)
elif b:
    print(2)
else:
    print(3)
