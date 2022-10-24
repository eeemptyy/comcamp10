nf = int(input())

if nf == 1:
    print('0')
elif nf == 2:
    print('0 1')
else:
    ls = [0, 1]
    c=2
    while len(ls) < nf:
        ls.append(ls[c-2]+ls[c-1])
        c += 1
    print(' '.join(str(i) for i in ls))