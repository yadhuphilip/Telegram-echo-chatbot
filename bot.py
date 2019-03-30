import requests
import json

update_id = None
token=""  #type in your api token  in here
base_link =  "https://api.telegram.org/bot{}/".format(token)
link = "https://api.telegram.org/bot{}/getUpdates?timeout=50".format(token)

def botmain(offset):
    if offset:
        new_link=link+"&offset={}".format(offset + 1)
        ret = requests.get(new_link)
    else:
        ret =  requests.get(link)
    return json.loads(ret.content)


def send_reply(msg,client):
    this_link = base_link+"sendMessage?chat_id={}&text={}".format(client,msg)
    if msg and client:
        requests.get(this_link)
    else:
        pass
while True:
    to_check = botmain(update_id)
    to_check = to_check["result"]
    if to_check:
        for every_item in to_check:
            update_id = every_item["update_id"]
             
            if every_item["message"]["text"]:
                message = every_item["message"]["text"]
                client = every_item["message"]["from"]["id"]

                send_reply(message,client)
    