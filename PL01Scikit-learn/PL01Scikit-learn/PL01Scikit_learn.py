from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print("\n------------- and -----------------\n")
# 学習用のデータと結果の準備
# X,Y
learn_data1 = [[0,0],[1,0],[0,1],[1,1]]
# X and Y
learn_label1 = [0,0,0,1]

# アルゴリズムの指定(LinearSVC)
clf1 = LinearSVC()

clf1.fit(learn_data1,learn_label1)

test_data1 =[[0,0],[1,0],[0,1],[1,1]]
test_label1= clf1.predict(test_data1)

print(test_data1,"の予測結果(and):",test_label1)
print("正解率 = " , accuracy_score([0,0,0,1],test_label1))

print("\n------------- xor -----------------\n")
# 学習用のデータと結果の準備
# X,Y
learn_data2 = [[0,0],[1,0],[0,1],[1,1]]
# X and Y
learn_label2 = [0,1,1,0]

# アルゴリズムの指定(LinearSVC)
clf2 =  KNeighborsClassifier(n_neighbors = 1)

clf2.fit(learn_data2,learn_label2)

test_data2 =[[0,0],[1,0],[0,1],[1,1]]
test_label2 = clf2.predict(test_data2)

print(test_data2,"の予測結果(xor):",test_label2)
print("正解率 = " , accuracy_score([0,1,1,0],test_label2))
