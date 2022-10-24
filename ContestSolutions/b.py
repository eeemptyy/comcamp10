# B

bi = input()
power = 0
total = 0
for i in range(len(bi)-1, -1, -1):
  digit = bi[i]
  total += int(digit)*2**power
  power += 1
print(total)
