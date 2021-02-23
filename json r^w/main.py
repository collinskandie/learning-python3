import simplejson as json
import os

if os.path.isfile(".\profile.txt") and os.stat(".\profile.txt").st_size !=0:
    old_file= open(".\profile.txt","r+")
    data= json.loads(old_file.read())
    print("Data age is",data["age"],"____add age 1 to data current age")
    data["age"]=data["age"]+1
    print("Data new age is:", data["age"])

else:
    old_file=open(".\profile.txt","w+")
    data={"Name": "Collins","age": 22}
    print("No data found setting defaul age to",data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
