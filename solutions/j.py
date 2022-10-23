ori = input().split(' ')
end = input().split(' ')

sx = int(ori[0])
sy = int(ori[1])
ex = int(end[0])
ey = int(end[1])

print(abs(sx-ex) + abs(sy-ey))