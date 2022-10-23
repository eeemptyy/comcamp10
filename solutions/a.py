n = int(input())

if n <= 15:
  print(0)
elif n <= 120:
  temp = n//60
  print(temp*15)
elif n > (24*60):
  print(690+100)
else:
  n = n - 120
  hr = n//60
  if n%60 > 0:
    hr += 1
  print(30 + (hr*30))