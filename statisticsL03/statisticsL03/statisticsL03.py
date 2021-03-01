import numpy as np
import pandas as pd
import os
import sys
# IPA(https://moji.or.jp/ipafont/ipaex00401/)からフォントをダウンロードして日本語化にしてmatplotlibrcの250行目あたりに
# DWしたフォントを定義(font.family : IPAexGothic) 念のためC:\Users\【ユーザー名】.matplotlib配下のjsonファイルを削除
import matplotlib.pyplot as plt

import pathlib
import matplotlib

#関数は呼び出す前に定義すること!
def Graf10(scores1,ax1):

    freq, _, _ =ax1.hist(scores1,bins=10,range=(0,100))

    ax1.set_title("IPAからフォントをダウンロードして日本語化にして 階級数10")
    ax1.set_xlabel("点数")
    ax1.set_ylabel("人数")

    ax1.set_xticks(np.linspace(0,100,10+1))
    ax1.set_yticks(np.arange(0,freq.max()+1))

    plt.show()

def Graf25(scores2,ax2):

    freq, _, _ =ax2.hist(scores2,bins=25,range=(0,100))

    ax2.set_title(" 階級数4")
    ax2.set_xlabel("点数")
    ax2.set_ylabel("人数")

    ax2.set_xticks(np.linspace(0,100,25+1))
    ax2.set_yticks(np.arange(0,freq.max()+1))

    plt.show()

def Graf25fg(scores3,ax31):

    ax32 = ax31.twinx()

    weights = np.ones_like(scores3) / len(scores3)
    rel_freq,_,_ = ax31.hist(scores3,bins=25,range=(0,100),weights=weights)

    cum_rel_freq = np.cumsum(rel_freq)
    class_value = [(i + (i + 4)) // 2 for i in range(0,100,4)]

    # 折れ線グラフの描画
    # 引数markerを'*'にすることでデータ点が*
    # 引数colorを'gray'にすることで灰色に
    ax32.plot(class_value,cum_rel_freq,ls="--",marker = "*", color = "red")
    ax32.grid(visible=False)

    ax31.set_title(" 階級数4 折れ線グラフ付")
    ax31.set_xlabel("点数")
    ax31.set_ylabel("相対度数")
    ax32.set_ylabel("累積相対度数")
    ax32.set_xticks(np.linspace(0,100,25 + 1))

    plt.show()

def Grafbox(scores4):

    flgbox = plt.figure(figsize=(5,6))
    axbox = flgbox.add_subplot(111)

    axbox.boxplot(scores4,labels=["英語"])

    plt.show()

#matprotlibのパスを表示 ------ ここから始まる --------
print(matplotlib.matplotlib_fname())

ef = os.path.exists('../../python_statistics_basic/data/ch2_scores_em.csv')
if(ef == False):
    print("fileなし！")
    sys.exit()

df = pd.read_csv('../../python_statistics_basic/data/ch2_scores_em.csv',index_col ='生徒番号')

english_scores = np.array(df["英語"])

flg = plt.figure(figsize=(10,6))
pax = flg.add_subplot(111)

print("1:10単位棒グラフ 2:4単位棒グラフ 3:4単位折れ線グラフ付グラフ　4:箱ひげ図 =>",end = "")
num = int(input().strip())

if num == 1:
    Graf10(english_scores,pax)
elif num == 2:
    Graf25(english_scores,pax)
elif num == 3:
    Graf25fg(english_scores,pax)
elif num == 4:
    Grafbox(english_scores)
else:
    print("wrong input!")
