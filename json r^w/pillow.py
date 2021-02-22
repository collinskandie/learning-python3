import requests
from io import BytesIO
from PIL import Image

r=requests.get("https://collinskandieportfolio.web.app/images/profile-me.jpeg")

image= Image.open(BytesIO(r.content))
print(image.size,image.format,image.mode)

path=("./image." +image.format)
try:
    image.save(path, image.format)
    print("Save successful")
except IOError:
    print("Erorr occurred")
