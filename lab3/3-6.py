a = [int(i) for i in input().split()]
c = max(a)
for i in range(len(a)):
    if a[i]==c:
        print(c, i)
        break
