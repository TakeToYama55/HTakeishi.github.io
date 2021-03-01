#from sklearn.linear_modal import LinearRegression
from sklearn.linear_model import LinearRegression
from urllib.request import urlretrieve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

print("1:Colaboratory(matplotlib) 2:DownLoadファイルから 3:30度over 4:回帰分析(明日の天気予報)=>",end="")
num = int(input().strip())

if num == 1:
    urlretrieve("https://raw.githubusercontent.com/kujirahand/mlearn-sample/master/tenki2006-2016/kion10y.csv","kion10y.csv")
    print(pd.read_csv("kion10y.csv"))
elif num == 2:
    with open("../../data/data.csv",encoding="Shift_JIS") as fr:
        lines = fr.readlines()

    lines = ["年,月,日,気温,品質,均質\n"] + lines[5:]
    lines = map(lambda v: v.replace("/",","),lines)
    result = "".join(lines).strip()
   # print(result)

    with open("../../data/kion10y.csv","wt",encoding="utf-8") as fw:
        fw.write(result)
        print("saved.")
elif num == 3:
    print("---- 30度over Start ----")
elif num == 4:
    print("<<< 回帰分析(明日の天気予報) >>>")
else:
    print("wrong param!")
    exit

df = pd.read_csv("kion10y.csv",encoding="utf-8")
md = {}

#違うやり方
if num == 1:
    #　月ごとに平均を求める
    g =df.groupby(["月"])["気温"]
    gg = g.sum() / g.count()
    # 結果を出力
    print(gg)
    gg.plot()
    plt.savefig("tenki-heikin-tuki.png")
    plt.show()

    sys.exit(0) # 注意!!!!! exit(0)によって例外が発生せず正常終了になる

elif num ==2:
    # 日付ごとに気温リストにまとめる
    cnt = 0
    for i,row in df.iterrows():
        m,d,v =(int(row["月"]),int(row["日"]),float(row["気温"]))
        key = str(m) + "/" + str(d)
        if not(key in md): md[key] = []
        md[key] += [v]
        cnt += 1
        # print("cnt:",end="")
        # print(str(cnt))

    # 日付ごとに平均を求める
    avs = {}
    for key in md:
        v = avs[key] = sum(md[key]) / len(md[key])
        print("{0} : {1}".format(key,v))

    sys.exit(0)

if num == 3:

    #気温が３０度以上か調べる
    atui_bool =(df["気温"] > 30)

    # データを抜き出す
    atui = df[atui_bool]
    # 年ごとにカウント
    cnt = atui.groupby(["年"])["年"].count()

    # 出力
    print(cnt)
    cnt.plot()
    plt.savefig("tenki-over30.png")
    plt.show()

    sys.exit(0)

if num == 4:

    # データを学習用とテスト用に分割
    train_year = (df["年"] <= 2015)
    test_year = (df["年"] >= 2016)
    interval = 6

def make_data(data):
    x = [] # 学習データ
    y = [] # 結果
    temps = list(data["気温"])
    for i in range(len(temps)):
        if i < interval: continue
        y.append(temps[i])
        xa = []
        for p in range(interval):
            d = i + p - interval
            xa.append(temps[d])
        x.append(xa)
    return(x,y)

train_x,train_y = make_data(df[train_year])
test_x,test_y = make_data(df[test_year])

# 直線回帰分析を行う
lr = LinearRegression(normalize=True)
lr.fit(train_x,train_y)
pre_y = lr.predict(test_x)

# 予想の評価
diff_y = abs(pre_y - test_y)
print("average=",sum(diff_y) / len(diff_y))
print("max=",max(diff_y))

# 結果を図にプロット
plt.figure(figsize=(10,6),dpi=100)
plt.plot(test_y,c="r")
plt.plot(pre_y,c="b")
plt.savefig("tenki-kion-lr.png")
plt.show()