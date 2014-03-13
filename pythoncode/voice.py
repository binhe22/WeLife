#coding:utf8
import requests
def gettext(filename):
    music=open(filename,"rb")
    audio=music.read()
    url ='http://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=zh-CN&maxresults=1'
    headers = {'Content-Type' : 'audio/L16; rate=8000'}
    req = requests.post(url,data=audio,headers=headers,timeout=3)
    return req.text
