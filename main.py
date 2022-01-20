import os
import json
import datetime as dt
import sys
import discord
from discord.ext import tasks
import log
import notif
from command import typeselect

with open("./.token",'r',encoding="utf-8") as f:
    TOKEN=f.readline()
LOG='./sq.log'
SERVER='./server.json'

if __name__=="__main__":
    server_id=None
    channel_id=None
    channel_sent=None
    args=sys.argv
    if(len(args)>=2):
        #print(args)
        if(args[1].isdigit()):
            server_id=args[1]
            print(server_id)
            with open(SERVER,"r",encoding="utf-8") as f:
                df=json.load(f)
                for s_line in df:
                    print(s_line)
                    if(str(s_line["server id"])==str(server_id)):
                        print("server name:"+s_line["server name"])
                        channel_id=s_line["channel id"]
                        break
                    else:   pass
        else:
            log.serious_error(LOG,"main.py/__main__","Argument is not digit")
            quit()
    else:
        log.serious_error(LOG,"main.py/__main__","Arguments are too short")
        quit()

    client=discord.Client()

    @tasks.loop(seconds=300)
    async def loop_notif():
        try:
            notif.connect_test()
        except Exception as e:
            log.serious_error(LOG,"main.py/__main__/Exception;",e)
            quit()
        else:
            print("connected")
            Sendlist=notif.notif()
            await client.wait_until_ready()
            for _ in Sendlist:
                await channel_sent.send(_)
        return

    @client.event
    async def on_ready():
        global channel_sent
        channel_sent=client.get_channel(channel_id)
        print("id:",channel_id)
        print("st:",channel_sent)
        Log=str(dt.datetime.now())+";"
        log.output_log(LOG,Log+"system;main.py/on_ready;Bot is login;"+str(channel_id))
        print("login:"+str(server_id)+","+str(channel_id))
        loop_notif.start()

    @client.event
    async def on_message(message):
        print(message.channel)
        M=[]
        
        print(M)
        Log="\t"+str(dt.datetime.now())+";"
        try:
            d=message.content
        except Exception as e:
            log.output_log(LOG,Log+"error;main.py/__main__/on_message/Exception;"+str(e))
            print("error")
            print(e)
        else:
            #print(d[0])
            if(d[0]=='/'):  pass
            elif message.author.bot:    return
            else:   return
            
            log.output_log(LOG,Log+"command;main.py/__main__/on_message;Get message is '"+str(d)+"'")
            print(d)
            Log+="send;main.py/__main__/on_message"
            
            mes=typeselect(d[0])
            await channel_sent.send(mes)
            log.output_log(LOG,Log+";Send message is "+mes.replace("\n","&&"))
            print(mes)
            return
    
    try:
        client.run(TOKEN)
    except Exception as e:
        log.serious_error(LOG,"main.py/__main__/Exception;",e)
        quit()