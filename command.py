import json
from notif import get_USERLIST

COMMAND='./command.json'
README='./readme.md'

comlist=[]

def sort_COMMAND():
    pass

def input_COMMAND():
    global comlist
    with open(COMMAND,'r',encoding="utf-8") as f:
        df=json.load(f)
        for _ in df:
            comlist.append(_)

def List_com():
    ret=get_USERLIST()
    return(ret)

def Help_com():
    global comlist
    ret="help\n"
    for e in comlist:
        ret=ret+str(e['message']+":"+e['explan']+"\n")
    return(ret)

def Readme_com():
    ret=""
    with open(README,'r',encoding="utf-8") as f:
        for line in f:
            ret=ret+line.replace("<br>","")
    return(ret)

def funcselect(com):
    if(com=="/help"):
        return(Help_com())
    elif(com=="/list"):
        return(List_com())
    elif(com=="/readme"):
        return(Readme_com())

def typeselect(com):
    input_COMMAND()
    global comlist
    for c in comlist:
        if c["message"]==com:
            t=c["type"]
            if(t=="message"):
                #print("mess")
                return(c["return"])
            elif(t=="function"):
                #print("func")
                return(funcselect(com))
            else:
                return(False)
    return("not defined")

if __name__=="__main__":
    while(True):
        print("終了する場合は'end'と入力してください")
        s=input("input command:")
        if(s=="end"):   break
        print(typeselect(s))