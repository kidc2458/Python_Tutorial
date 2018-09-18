numbers = list(range(10))
print(numbers)

del numbers[0]
print(numbers)

del numbers[:5]
print(numbers)

numbers[1:3] = [77,88]
print(numbers)

numbers[1:3] = [77,88,99]
print(numbers)

numbers[1:4] = [8]
print(numbers)



list1 = [0, 1, 2, 3, 4, 5]
# list1의 1부터 3까지를 slice를 이용해서 각각 11, 22, 33으로 바꿔보세요.
# 바꾸고 나면 list1은 [0, 11, 22, 33, 4, 5]가 되어야 합니다.
list1[1:4] = [11,22,33]


list2 = [0, 1, 2, 3, 4, 5]
# list2의 1부터 3까지를 del과 slice를 이용해서 지워보세요
# 바꾸고 나면 list2은 [0, 4, 5]가 되어야 합니다.
del list2[1:4]

print("list1 : {}, list2 : {}".format(list1, list2))