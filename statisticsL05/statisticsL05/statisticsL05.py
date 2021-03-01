" ------------第４章 推論統計 ---------------"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def filecheck(spath,iname):

    print('__file__:    ', __file__)

    ef = os.path.exists(spath)
    if(ef == False):
        print("fileなし！")
        sys.exit(0)

    return pd.read_csv(spath)

def ms1(indf,pscores):

    np.random.seed(0)
    print(np.random.choice([1,2,3],3))

    # 非復元抽出
    # np.random.choice([1,2,3],3,replace=False)

    for i in range(5):
        sample = np.random.choice(scores,20)
        print(f"{i + 1}回目の無造作で得た標本平均",sample.mean())

    print("標本データ:",end = "")
    sample = np.random.choice(pscores,1000)

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    ax.hist(sample,bins=100,range=(0,100),density=True)
    ax.set_xlim(20,100)
    ax.set_ylim(0,0.042)
    ax.set_xlabel("点数")
    ax.set_ylabel("相対度数")

    plt.show()

def ms2():
    sample_means = [np.random.choice(scores, 20).mean() for _ in range(10000)]
   # sample_means = [np.ramdom.choice(pscores,20).mean() for _ in range(10000)]

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    ax.hist(sample_means,bins=100,range=(0,100),density=True)
    
    # 母平均を縦線で表示
    ax.vlines(np.mean(scores),0,1,"gray")
    ax.set_xlim(50,90)
    ax.set_ylim(0,0.13)
    ax.set_xlabel("点数")
    ax.set_ylabel("相対度数")

    plt.show()

# 確率分布(probability distribution)
def pbb():

     dice = [1,2,3,4,5,6]
     prob = [1/21,2/21,3/21,4/21,5/21,6/21]

     # 100回実行
     num_trial = 3000
     sample = np.random.choice(dice,num_trial,p=prob)

     freq,_ =np.histogram(sample,bins=6,range=(1,7))
     print(pd.DataFrame({"度数":freq,"相対度数":freq / num_trial},index = pd.Index(np.arange(1,7),name="出目")))

     fig = plt.figure(figsize=(10,6))
     ax = fig.add_subplot(111)
     ax.hist(sample,bins=6,range=(1,7),density=True,rwidth=0.8)

     # 真の確率分布を横線で表示
     ax.hlines(prob,np.arange(1,7),np.arange(2,8),colors="gray")
     # 棒グラフの[1.5,2.5,...,6.5]の場所に目盛りをつける
     ax.set_xticks(np.linspace(1.5,6.5,6))
     # 目盛りの値は[1,2,3,4,5,6]
     ax.set_xticklabels(np.arange(1,7))
     ax.set_xlabel("出目")
     ax.set_ylabel("相対度数")

     plt.show()


gdf = filecheck("../../python_statistics_basic/data/ch4_scores400.csv","点数")
scores = np.array(gdf['点数'])
print(scores[:10])

print("1:推論統計 2:1の標本平均の分布 3:確率モデルとヒストグラム 3:推論統計のグラフ化 =>",end = "")
num = int(input().strip())

if num == 1:
    ms1(gdf,scores)
if num == 2:
    ms2()
elif num ==3:
    pbb()
else:
    print("Worng input!")
    sys.exit(0)