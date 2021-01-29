import requests

f= open("valid_Accounts.txt","a")
with open('users.txt',encoding="utf8") as users:
    for user in users:
        user = user.rstrip("\n")
        url = f"https://ask.fm/{user}"
        r = requests.get(url)
        if r.status_code == 200:
            print(f"{user}")
            error = "Well, apparently not anymore."
            if error not in r.content.decode():
                txt=f"{url}\n"
                f.write(txt)

            else:
                print("Well, apparently not anymore.")