import cv2
import urllib.request as req
import matplotlib.pyplot as plt

def display(img):
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.show()

def resize(img):
    gresize = cv2.resize(img,(800,300))

    plt.imshow(cv2.cvtColor(gresize,cv2.COLOR_BGR2RGB))
    plt.show()


#url = "http://uta.pw/shodou/img/28/214.png"
url ="file:///D:/Prg10/Python/PL05/PL05/test3.JPG"
#req.urlretrieve(url,"test.jpg")

print("1.画像表示 2.リサイズ　3.切り取り=>",end="")
num = int(input().strip())


# 画像を読み込む
img = cv2.imread("./test3.jpg")
#img = cv2.imread(url)
plt.axis("off")
# 画像を保存する
cv2.imwrite("D:\Prg10\Python\L05\out3.png",img)

if num == 1:
    display(img)
elif num == 2:
    resize(img)