import json
import requests

API_BASE = "https://api.vrchat.cloud/api/1"

url = "{}/config".format(API_BASE)
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url=url,headers=headers)
apiKey = json.loads(response.text)["clientApiKey"] # 2018/6/16時点で "JlE5..." みたいなのが返ってくる

from requests.auth import HTTPBasicAuth

USER     = "Muunii"
PASSWORD = "00930613t="

url = "{}/auth/user".format(API_BASE)
response = requests.get(url, 
                        params={"apiKey": apiKey},
                        auth=HTTPBasicAuth(USER, PASSWORD),
                        headers=headers)
# token = json.loads(response.text)["authToken"] # "authcookie_[UUID]" みたいなのが返ってくる
token = response.cookies["auth"] # (API変更のためCookieからauthTokenを取得、2018/7/8追記)

url = "{}/auth/user/friends".format(API_BASE)
response = requests.get(url, 
                        params={"apiKey": apiKey, "authToken": token},
                        headers=headers)
friends = json.loads(response.text)
for f in friends:
    print(f["displayName"]) # オンラインなフレンド一覧を表示