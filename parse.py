from BotAmino import BotAmino
from amino import client
from requests.models import Response
import websockets
import json



cli = BotAmino(email='okeka4016@gmail.com',password=input("type pass"))


def youtube(video_name=None):
    uri = VideosSearch(video_name,limit=1)
    result = uri.result()
    response = json.dumps(result)
    json_dict = json.loads(response)
    url = json_dict['result'][0]['link']
    title = json_dict["result"][0]['title']
    print(url)






print("launching")














def parse_config(data):
    return data


@client.command("join_vc")
def join_vc(args):
    args.client.start_voice_room(comId=data.comId, chatId=data.chatId)
    with websockets.connect("wss://ws1.narvii.com") as websocket:
        data = youtube(video_name=data.message)
        websocket.send(data)
        websocket.recv()
        while pass:
            print("Playing {data.title}")
        while s_end:
            github_uri = ("")
            stop_audio = (github_uri)
            websocket.send(stop_audio)


@client.command("end_vc")
def end_vc(data):
    data.client.end_voice_room(comId=data.comId, chatId=data.chatId)
    print("ended...")










parse_config()



client.launch(False)



print("init...")