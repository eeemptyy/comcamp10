sec = int(input())

hr = sec//3600
sec = sec%3600
minn = sec//60
sec = sec % 60

print('{:02d}:{:02d}:{:02d}'.format(hr, minn, sec))