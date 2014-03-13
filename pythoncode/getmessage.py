#coding:utf8
import jieba
import redis
import gevent
from  wxhack import *
def ListenMessage(redbot):
    redbot.GetListContent(redbot.GetMessageList(2))
    gevent.sleep(1)
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    while 1:
        try:
                num=redbot.IfNewMessage()
                if num:
                    MessageList=redbot.GetListContent(redbot.GetMessageList(num))
                    for item in MessageList:
                        word_list=item["msgcontent"]
                        #jieba_list=jieba.cut(MsgContent)
                        #word_list=[]
                        if u"打开" in word_list:
                            Com=0
                        if u"关闭" in word_list:
                            Com=1
                        if u"电灯" in word_list or u"灯" in word_list:
                            Com+=1
                        if u"风扇" in word_list or u"电风扇" in word_list:
                            Com+=3
                        if u"空调" in word_list:
                            Com+=5
                        if u"预警" in word_list:
                            Com+=7
                        print Com
                        r.lpush("mycommand",str(Com))
                        print word_list
                gevent.sleep(1)
        except Exception:
                 gevent.sleep(1)
if __name__ == '__main__':
        redbot=wx("redbot","xredcn123")
        redbot.LogWX()
        ListenMessage(redbot)
