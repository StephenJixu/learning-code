


'''A---T1524'''
# money = float(input())
# rate_list = (input().split())
# max_rate = float(max(rate_list))
# output = max_rate * money
# print('%.2f' % output)







# '''B---T1654 '''
# n, m = map(int, input().split())
# an_list = list(map(int,input().split()))
# # new_An = []
# zero_flag = False
# times = 1
# tota = 0

# for i in an_list:
#     new_An.append(int(i))
# for i in new_An:
#     if i > m:
#         times += 1
#     elif i == m:
#         times += 1
#         tota = 0
#     elif tota >= n:
#         times += 1
#         tota = i
#     else:
#         tota += i
# print(times)
#
# for i in an_list:
#     tota += i
#     if tota > m:
#         times += 1
#         tota = 0
#         tota += i
# print(times)







'''C---T1279'''
# phrase1 = list(input())
# phrase2 = list(input())
# phrase3 = list(input())
# letter_set = []
# dis = 0
# for i in range(len(phrase1)):
#     letter_set.clear()
#     letter_set.append(phrase1[i])
#     letter_set.append(phrase2[i])
#     letter_set.append(phrase3[i])
#     if len(set(letter_set)) == 2:
#         dis += 1
#     elif len(set(letter_set)) == 3:
#         dis += 2
# print(dis)





'''D---T1445'''
# num = input()
# lst = list(map(int, input().split()))
# set_lst = set(lst)
# uncompare = []
# times = 0
# for i in set_lst:
#     if lst.count(i)%2 == 1:
#         uncompare.append(i)
# uncompare.sort()
# for i in range(0,len(uncompare),2):
#     times += (uncompare[i+1]-uncompare[i])
# print(times)






'''E---T1730'''
# num = int(input())
# lst = list(map(int, input().split()))
# sorted_list = sorted(enumerate(lst, start=1), key=lambda x: x[1])
# sorted_id = [i[0] for i in sorted_list]
# p = num
# total = 0
# for i in lst:
#     total += (i*(p-1))
#     p -= 1
# old_time = total/num
# sorted_list = sorted(lst)
# total = 0
# p = num
# for i in sorted_list:
#     total+= (i*(p-1))
#     p -= 1
# new_time = total/num
# for i in range(num):
#     print(sorted_id[i],end=' ')
#
# if new_time < old_time:
#     print('\n%.2f' % new_time)
# else:
#     print('\n%.2f' % new_time)





'''F---T1395'''
# ori = list(input())
# turn = list(input())
# times = 0
# flag = False
# i = 0
# while i < len(ori):
#
#     if ori[i] != turn[i]:
#         if i == len(ori)-1:
#             print('No Answer.')
#             flag = True
#             break
#         elif ori[i+1] != turn[i+1]:
#             times += 1
#             i += 1
#         else:
#             temp = i
#             i += 1
#             while ori[i] == turn[i]:
#                 i += 1
#                 if i == len(ori):
#                     print('No Answer.')
#                     flag= True
#                     break
#             times += (i-temp)
#
#     i += 1
# if flag == False:
#     print(times)
'''F-优解'''
# a = list(input())
# b = list(input())
# count = 0
# for i in range(len(a) - 1):
#     if a[i] == b[i]:
#         continue
#     else:
#         if a[i+1] == '*':
#             a[i], a[i + 1] = b[i], 'o'
#         else:
#             a[i], a[i + 1] = b[i], '*'
#         count += 1
# if a == b:
#     print(count)
# else:
#     print('No Answer')
'''F-优解2'''
# a = list(input())
# b = list(input())
# count = 0
# for i in range(len(a) - 1):
#     if a[i] == b[i]:
#         continue
#     else:
#         if a[i+1] == '*':
#             b[i], a[i+1] = a[i], 'o'
#         else:
#             b[i], a[i+1] = a[i], '*'
#         count += 1
# if a == b:
#     print(count)
# else:
#     print('No Answer')




'''G---T1982'''
# num = int(input())
# total_list = []
# for i in range(num):
#     lst = list(input().split('/'))
#     total_list.append(lst)
# pr_list = sorted(total_list, key=lambda x: (int(x[2]),  int(x[1]), int(x[0])), reverse=False)
# print_format = '{}/{}/{}/'
# for i in range(len(pr_list)):
#     print(print_format.format(pr_list[i][0], pr_list[i][1], pr_list[i][2]))
#     # print(f'{pr_list[i][0]}/{pr_list[i][1]}/{pr_list[i][2]}')
