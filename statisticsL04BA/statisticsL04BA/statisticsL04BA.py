import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Anscom(anscombe_data):

    print(anscombe_data[0])

    stats_df = pd.DataFrame(index=["xの平均","xの分散","yの平均","yの分散","xとyの相関係数","xとyの回帰直線"])

    for i, data in enumerate(anscombe_data):
        dataX = data[:,0]
        dataY = data[:,1]
        poly_fit = np.polyfit(dataX,dataY,1)
        stats_df[f'data{i+1}'] = \
                                    [f"{np.mean(dataX):.2f}",f"{np.var(dataX):.2f}",
                                     f"{np.mean(dataY):.2f}",f"{np.var(dataY):.2f}",
                                     f"{np.corrcoef(dataX,dataY)[0,1]:2f}",f"{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x"]

    print(stats_df)

def Sanpu(anscombe_data):

    flg,axes = plt.subplots(nrows=2,ncols=2,figsize=(19,19),sharex=True,sharey=True)
    xs = np.linspace(0,30,100)

    for i,data in enumerate(anscombe_data):
        poly_fit =np.polyfit(data[:,0],data[:,1],1)
        poly_1d = np.poly1d(poly_fit)
        ys = poly_1d(xs)

        # 描画する領域の選択
        ax = axes[i//2,i%2]
        ax.set_xlim([4,20])
        ax.set_ylim([3,13])

        #タイトルをつける
        ax.set_title(f"data{i + 1}")
        ax.scatter(data[:,0],data[:,1])
        ax.plot(xs,ys,color = "gray")

    plt.tight_layout()
    plt.show()

#" start
ef = os.path.exists("../../python_statistics_basic/data/ch3_anscombe.npy")
if(ef == False):
    print("fileなし！")
    sys.exit(0)
print("1.アンコスム 2.散布図　=>",end="")
num = int(input().strip())

anscombe_data = np.load("../../python_statistics_basic/data/ch3_anscombe.npy")
print(anscombe_data.shape)

if num == 1:
    Anscom(anscombe_data)
elif num == 2:
    Sanpu(anscombe_data)
else:
    print("wrong input param!")