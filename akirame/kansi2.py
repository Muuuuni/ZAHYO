import requests
import json
from urllib.parse import quote
from sys import exit
from datetime import datetime
from requests.auth import HTTPBasicAuth

def friend_logs():
    # 監視するユーザー名を記入
    user_name = "Ticm d5c3"

    # # VRCのID、PWを取得
    # credential = json.load(open('credential.json'))

    username = "Muunii"
    password = "00930613t="
    API_BASE = "https://api.vrchat.cloud/api/1"
    apiKey = 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26'# 21/05/22 時点で公開されているキー
    data = {'apiKey':apiKey}
    headers = {'User-Agent': 'Mozilla/5.0'}

    url = "{}/auth/user".format(API_BASE)
    response = requests.get(url, 
                        params={"apiKey": apiKey},
                        auth=HTTPBasicAuth(username, password),
                        headers=headers)
    # token = json.loads(response.text)["authToken"] # "authcookie_[UUID]" みたいなのが返ってくる
    token = response.cookies["auth"] # (API変更のためCookieからauthTokenを取得、2018/7/8追記)

    # auth/user/playermoderations endpoint よりmoderation情報を取得
    response = requests.get('https://api.vrchat.cloud/api/1/auth/user/friends', data=data, headers=headers, params={"authToken": token})
    moderations = response.json()
    friend_disturber_list = []

    #moderation情報より対象のlocationを取得
    instance_location = ""
    for i in (list(moderations)):
        if user_name == i["displayName"]:
            instance_location = i['location']

    if instance_location == "":
        print(111)
        return

    if instance_location != "private":
        #対象と一緒のインスタンスにいるフレンドを取得
        for i in (list(moderations)):
            if i['location'] == instance_location and i["displayName"] != user_name:
                friend_disturber_list.append(i["displayName"])

        locato = instance_location.split(":")

        #インスタンス人数、インスタンスの種類を取得
        response = requests.get('https://api.vrchat.cloud/api/1/instances/' + instance_location, data=data, headers=headers, params={"authToken": token})
        moderations = response.json()
        n_user = moderations['n_users']
        instance_type = moderations['type']
        if instance_type == "hidden":
            instance_type = "friends+"

        #ワールド名を取得
        response = requests.get('https://api.vrchat.cloud/api/1/worlds/' + locato[0], data=data, headers=headers, params={"authToken": token})
        moderations = response.json()
        world_name = moderations['name']
        #print(world_name)

        with open("players_log.txt", "a",encoding='utf-8') as opfile:
            opfile.write(u"{} {} {} {} {}\n".format(datetime.now(),world_name,n_user,instance_type,friend_disturber_list))
    else:
        with open("players_log.txt", "a",encoding='utf-8') as opfile:
            opfile.write(u"{} {}\n".format(datetime.now(),"private"))

friend_logs()