m = input()
lss = [
  ['000', '  0', '000', '000', '0 0', '000', '000', '000', '000', '000'],
  ['0 0', '  0', '  0', '  0', '0 0', '0  ', '0  ', '  0', '0 0', '0 0'],
  ['0 0', '  0', '000', '000', '000', '000', '000', '  0', '000', '000'],
  ['0 0', '  0', '0  ', '  0', '  0', '  0', '0 0', '  0', '0 0', '  0'],
  ['000', '  0', '000', '000', '  0', '000', '000', '  0', '000', '000']
]

prt = []
for i in range(5):
  for j in range(len(m)):
    n = int(m[j])
    prt.append(lss[i][n])
    if (j != len(m)-1):
      prt.append('  ')
  prt.append('\n')

print(''.join(prt))
