a = [int(i) for i in input().split()]
k, c = map(int, input().split())
a.append(0)
a = a[:k] + [c] + a[k:-1]
print(' '.join([str(i) for i in a]))
