a = list(map(int, input().split()))
a.sort()
amount = 0
b = 0
for i in range(a[-1] + 1):
    b = a.count(i)
    if b > 1 :
        while b != 0:
            b += -1
            amount += b
print(amount)
