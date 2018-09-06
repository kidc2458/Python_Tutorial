
def get_web(url):
	"""URL을 넣으면 페이지 내용을 돌려주는 함수"""
	import urllib.request
	response = urllib.request.urlopen(url)
	data = response.read()
	decode = data.decode('utf-8')
	return decode
	
url = input('웹 페이지 주소?')
content = get_web(url)
print(content)