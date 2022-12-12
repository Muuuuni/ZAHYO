# https://qiita.com/yoshi_yast/items/bd5e1e91ac9f64157203

import requests
import base64
import json

GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='
API_KEY = 'APIキーを設定する'

# APIを呼び、認識結果をjson型で返す
def request_cloud_vison_api(image_base64):
    api_url = GOOGLE_CLOUD_VISION_API_URL + API_KEY
    req_body = json.dumps({
        'requests': [{
            'image': {
                # jsonに変換するためにstring型に変換する
                'content': image_base64.decode('utf-8')
            },
            'features': [{
                # ここを変更することで分析内容を変更できる
                'type': 'TEXT_DETECTION',
                'maxResults': 10,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    return res.json()

# 画像読み込み
def img_to_base64(filepath):
    with open(filepath, 'rb') as img:
        img_byte = img.read()
    return base64.b64encode(img_byte)

# 文字認識させたい画像を設定
img_base64 = img_to_base64('340_trimmed.jpg')
result = request_cloud_vison_api(img_base64)
# 認識した文字を出力
text_r = result["responses"][0]["textAnnotations"][1]["description"]
print(text_r)