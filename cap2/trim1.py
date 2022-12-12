import cv2
import os

cap = cv2.VideoCapture('full.mp4')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
count=int(count)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FPS))
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(cap.isOpened())
# True
print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 0.0
print(cap.get(cv2.CAP_PROP_POS_MSEC))
# 0.0

def save_frame(cap, frame_num, result_path):
    if not cap.isOpened():
        return

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

    ret, frame = cap.read()

    if ret:
        cv2.imwrite(result_path, frame)

def cut(input_filename, output_filename, x, y, width=1200, height=675):
    
    #インプット画像を指定の大きさに（デフォルト：1200×675）に切り取りする。
    
    #画像の読み込み
    img = cv2.imread(input_filename) 

    #インプット画像のサイズを変数に入れる
    i_height = img.shape[0]
    i_width = img.shape[1]

    # #切り取る部分の左上の頂点を決める
    # i = int((i_height-height)/2)
    # j = int((i_width-width)/2)

    #頂点から指定のサイズでスライスし、画像を書き出す
    img2 = img[x:x+height, y:y+width]
    cv2.imwrite(output_filename, img2)

ret, frame = cap.read()


for i in range(0,count,6):
    save_frame(cap, i//6, str(i//6)+".jpg")

for i in range(0,count,6):
    cut(str(i//6)+".jpg", str(i//6)+"_t.jpg", 245, 500, width=120, height=148)

for i in range(0,count,6):
    os.remove(str(i//6)+".jpg")