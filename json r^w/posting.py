import requests

my_data={"Name":"Collins","Email": "Just@example.com"}
r=requests.post("http://www.w3schools.com/php/welcome.php", my_data)

file= open("myfile.html", "w+")
file.write(r.text)
