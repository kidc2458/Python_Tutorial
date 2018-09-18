def safe_index(my_list, value):
    # 함수를 완성하세요
    if value in my_list:
        return my_list.index(value)
    else:
        return None

print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))

list1 = [1, 2, 3, 4]

# 아래줄에서 list1의 1번째 자리에 8을 넣고 원래 있던 값은 오른쪽으로 밀어 보세요.
list1.insert(1,8)

print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))
# 아래줄에서 list1을 작은 수부터 큰 수로 정렬해 보세요
list1.sort()

print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))
# 아래줄에서 list1을 거꾸로 만들어 보세요
list1.reverse()




print("list1을 거꾸로 정렬한 결과 : {}".format(list1))

str = "오늘은 날씨가 흐림"

# split()을 이용해서 str을 공백으로 나눈 문자열을 words에 저장하세요
words = str.split()

# index()를 이용해서 "흐림"이 words의 몇번째에 있는지 찾고, 
# position에 저장하세요.
position = words.index("흐림")

words[position] = "맑음"

# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장하세요. 
# words를 문자열로 바꿀때는 공백 한 칸을 기준으로 붙이면 됩니다.
new_str = " ".join(words)

print(new_str)