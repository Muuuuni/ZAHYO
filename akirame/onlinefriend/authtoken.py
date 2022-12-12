from requests.auth import HTTPBasicAuth

USER     = "your-user-name"
PASSWORD = "your-password"

url = "{}/auth/user".format(API_BASE)
response = requests.get(url, 
                        params={"apiKey": apiKey},
                        auth=HTTPBasicAuth(USER, PASSWORD))
# token = json.loads(response.text)["authToken"] # "authcookie_[UUID]" みたいなのが返ってくる
token = response.cookies["auth"] # (API変更のためCookieからauthTokenを取得、2018/7/8追記)

