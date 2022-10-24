# A
inp1 = input()
inp2 = input()
inp3 = input()
inp4 = input()
inp5 = input()

a = 1
b = 0
c = 0

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



if inp2 == 'A':
  t = a
  a = b
  b = t
elif inp2 == 'B':
  t = b
  b = c
  c = t
elif inp2 == 'C':
  t = a
  a = c
  c = t

if inp3 == 'A':
  t = a
  a = b
  b = t
elif inp3 == 'B':
  t = b
  b = c
  c = t
elif inp3 == 'C':
  t = a
  a = c
  c = t

if inp4 == 'A':
  t = a
  a = b
  b = t
elif inp4 == 'B':
  t = b
  b = c
  c = t
elif inp4 == 'C':
  t = a
  a = c
  c = t

if inp5 == 'A':
  t = a
  a = b
  b = t
elif inp5 == 'B':
  t = b
  b = c
  c = t
elif inp5 == 'C':
  t = a
  a = c
  c = t

if a:
  print(1)
elif b:
  print(2)
else:
  print(3)
