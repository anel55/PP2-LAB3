x = input()
p = input()
line = [i for i in x.split() if int(i) >= int(p)]
print(len(line) + 1)
