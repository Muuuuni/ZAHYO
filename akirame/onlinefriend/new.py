import json
import requests
import os
import subprocess

def exec_subprocess(cmd: str, raise_error=True):
    '''
    コマンドを同期実行し、
    標準出力と標準エラー出力は最後にまとめて返却する
    raise_errorがTrueかつリターンコードが0以外の場合は例外を出す
    戻り値は3値のタプルで (標準出力(bytes型), 標準エラー出力(bytes型), リターンコード(int))
    '''
    child = subprocess.Popen(cmd, shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = child.communicate()
    rt = child.returncode
    if rt != 0 and raise_error:
        raise Exception(f"command return code is not 0. got {rt}. stderr = {stderr}")

    return stdout, stderr, rt

API_BASE = "https://api.vrchat.cloud/api/1"

url = "{}/config".format(API_BASE)
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url=url, headers=headers)
# response, err, rt = exec_subprocess(f"curl {url}")
response = response.text
# print(response)
apiKey = json.loads(response)["clientApiKey"] 
# apiKey = json.loads(response.text)["clientApiKey"] # 2018/6/16時点で "JlE5..." みたいなのが返ってくる
print(apiKey)
exit()
from requests.auth import HTTPBasicAuth

USER     = "Muunii"
PASSWORD = "00930613t="

url = "{}/auth/user".format(API_BASE)
response = requests.get(url, 
                        params={"apiKey": apiKey},
                        auth=HTTPBasicAuth(USER, PASSWORD))

# token = json.loads(response.text)["authToken"] # "authcookie_[UUID]" みたいなのが返ってくる
token = response.cookies["auth"] # (API変更のためCookieからauthTokenを取得、2018/7/8追記)