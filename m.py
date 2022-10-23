a = int(input())

fine = 0
u = 0
t = 5
for i in range(6):
  v = u + a*t
  u = v

  rfine = 0
  if v >= 30 and v < 60:
    rfine = 100
  elif v >= 60 and v < 90:
    rfine = 200
  elif v >= 90 and v <= 100:
    rfine = 500
  elif v > 100:
    rfine = 500 + ((v-100)*100)

  fine += rfine
print(fine)