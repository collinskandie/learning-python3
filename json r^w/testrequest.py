import requests
r=requests.get("https://collinskandieportfolio.web.app")
print("Status",r.text)

f=open(".\index.html","w+")
f.write(r.text)
