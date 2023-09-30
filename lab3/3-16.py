arr = []
for _ in range(8):
    arr.append([int(i) for i in input().split()])

ans = 'NO'
for i in range(8):
    x, y = arr[i]
    for j in range(i+1, 8):
        x2, y2 = arr[j]
        if x == x2 or y == y2 or (abs(x-x2) == abs(y-y2)):
            ans = 'YES'

print(ans)
