import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

print('__file__:    ', __file__)

ef = os.path.exists('../../python_statistics_basic/data/ch2_scores_em.csv')
if(ef == False):
    print("fileなし！")
    sys.exit()

df = pd.read_csv('../../python_statistics_basic/data/ch2_scores_em.csv',index_col ='生徒番号')

#print(df.shape)  #データの大きさ

scores = np.array(df['英語'])[:10]

scores_df = pd.DataFrame({"点数": scores},index=pd.Index(['A','B','C','D','E','F','G','H','I','J'],name="生徒"))

print(scores_df)

# avr = sum(scores) / len(scores)
# print("平均:",end="")
# print(avr)
#!!!!!!もっと簡単な方法!!!!!
print("平均:",end="")
print(np.mean(scores))

onk = int(input())
if onk != 1:
    retrun

print("\n(2)中央値-------------------------------------------\n")
print("・データ数nが奇数なら(n+1)/2番目のデータが中央値\n")
print("・データ数nが偶数ならn/2番目のデータとn/2+1番目のデータの平均が中央値\n")

sorted_scores = np.sort(scores)
#print("中央値:",end="")
#print(sorted_scores)

#n = len(sorted_scores)
#if n % 2 == 0:
#    m0 = sorted_scores[n // 2 - 1]
#    m1 = sorted_scores[n // 2]
#    median = (m0 + m1) / 2
#else:
#    median = sorted_scores[(n + 1)  // 2 -1]

#print("中央値:",end="")
#print(median)

#!!!!!!もっと簡単な方法!!!!!
print("中央値:",end="")
#print(np.median(scores))

#!!!!!!メソッドを用いた別のやり方!!!!!
print(scores_df.median())

onk = int(input())
if onk != 1:
    retrun

print("\n(3)最頻値-------------------------------------------\n")
print("・データの中で最も多く出現する値のこと。ただしデータが全て異なる値の場合全ての値が最頻値になってしまう\n")

mh =pd.Series([1,1,1,2,2,3]).mode()

print("最頻値:",end="")
print(mh)

print("\n(4)分散と標準偏差 P17　～---------------------------\n")

mean = np.mean(scores)
deviation = scores - mean
print(deviation)

another_scores = [50,60,58,54,51,56,57,53,52,59]
another_mean = np.mean(another_scores)
another_deviation = another_scores - another_mean

print(another_deviation)

print("\n")

summary_df = scores_df.copy()
summary_df['偏差'] = deviation
print(summary_df)

print("\n")

print(summary_df.mean())

print(np.mean(deviation ** 2))

#nmpy版
#np.var(scores)

summary_df["偏差２乗"] = np.square(deviation)
print(summary_df)
print(summary_df.mean())

print("分散ルート:",end="")

#nmpy版
#np.std(scores,ddod=0)

print(np.sqrt(np.var(scores,ddof = 0)))

print("範囲:",end="")
print(np.max(scores) - np.min(scores))


print("\n四部位範囲:",end="")

scores_Q1 = np.percentile(scores,25)
scores_Q3 = np.percentile(scores,75)
scores_IQR = scores_Q3 - scores_Q1
print(scores_IQR)

print("\n--------------\n",end="")
print(pd.Series(scores).describe())

onk = int(input())
if onk != 1:
    retrun

print("\n(5)標準化 P28　～---------------------------\n")
print("標準偏差",end="")
#z =(scores - np.mean(scores)) / np.std(scores)

z = 50 + 10 * (scores - np.mean(scores)) / np.std(scores)

scores_df["偏差値"] = z
print(scores_df)

print("\n--------------\n",end="")
english_scores = np.array(df["英語"])
print(pd.Series(english_scores).describe())

print("\n--------------\n",end="")
freq, _ = np.histogram(english_scores,bins=10,range=(0,100))
print(freq)

#0～10,10～20, ... といった文字列のリストを作る
freq_class = [f'{i}~{i+10}' for i in range(0,100,10)]
# freq_classをインデックスにしてfreqでDataFrameを作る
freq_dist_df = pd.DataFrame({"度数":freq},index=pd.Index(freq_class,name="階級"))

print("\n2度数分布表:",end="")
print(freq_dist_df)

print("\n2-1階級値（各階級の中央の値):\n",end="")
class_value = [(i+(i+10))// 2 for i in range(0,100,10)]
print(class_value)

print("\n2-2相対度数（全データに対してその階級のデータがどのくらいの割合を占めるか示す):\n",end="")
rel_freq = freq / freq.sum()
print(rel_freq)

print("\n2-3累積相対度数（その階級までの相対度数の和を示す):\n",end="")
cum_rel_freq = np.cumsum(rel_freq)
print(cum_rel_freq)

print("\n2-1～2-3まとめ\n",end="")

freq_dist_df["階級値"] = class_value
freq_dist_df["相対度数"] = rel_freq
freq_dist_df["累積相対度数"] = cum_rel_freq

freq_dist_df = freq_dist_df[["階級値","度数","相対度数","累積相対度数"]]
print(freq_dist_df)

print("\n最頻値:",end=""
      )
print(freq_dist_df.loc[freq_dist_df["度数"].idxmax(),"階級値"])


print("\n(6)ヒストグラム P34　～---------------------------\n")

flg = plt.figure(figsize=(10,6))

ax = flg.add_subplot(111)

freq, _, _ =ax.hist(english_scores,bins=10,range=(0,100))

ax.set_xlabel("点数")
ax.set_ylabel("人数")

ax.set_xticks(np.linspace(0,100,10+1))

ax.set_yticks(np.arange(0,freq.max()+1))

plt.show()

onk = int(input())
if onk != 1:
    retrun
