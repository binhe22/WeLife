#coding:utf8
import os
#from gevent import monkey; monkey.patch_all()
import redis
import sqlite3
import gevent
from gevent.pywsgi import WSGIServer
import json
from hashlib import md5
import time
#import redisv2
import datetime
import pymongo
from wxhack import *
import jieba
import warning
def return_params(raw_string):
    raw_string=raw_string.split("&")
    params_format={}
    for item in raw_string:
        item=item.split('=')
        print item
        params_format[item[0]]=item[1]
    return params_format

def insert_img(params):
    img=open("temp.jpg","wb")
    img.write(params)
    img.close()
    warning.sendmail()
    return 1

def insert_data(params):
    try:
        print params
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)
        com=r.lpop("mycommand")
        if not com:
            return "0"
        return com
    except Exception,e:
        print str(e)
        return "0"

def http_server(environ, start_response):
        print  "http"
        status = '200 OK'
        headers = [
        ('Content-Type', 'application/json') #设定网络文件的类型是json
        ]#put the http header here
        start_response(status,headers)
        #print environ
        print environ
        handle_way=environ["PATH_INFO"][1:]
        print handle_way
        print environ
        print environ["QUERY_STRING"]
        if handle_way=="img":
            try:
                if insert_img(environ['wsgi.input'].read()):
                    return "0"
                else:
                    return "-1"
            except Exception,e:
                return str(e)
        if handle_way=="request":
           try:
               return insert_data(return_params(environ['QUERY_STRING']))
           except Exception,e:
                return str(e)



def  Start_httpserver ():
    WSGIServer(('', 8000), http_server).serve_forever()

def main():
    	Start_httpserver()

if __name__ == '__main__':
        main()


