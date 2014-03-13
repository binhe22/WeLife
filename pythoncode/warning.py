#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import sendcloud
import os
# 不同于登录SendCloud站点的帐号，您需要登录后台创建发信域名，获得对应发信域名下的帐号和密码才可以进行邮件的发送。
def sendmail():
    s1 = open('warning.html').read()
    server = sendcloud.SendCloud('postmaster@lowercase.sendcloud.org', 'dJPA3KrM', tls=False) # 目前tls 不可用
    message = sendcloud.Message(("from@sendcloud.com", "来自微Life"), "家庭安全及节能预警", html=s1)
    message.add_to(["851733805@qq.com"], ["toname1"])
    message.add_attachment("现场截图", "temp.jpg")
    server.smtp.send(message)
if __name__=="__main__":
    sendmail()
