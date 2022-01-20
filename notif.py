#!
# -*- coding: utf-8 -*-
"""
# Webスクレイピングbot
# 最終目標:配信の通知を行うbot
# 仕様:5分毎に対象のユーザページを取得し、更新があれば出力する(詳細未定)
# 運用環境:RaspberryPi4(予定)
# その他:対象ユーザのパターンを学習し、良く配信する時間帯に頻繁にデータを取得する機能。
# 
"""


import os 
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary
import json
import datetime as dt
import log

URL="https://www.mirrativ.com/"    #ミラティブ
USERLIST=[]    #配信者のIDと名前
LIST = './userlist.json'
LOG='./sq.log'

tags=["</a","</span","<span","</p","</h2","[","]","\u3000"]


def connect_test():
    request.Request('https://discord.com')

def sq(num):
    url=URL+"user/"+str(USERLIST[num]["ID"])
    driver=webdriver.Chrome()
    driver.get(url)
    res=driver.page_source
    soup=BeautifulSoup(res,"html.parser")
    driver.quit()
    return soup

def get_Livelist(soup):
    LiveList=soup.find_all("span",class_="_1l3YJQwq4_n_uSDBFFwGB8")
    h2=[]
    for s in LiveList:
        h2.append(s.select('h2'))
    
    lst=[]
    for t in h2:
        t2=str(t)
        t2=html_del_tags(tags,t2)
        t2=t2.split(">")
        del t2[3:]
        lst.append(t2)

    return(lst)

def get_name_dy(soup):
    lst=soup.find("p",class_="m-user-name")
    lst=html_del_tags(tags,str(lst))
    lst=lst.split(">")
    name=lst[1]
    return(name)

def html_del_tags(taglist,s):
    for tag in taglist:
        s=s.replace(tag,"")
    return s

def make_link(LiveList,num):
    url=URL+str(USERLIST[num]["ID"])

    link=LiveList[0][1].replace('"',"")
    link=link.replace("<a href=","")
    url=url+link
    return(url)

def input_USERLIST():
    global USERLIST
    with open(LIST,'r',encoding="utf-8") as f:
        df=json.load(f)
    for _ in df:
        if(_ in USERLIST):  pass
        else:   USERLIST.append(_)

def get_USERLIST():
    input_USERLIST()
    dm=""
    for _ in USERLIST:
        #print(_)
        dm+=str(_)+"\n"
        #print(dm)
    return(dm)

def notif():
    log.output_log(LOG,"\t"+str(dt.datetime.now())+";system;notif.py/__main__;call notif.py")
    print("call notif.py/notif")
    input_USERLIST()
    sendlist=[]
    global USERLIST
    for i in range(len(USERLIST)):
        ID=USERLIST[i]["ID"]
        Livelist=[]
        dt_now=dt.datetime.now()
        Log="\t\t"+str(dt_now)+";"
        Message=[ID]
        try:
            soup=sq(i)
            name=get_name_dy(soup)
            Livelist=get_Livelist(soup)
        except IndexError:
            print("error")
            print("list index out of range")
            Message.append("list index out of range")
            Log+="error;notif.py/__main__/Exception;"+str(Message)
        except Exception as e:
            quit(e)
        else:
            url=make_link(Livelist,i)
            if(log.log_match(LOG,url,ID)):
                st=(str(name)+"さんが配信を始めました！\n"+str(Livelist[i][2])+"\n"+str(url))
                print(st)
                Message.append(str(name))
                Message.append(str(url))
                Log+="start;notif.py/__main__;"+str(Message)
                sendlist.append(st)
            else:
                continue
        log.output_log(LOG,Log)
    return(sendlist)

if __name__=="__main__":
    #log.output_log(LOG,"\t"+str(dt.datetime.now())+";system;notif.py/__main__;call notif.py")
    print("call notif.py")
    input_USERLIST()
    for i in range(len(USERLIST)):
        ID=USERLIST[i]["ID"]
        Livelist=[]
        dt_now=dt.datetime.now()
        Log="\t\t"+str(dt_now)+";"
        Message=[ID]
        try:
            soup=sq(i)
            name=get_name_dy(soup)
            Livelist=get_Livelist(soup)
        except Exception as e:
            print("error")
            print(e)
            Message.append(str(e))
            Log+="error;notif.py/__main__/Exception;"+str(Message)
        else:
            url=make_link(Livelist,i)
            print("URL:"+url)
            if(log.log_match(LOG,url,ID)):
                st=(str(name)+"さんが配信を始めました！\n"+str(Livelist[i][2])+"\n"+str(url))
                print(st)
                Message.append(str(name))
                Message.append(str(url))
                Log+="start;notif.py/__main__;"+str(Message)
            else:
                continue
        #log.output_log(LOG,Log)
    """
    #for _ in Livelist:
    #    print(_)
    """
