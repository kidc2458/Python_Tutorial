list = [1,2,3,4,5]
for i, v in enumerate(list):
	print('{}번째 값: {}'.format(i,v))
print()
for a in enumerate(list):
	print('{}번째 값: {}'.format(a[0],a[1]))
print()
for a in enumerate(list):
	print('{}번째 값: {}'.format(*a))
print()
print()

ages = {'Tod':35,'Jane':23,'Paul':62}
for a in ages.items():
	print('{}의 나이는:{}'.format(*a))
	
	