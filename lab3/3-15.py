s = input().split()
n, k = int(s[0]), int(s[1])
a = ['I' for i in range(n)]
for i in range(k):
    s = input().split()
    l, r = int(s[0]), int(s[1])
    for j in range(l-1, r):
        a[j] = '.'
for i in a: print(i, end='')
