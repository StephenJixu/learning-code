 #(走廊搬桌子)corridor
keys = [i for i in range(0, 199)]
values = [0 for i in range(0, 199)]
dic = {x: y for x, y in zip(keys, values)}
n = int(input())
while n:
    f, e = map(int, input().split(' '))
    for i in range(f, e+1, 2):
        dic[(i-1)//2] += 1
    n -= 1
times = max(dic.values())
print(10*times)
