import requests


base_url="http://127.0.0.1:8000/PANTERA_API/V1"

def registeruser(username,name,user_id):
    url=f'{base_url}/USERS'
    response=requests.get(url)
    res=response.json()
    user_exits=False
    for i in res:
        if i["user_id"] == str(user_id):
            user_exits = True
            break



    if user_exits == False:
        requests.post(url,data={"name": name, "user_name":username,"user_id":user_id})
    else:
        return "ushbu foydalanuvchi allaqachon mavjud!"
# registered=registeruser(name="muhiddinov",user_id="1234567",username="abdulhodiy")
# print(registered)

def feedback(user_id,Text):
    url = f'{base_url}/FEEDBACKS'
    if Text and user_id:
        requests.post(url,data={"user_id": user_id, "Text":Text})
    else:
        return print("AMAL BJARILMADI!!")