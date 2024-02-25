x = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    x.append([name, score])
    
check = sorted({y[1] for y in x})[1]

names = sorted([i[0] for i in x if i[1]==check])

print('\n'.join(names))
