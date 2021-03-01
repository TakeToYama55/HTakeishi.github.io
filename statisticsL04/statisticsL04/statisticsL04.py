import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

print("1.分析結果 2.分析結果の視覚化 3.回帰直線 4.ヒートマップ=>",end="")
num = int(input().strip())

ef = os.path.exists('../../python_statistics_basic/data/ch2_scores_em.csv')
if(ef == False):
    print("fileなし！")
    sys.exit(0)

df = pd.read_csv('../../python_statistics_basic/data/ch2_scores_em.csv',index_col ='生徒番号')

if num == 1:
    en_scores = np.array(df["英語"][:10])
    ma_scores = np.array(df["数学"][:10])

    scores_df = pd.DataFrame({"英語":en_scores,"数学":ma_scores},index=pd.Index(["A","B","C","D","E","F","G","H","I","J"],name="生徒"))

    print(scores_df)

    summary_df = scores_df.copy()

    summary_df["英語の偏差"] = summary_df["英語"] - summary_df["英語"].mean()
    summary_df["数学の偏差"] = summary_df["数学"] - summary_df["数学"].mean()
    summary_df["偏差同士の積"] = summary_df["英語の偏差"] * summary_df["数学の偏差"]

    print(summary_df)

    print("\n偏差同士の積:",end="")
    print(summary_df["偏差同士の積"].mean())

    cov_mat = np.cov(en_scores,ma_scores,ddof=0)
    print("\n共分散行列:",end="")
    print(cov_mat)

    print("\n共分散:",end="")
    print(cov_mat[0,1],cov_mat[1,0])

    print("\n英語の分散:",end="")
    print(cov_mat[0,0])

    print("\n数学の分散:",end="")
    print(cov_mat[1,1])

    emb = np.var(en_scores,ddof=0),np.var(ma_scores,ddof=0)

    em_p = np.cov(en_scores,ma_scores,ddof=0)[0,1] / (np.std(en_scores) * np.std(ma_scores))
    print("\n英語と数学の分散:",end="")
    print(em_p)

    print("\n相関行列:",end="")
    print(np.corrcoef(en_scores,ma_scores))

    print("\nDataFrameの相関行列:",end="")
    print(scores_df.corr())

    sys.exit(0)

elif num == 2:
    english_scores = np.array(df["英語"])
    math_scores = np.array(df["数学"])

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)

    # 散布図
    ax.scatter(english_scores,math_scores)

    ax.set_xlabel("英語")
    ax.set_ylabel("数学")

    plt.show()

    sys.exit(0)

elif num == 3:
    en_scores = np.array(df["英語"])
    ma_scores = np.array(df["数学"])

    poly_fit = np.polyfit(en_scores,ma_scores,1)

    poly_1d = np.poly1d(poly_fit)

    xs = np.linspace(en_scores.min(),en_scores.max())

    ys = poly_1d(xs)

    fig = plt.figure(figsize=(8,8))
    ax2 = fig.add_subplot(111)
    ax2.set_xlabel("英語")
    ax2.set_ylabel("数学")
    ax2.scatter(en_scores,ma_scores,label="点数")
    ax2.plot(xs,ys,color="gray",label=f'{poly_fit[1]:.2f} + {poly_fit[0]:.2f}x')

    ax2.legend(loc="upper left")

    plt.show()

    sys.exit(0)

elif num == 4:
    enscores = np.array(df["英語"])
    mascores = np.array(df["数学"])

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)

    c = ax.hist2d(enscores,mascores,bins=[9,8],range=[(35,80),(56,95)])

    ax.set_xlabel(c[1])
    ax.set_ylabel(c[2])

    fig.colorbar(c[3],ax=ax)
    plt.show()

    sys.exit(0)
