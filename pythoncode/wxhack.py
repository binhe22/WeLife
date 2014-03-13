#coding:utf8
import os
import redis
import json
import re
import voice
from StringIO import StringIO
import requests
import base64
from BeautifulSoup import BeautifulSoup as bs
from hashlib import md5
import time

class wx(object):
    def __init__(self,name,passwd):
        self.name=name
        self.passwd=passwd
        self.headers={"Accept":"application/json, text/javascript, */*; q=0.01",
                    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin":"https://mp.weixin.qq.com",
                    "Referer":"https://mp.weixin.qq.com/",
                    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36",
                    "X-Requested-With":"XMLHttpRequest"}
        self.token=''
        self.cookies=dict()
        self.musicurl="https://mp.weixin.qq.com/cgi-bin/getvoicedata?msgid=%s&fileid=&token=%s&lang=zh_CN"
        self.getnewsumurl="https://mp.weixin.qq.com/cgi-bin/getnewmsgnum"
        self.allmessage="https://mp.weixin.qq.com/cgi-bin/message?t=message/list&count=%s&day=7&token=%s&lang=zh_CN"
        self.cookieskey=['slave_user','cert','slave_sid','remember_acct','sig']
        self.GetNewSum="https://mp.weixin.qq.com/cgi-bin/getnewmsgnum"
        self.lastid=0
        self.SendMessageUrl="https://mp.weixin.qq.com/cgi-bin/singlesend"
    def md5value(self,values):
        m=md5()
        m.update(values)
        return m.hexdigest()

    def IfNewMessage(self):
        payload={"token":self.token,
                 "lang":"zh_CN",
                 "t":"ajax-getmsgnum",
                 "lastmsgid":self.lastid}
        #print payload
        newheaders=self.headers
        newheaders["Referer"]="https://mp.weixin.qq.com/cgi-bin/message?t=message/list&count=20&day=7&token=451466215&lang=zh_CN"
        #print newheaders,cookies
        IfMessageRetu=requests.post(self.GetNewSum,cookies=self.cookies,headers=newheaders,data=payload,timeout=3)
        #print IfMessageRetu.text
        return json.loads(IfMessageRetu.text)["newTotalMsgCount"]

    def SendMessage(self,userid,msgid,content):
        payload={
                "mask":"false",
                "tofakeid":userid,
                "imgcode":"",
                "type":"1",
                "content":content,
                "quickreplyid":msgid,
                "token":self.token,
                "lang":"zh_CN",
                "t":"ajax-response"
                }
        newheaders=self.headers
        newheaders["Referer"]="https://mp.weixin.qq.com/cgi-bin/message?"
        #print self.SendMessageUrl,payload,newheaders
        a=requests.post(self.SendMessageUrl,data=payload,cookies=self.cookies,headers=newheaders,timeout=3)
        #print a.text
        #return json.loads(a.text)["msg"]



    def update_cookies(self,backinfo):
        for item in self.cookieskey:
            try:
                self.cookies[item]=backinfo.cookies[item]
            except Exception,e:
                print e

    def LogWX(self):
            payload = {'username': self.name, 'pwd':self.md5value(self.passwd),'imgcode':'','f':'json'}
            print payload
            a=requests.post("https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN",data=payload,headers=self.headers,timeout=3)
            jinfo=json.loads(a.text)
            newurl="https://mp.weixin.qq.com"+jinfo["ErrMsg"]
            self.token=re.findall("token=(.*)",jinfo["ErrMsg"])
            self.token=self.token[0]
            self.update_cookies(a)

    def GetMessageList(self,num):
            url=self.allmessage%(num,self.token)
            getidheaders=self.headers
            newrefer="https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=%s"%self.token
            getidheaders["Referer"]=str(newrefer)
            getidheaders["Accept"]="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            a=requests.get(url,cookies=self.cookies,headers=getidheaders)
            #print cookiesG
            #print getidheaders
            #print url
        # print a.text
            info=re.findall('list : \({"msg_item":(.*)}\).msg_item ',a.text)
            return json.loads(info[0])


    def GetListContent(self,messagelist):
            try:
                self.lastid=messagelist[0]["id"]
            except:
                pass
            MessageContent=[]
            OneMessage={}
            count=0
            for item in messagelist:
                userid=item["fakeid"]
                msgid=item["id"]
                nick_name=item["nick_name"]
                self.SendMessage(userid,msgid,"redbot")
                if item["type"]==1:
                    msgcontent=item["content"]
                    #print nick_name,"say: ",item["content"]
                if item["type"]==3:
                    url=self.musicurl%(item["id"],self.token)
                    #print url
                    temp=requests.get(url,cookies=self.cookies)
                    f=open("../fetchvoice/"+str(item["id"])+".mp3","wb+")
                    f.write(temp.content)
                    f.close()
                    mycommand="lame --decode ../fetchvoice/%d.mp3    ../fetchvoice/%d.wav"%(item["id"],item["id"])
                    os.system(mycommand)
                    con=voice.gettext("../fetchvoice/%s.wav"%item["id"])
                    #print con
                    con=json.loads(con)
                    backinfo=con["hypotheses"]
                    try:
                        backinfo=backinfo[0]
                        if backinfo["confidence"]>0.3:
                            #print item["nick_name"],"say: ",backinfo['utterance']
                            msgcontent=backinfo['utterance']
                        else:
                            #print item['nick_name'],"can't hear"
                            msgcontent="can't hear"
                    except Exception,e:
                        print str(e)
                        #print item['nick_name'],"can't hear"
                        msgcontent="can't hear"


                OneMessage["userid"]=userid
                OneMessage["msgid"]=msgid
                OneMessage["name"]=nick_name
                OneMessage["msgcontent"]=msgcontent
                MessageContent.append(OneMessage)
            return MessageContent


        #typeinfo=re.findall('"type":"(\d*)"',a.text)
if __name__=="__main__":
        #name=raw_input("name:")
        #passwd=raw_input("password:")
        redbot=wx("your name","your password")
        redbot.LogWX()
        print redbot.GetMessageList(5)
        redbot.GetListContent(redbot.GetMessageList(5))
        time.sleep(1)
        while 1:
            num=redbot.IfNewMessage()
            if num:
                print redbot.GetListContent(redbot.GetMessageList(num))
            time.sleep(5)









