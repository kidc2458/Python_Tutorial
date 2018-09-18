dic = {"Key2":"Value1"}

if "Key1" in dic and dic["Key1"] == "Value1":
	print("Key1도 있고, 그 값은 Value1이네")
else:
	print("아니네")
	
#에러
if dic["Key1"] == "Value1" and "Key1" in dic:
	print("Key1도 있고, 그 값은 Value1이네")
else:
	print("아니네")