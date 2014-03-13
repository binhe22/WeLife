#coding:utf8
import requests 
from wxhack import *
payloads={
        "temp":"30",
        "hum":"90",
        "broken":"1",
        "img":""
        }

def postdata(filename):
    img=open(filename,"rb")
    img=img.read()
    url ='http://127.0.0.1:8000/img'  
    req = requests.post(url,data=payloads)
    return req.text
 
if __name__=="__main__":
    redbot=wx("redbot","xredcn123")
    redbot.LogWX()

