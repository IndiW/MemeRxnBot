from fbchat import Client
from fbchat.models import * 
from itertools import islice

#Replies to memes and urls with a laughing 
#Replies to certain messages with a gif
#replace xxx with chat id
class RxnBot(Client):
    def onMessage(self,author_id,message_object,thread_id,thread_type,**kwards):
        words = ["lmao","LOL","haha","LMAO"]
        if author_id != self.uid:
            if message_object.text in words and thread_id == "xxx":
                print(message_object.text)
                client.send(Message(text="LMAOO"), thread_id="xxx", thread_type=ThreadType.USER)
                print(client.fetchMessageInfo(message_object,thread_id="xxx"))

username = input("Username: ")
password = input("Password: ")


client = RxnBot(username,password)
client.listen()

print(client.isLoggedIn())



#groups = client.searchForUsers(")
#message_id = client.send(Message(text="test"),thread_id="xxx",thread_type=ThreadType.GROUP)
#client.send(Message(text="Hi me!"), thread_id=client.uid, thread_type=ThreadType.USER)
#messages = client.fetchThreadMessages(thread_id="xxx",limit = 5)
#messages.reverse()
#for message in messages:
#    print(type(message.text))
#images = client.fetchThreadImages("xxx")
#for image in islice(images,2):
#    print(image.large_preview_url)

if client.isLoggedIn():
    client.logout()
    #print(client.isLoggedIn())
    print("Logged Out")

