a = [int(i) for i in input().split()]
minA=a.index(min(a))
maxA=a.index(max(a))
a[minA], a[maxA]=a[maxA], a[minA]

print(' '.join([str(i) for i in a]))
