a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i], a[i-1] = a[i-1], a[i]
for i in a:
    print(i, end = ' ')
