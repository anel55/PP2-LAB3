a = input().split()
c = 0
for i in range(1, len(a)):
    if a[i-1] != a[i]:
        c += 1
print(c + 1)
