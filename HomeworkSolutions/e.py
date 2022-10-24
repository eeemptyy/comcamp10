ori = input().split(' ')
end = input().split(' ')

sx = float(ori[0])
sy = float(ori[1])
ex = float(end[0])
ey = float(end[1])

print(abs(sx-ex) * abs(sy-ey))