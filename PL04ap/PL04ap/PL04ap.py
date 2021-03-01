import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.utils import all_estimators
import warnings
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import os

def Filecheck(spath,demilit):

    print('__file__:    ', __file__)

    ef = os.path.exists(spath)
    if(ef == False):
        print("fileなし！")
        sys.exit(0)
    else:
        data_array = pd.read_csv(spath, sep= demilit,encoding="utf-8")
        return data_array

def Salgorithm(iris_data):

    # アヤメデータをラベルと入力データに分離
    y = iris_data.loc[:,"Name"]
    x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

    # 学習用とテスト用に分離する
    x_train,X_test,y_train,Y_test = train_test_split(x,y,test_size = 0.2,train_size = 0.8,shuffle = True)

    # classifierのアルゴリズムすべてを取得する
    warnings.filterwarnings("ignore")
    allAlgorithms = all_estimators(type_filter="classifier")

    for(name,algorithm) in allAlgorithms:
        try :
            # 各アリゴリズムのオブジェクトを作成
            clf = algorithm()

         # 学習して、評価する
            clf.fit(x_train, y_train)
            y_pred = clf.predict(X_test)
            print(name,"の正解率 = " , accuracy_score(Y_test, y_pred))
  
            # WarningやExceptionの内容を表示する
        except Warning as w :
            print("\033[33m"+"Warning："+"\033[0m", name, ":", w.args)
        except Exception as e :
            #print("\033[31m"+"Error："+"\033[0m", name, ":", e.args)
            pass

def Cvalidation(iris_data):

    y = iris_data.loc[:,"Name"]
    x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

    # classifierのアルゴリズムすべてを取得する
    warnings.filterwarnings("ignore")
    allAlgorithms = all_estimators(type_filter="classifier")

    # K分割クロスバリテーション用オブジェクト
    kfold_cv = KFold(n_splits=5, shuffle=True)

    for(name,algorithm) in allAlgorithms:
        
        try :
           # 各アリゴリズムのオブジェクトを作成
            if(name == "LinearSVC") :
                clf = algorithm(max_iter = 10000)
            else:
                clf = algorithm()

            # scoreメソッドを持つクラスを対象とする
            if hasattr(clf,"score"):
        
            # クロスバリデーションを行う
                scores = cross_val_score(clf,x,y,cv=kfold_cv)
                print(name,"の正解率=")
                print(scores)
        except Exception as e :
            pass

def gridSearch(iris_data):

    ## 学習用とテスト用に分離する
    #y = iris_data.loc[:,"Name"]
    #x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

    ## 学習用とテスト用に分離する
    #x_train,X_test,y_train,Y_test = train_test_split(x,y,test_size = 0.2,train_size = 0.8,shuffle = True)

    ## グリッドサーチで利用するパラメータを指定
    #parameters = [
    #        {"C":[1,10,100,100],"kernel":["linear"]},
    #        {"C":[1,10,100,100],"kernel":["rbf"],"gamma":[0.001,0.0001]},
    #        {"C":[1,10,100,100],"kernel":["sigmold"],"gamma": [0.001,0.0001]}
    #]

    ##グリッドサーチを行う
    #kfold_cv = KFold(n_splits=5, shuffle=True)
    #clf = GridSearchCV(SVC(),parameters,cv=kfold_cv)
    #clf.fit(x_train,y_train)
    #print("最適なパラメータ　=",clf.best_estimator_)

    ## 最適なパラメータで評価
    #y_pred = clf.predict(X_test)
    #print("評価時の正解率 = ",accuracy_score(Y_test,y_pred))
    # アヤメデータをラベルと入力データに分離する
    y = iris_data.loc[:,"Name"]
    x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

    # 学習用とテスト用に分離する 
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, train_size = 0.8, shuffle = True)

    # グリッドサーチで利用するパラメータを指定 --- (*1)
    parameters = [
        {"C": [1, 10, 100, 1000], "kernel":["linear"]},
        {"C": [1, 10, 100, 1000], "kernel":["rbf"], "gamma":[0.001, 0.0001]},
        {"C": [1, 10, 100, 1000], "kernel":["sigmoid"], "gamma": [0.001, 0.0001]}
    ]

    # グリッドサーチを行う --- (*2)
    kfold_cv = KFold(n_splits=5, shuffle=True)
    clf = GridSearchCV( SVC(), parameters, cv=kfold_cv)
    clf.fit(x_train, y_train)
    print("最適なパラメータ = ", clf.best_estimator_)

    # 最適なパラメータで評価 --- (*3)
    y_pred = clf.predict(x_test)
    print("評価時の正解率 = " , accuracy_score(y_test, y_pred))


# ---- Start -----
print("1.各アルゴリズムの正解率 2.クロスバリエーション　3.グリッドサーチ=>",end="")
num = int(input().strip())

fdata = Filecheck("../../Iris-flower-dataset-master/iris.csv",",")

if num == 1: 
    Salgorithm(fdata)
elif num == 2:
    Cvalidation(fdata)
elif num == 3:
    gridSearch(fdata)
else:
    print("worng input param !")
    sys.exit(0)