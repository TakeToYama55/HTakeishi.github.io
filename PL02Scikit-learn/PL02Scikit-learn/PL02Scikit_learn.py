import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

import os

def Filecheck(spath,demilit):

    print('__file__:    ', __file__)

    ef = os.path.exists(spath)
    if(ef == False):
        print("fileなし！")
        sys.exit()
    else:
        data_array = pd.read_csv(spath, sep= demilit,encoding="utf-8")
        return data_array

def Iris(iris_data):

    # アヤメデータをラベルと入力データに分離する(サンプルデータにはヘッダ部分がなかったため付加した)
    y = iris_data.loc[:,"Name"]
    x = iris_data.loc[:,["SepalLength", "SepalWidt", "PetalLength", "PetalWidth"]]

    # 学習用とテスト用に分離する
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,train_size = 0.8, shuffle = True)

    # 学習する
    clf = SVC()
    clf.fit(x_train,y_train)

    # 評価する
    y_pred = clf.predict(x_test)

    print("正解率 = " , accuracy_score(y_test,y_pred))

def Wine(wine_data):

    y = wine_data["quality"]
    x = wine_data.drop("quality",axis = 1)

    #学習用とテスト用に分離する
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

    # 学習する
    model = RandomForestClassifier()
    model.fit(x_train,y_train)

    # 評価する
    y_pred = model.predict(x_test)
    print(classification_report(y_test,y_pred))
    print("正解率=",accuracy_score(y_test,y_pred))

def Wine_rev(wine_data):

    y = wine_data["quality"]
    x = wine_data.drop("quality",axis = 1)

    # yのラベルをつけ直す
    newlist = []
    for v in list(y):
        if v <= 4:
            newlist += [0]
        elif v <= 7:
            newlist += [1]
        else:
            newlist += [2]
    y = newlist

    # 学習用とテスト用に分割する
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

    # 学習する
    model = RandomForestClassifier()
    model.fit(x_train,y_train)

    # 評価する
    y_pred = model.predict(x_test)
    print(classification_report(y_test,y_pred))
    print("正解率=",accuracy_score(y_test,y_pred))


print("1:iris  2:wine  3:wine_rev=>",end = "")
num = int(input().strip())

tdata = []

if num == 1:
    tdata = Filecheck("../../Iris-flower-dataset-master/iris.csv",",")
    Iris(tdata)
elif num == 2:
    tdata = Filecheck("../../data/winequality-white.csv",";")
    Wine(tdata)
elif num == 3:
    tdata = Filecheck("../../data/winequality-white.csv",";")
    Wine_rev(tdata)
else:
    print("worg input!")