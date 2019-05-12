from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
import requests 
import time
from datetime import datetime
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_id = 49631
api_hash = 'fb050b8f6771e15bfda5df2409931569'

client = TelegramClient('session_name', api_id, api_hash)


s = requests.session()


print("~ Amin Tamvan ~")
print("\n")
print("List username bot ada disini : http://link.akuno.net/FziLTaW0")
print(" ")
print(" ")
uname = input("masukan username bot dogeclick : ")
print(" ")
print(" ")

try:
    client.start()
        # print("signed as",client.get_me().stringify())
        # client.get_messages('@Zcash_click_bot', 100)
    channel_username=uname # your channel
    channel_entity=client.get_entity(channel_username)
    url = ""
    for i in range(5000000):
        now = datetime.now()
        tim = now.strftime("%H:%M:%S")

        posts = client(GetHistoryRequest(
                peer=channel_entity,
                limit=1,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            )
        )
        messageId = posts.messages[0].id
        # time.sleep(5)
        
        if posts.messages[0].message.find("to earn") != -1:
            url = posts.messages[0].reply_markup.rows[0].buttons[0].url
            res = s.get(posts.messages[0].reply_markup.rows[0].buttons[0].url, verify=False,timeout=5)
            res.close()
            
            if res.text.find("reCAPTCHA") == -1:
                # print(posts.messages[0].reply_markup)
                t = "Try to visit url"
                print('['+tim+']', t)
            else:
                client(GetBotCallbackAnswerRequest(
                channel_username,
                messageId,
                data=posts.messages[0].reply_markup.rows[0].buttons[1].data
                ))
                t = "captcha required, skipped."
                print('['+tim+']', t)
        elif posts.messages[0].message.find("You earned") != -1:
            print('['+tim+']',posts.messages[0].message)
        elif posts.messages[0].message.find("You must stay on the site for") != -1:
            client.send_message(channel_username, '🖥 Visit sites')
            posts = client(GetHistoryRequest(
                    peer=channel_entity,
                    limit=1,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0
                )
            )
            messageId = posts.messages[0].id
            res1 = s.get(posts.messages[0].reply_markup.rows[0].buttons[0].url, verify=False,timeout=5)
            
            if res1.text.find("reCAPTCHA") == -1:
                res = s.get(posts.messages[0].reply_markup.rows[0].buttons[0].url, verify=False,timeout=5)
                soup = BeautifulSoup(res.text, "html.parser")
                print(soup)
                c = soup.div["data-code"]
                t = soup.div["data-token"]
                time.sleep(5)
                ress = s.post("https://dogeclick.com/reward", data = {"code": c, "token": t}, verify=False,timeout=5)
                
                print('['+tim+']', ress.text)
            else:
                client(GetBotCallbackAnswerRequest(
                channel_username,
                messageId,
                data=posts.messages[0].reply_markup.rows[0].buttons[1].data
                ))
                t = "captcha required, skipped."
                print('['+tim+']', t)
        elif posts.messages[0].message.find("Sorry, there are no new ads available") != -1:
            print('['+tim+']', "No ads anjay ? ads nya habis anjay ? tunggu aja anjay ?")
            client.send_message(channel_username, '🖥 Visit sites')
        elif posts.messages[0].message.find("Please stay on the site for at least") != -1:
            time.sleep(5)
        else:
            # client.send_message('@Zcash_click_bot', '🖥 Visit sites')
            print
    print("\n")
        
    
    # client.send_message('@Zcash_click_bot', '🖥 Visit sites')
finally:
    print("done")
    client.disconnect()