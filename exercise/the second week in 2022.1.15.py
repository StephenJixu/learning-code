G-sort编写key来进行排序




'''第二周A'''
import math
while True:
    n = int(input())
    if n == '':
        break
    Sum = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            ex = math.sqrt(i * i + j * j)
            if ex%1 == 0 and ex<=n:
                Sum=Sum+1
    print(int(Sum>>1))



'''第二周B'''
lst=[i**2 for i in range(10,32)]
output = []
y = 0
for i in lst:
    lst1= []
    temp = i
    while True:
        chu = i%10
        lst1.append(chu)
        i//=10
        if i == 0:
            break
    if len(lst1) != len(set(lst1)):
        output.append(temp)
ans = input()
print(output[int(ans)-1])



'''第二周C'''
number = int(input())
matrix = [([0] * number) for l in range(number)]



i = 0
j = number-1
total = matrix[i][j] = 1
while (total < number * number):
    # 向右填数
    while (j + 1 < number and matrix[i][j + 1] == 0):
        total += 1
        j += 1
        matrix[i][j] = total
    # 向下填数
    while (i + 1 < number and matrix[i + 1][j] == 0):
        total += 1
        i += 1
        matrix[i][j] = total
    # 向左填数
    while (j > 0 and matrix[i][j - 1] == 0):
        total += 1
        j -= 1
        matrix[i][j] = total
    # 向上填数
    while (i + 1 > 0 and matrix[i - 1][j] == 0):
        total += 1
        i -= 1
        matrix[i][j] = total
for i in range(number):
    for j in range(number):
        print ('%d' % matrix[i][j],end='')
    print()



'''第二周D'''
high,up,down = map(int,input().split())
re = up-down
calc = (high-up)%re
if calc == 0:
    day = (high-up)//re+1
else:
    day = (high-up)//re+2
print(day)


'''第二周E'''
number = int(input())
n = number*2-1
matrix = [([0] * n) for l in range(n)]
i = 0
j = number-1
total = matrix[i][j] = 1
while (total < n * n):
    # 第一行
    if i == 0 and j == n-1:
        total += 1
        i += 1
        matrix[i][j] = total

    elif (i == 0 and j != n-1):
        total += 1
        i = n-1
        j += 1
        matrix[i][j] = total
    # 最后一列
    elif (j == n-1 and i !=0):
        total += 1
        j = 0
        i -= 1
        matrix[i][j] = total
    elif i == n-1 and j == n-1:
        total += 1
        i += 1
        matrix[i][j] = total
    elif matrix[i-1][j+1] != 0:
        total += 1
        i += 1
        matrix[i][j] = total
    elif matrix[i-1][j+1] == 0 :
        total += 1
        i -= 1
        j += 1
        matrix[i][j] = total
for i in range(n):
    for j in range(n):
        print ('%d ' % matrix[i][j],end='')
    print()

























'''第二周F'''
forn,K = map(int,input().split())
namel = []
tsl = []
for i in range(forn):
    name,ts = input().split()
    namel.append(name)
    tsl.append(int(ts))
dit = {x: y for x, y in zip(tsl, namel)}
tsl.sort(reverse=False)
print(dit[tsl[K-1]])





'''第二周G'''
a = []
n = int(input())
def f(x):
    if x[1] >= 60:
        return (-x[1],x[2])
    else:
        return (0,x[2])
for i in range(n):
    into = input().split()
    lst = [into[0],int(into[1]),i]
    a.append(lst)
a.sort(key=f)
for i in range(n):
    print(a[i][0])
