import requests
import json
from urllib.parse import quote
from sys import exit
from datetime import datetime

# 監視するユーザーリストを取得
user_file = open("online_player_list.txt", mode='r',encoding='utf-8')
user_data = user_file.read()
user_file.close()
low_user_data = eval(user_data)

# 既にオンラインで通知を送っているユーザーリスト
on_user_file = open("tmp_players.txt", mode='r',encoding='utf-8')
on_user_data = on_user_file.read()
on_user_file.close()
if on_user_data == "":
    on_low_user_data = []
else:
    on_low_user_data = on_user_data.split(",")
write_tmp = 0

username = "Muunii"
password = "00930613t="
apiKey = 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26'# 21/05/22 時点で公開されているキー
data = {'apiKey':apiKey}
headers = {'User-Agent': 'SunaFH/1.0.5'}

# APIにてフレンドリストを取得

response = requests.get('https://api.vrchat.cloud/api/1/auth/user', data=data, headers=headers, auth=username, password=password)
token = response.cookies["auth"]

response = requests.get('https://api.vrchat.cloud/api/1/auth/user/friends', data=data, headers=headers, params={"authToken": token})
moderations = response.json()

write_online = []
write_offline = []
moderations_filtered = []

for i in (list(moderations)):
    moderations_filtered.append(i['displayName'])
for a in moderations_filtered:
    if a in low_user_data:
        if a not in on_user_data:
            write_online.append(a)
            write_tmp = 1

# 繰り返して既に報告したリストへ入力する
on_low_user_data.extend(write_online)
remove_list = []

for i in on_low_user_data:
    if i in moderations_filtered:
        pass
    else:
        #print(i)
        remove_list.append(i)

# 既にログアウトしている人をオンラインリストから除外
print(type(remove_list))
if len(remove_list) >= 1:
    for i in range(len(remove_list)):
        on_low_user_data.remove(remove_list[i])

with open("tmp_players.txt", "w",encoding='utf-8') as opfile:
    opfile.write(",".join(on_low_user_data))