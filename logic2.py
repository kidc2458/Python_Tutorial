def return_false():
	print("함수 return_false")
	return False

def return_true():
	print("함수 return_true")
	return True
	
print("테스트1")
a = return_false()
b = return_true()

if a and b:
	print(True)
else:
	print(False)

#단락 평가
print("테스트2")
if return_false() and return_true():
	print("True")
else:
	print(False)