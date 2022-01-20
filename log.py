import datetime as dt

def output_log(dir,message):
    message+="\n"
    with open(dir,'r',encoding="utf-8") as f:
        l=f.readlines()
    l.insert(0,message)
    with open(dir,"w",encoding="utf-8") as f:
        f.writelines(l)
    return True

relist=["[","'"," ","\n","]"]
def replace_in_list(s):
    for tag in relist:
        s=s.replace(tag,"")
    return s

def log_match(dir,url,ID):
    #print("log_match")
    match=False
    with open(dir,'r',encoding="utf-8") as f:
        for s_line in f:
            line=s_line.split(";")
            if(len(line)>=2):
                if(line[1]=="start"):
                    match=True
                    s_log=replace_in_list(line[3]).split(",")
                    print(s_log)
                    print(ID)
                    if(s_log[0]==ID):
                        #print("log_match:"+s_log[2])
                        if(url!=s_log[2]):
                            return(True)
                        else:   pass
                    else:   pass
                else:   pass
            else:   pass
    if(match!=True):
        return(True)
    return(False)

def serious_error(dir,func,e):
    Log=str(dt.datetime.now())+"serious error;"+str(func)+";"+str(e)
    output_log(dir,Log)
    print("serious error")
    print(e)

if __name__=="__main__":
    pass

"""
# Log_message
# 
# datetime;type;writer_function;message;
# 
# type{
#   error:エラー
#   start:配信開始を通知
#   system:システム関係
#   command:コマンドの入力を検知
#   send:コマンドに対応したメッセージ出力
# }
# 
# 
# 
# 
# 
# 
# 
#  
# 
"""