# k平均法
# k平均法はk-means clusteringとも呼ばれる教師なし学習の手法です
# 「距離」に基づき、データをk個のクラスタに分類します

# ・k平均法とは？
#  ・「距離」に基づき、データを「k」個のクラスタに分類する手法
#  ・クラスタ分析はデータを似たもの同士グループ分けする分析であるが、
#    「k平均法」は、このようなクラスタ分析の手法のひとつ
#  ・横軸；特徴量1、縦軸；特徴量2のデータを考える
#   ・１．各サンプルに、ランダムに「k」種類のグループのうちどれかを割り当てる
#   ・２．各グループの重心を計算する
#   ・３．各サンプルが属するグループを、一番重心が近いグループに変更する
#   ・４．変化が無くなれば終了。変化がある場合は、２．に戻る


# ・データセットの読み込み
#  ・今回は、Irisデータセットを使用します。以下はこのデータセットの説明変数です。
#   ・sepal length (cm): がくの長さ
#   ・sepal width (cm): がくの幅
#   ・petal length (cm): 花弁の長さ
#   ・petal width (cm): 花弁の幅
#  ・目的変数classは0から2の整数で、花の品種を表します。
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)  # data: 説明変数
iris_df["class"] = iris.target  # target: 目的変数
iris_df.head()
#  ・データセットの説明を表示します。
print(iris.DESCR)
#  ・各統計量を表示します。
iris_df.describe()
#  ・ライブラリseabornのpairplotにより、説明変数同士、
#    及び説明変数と目的変数の関係を一覧表示します。
import seaborn as sns
sns.pairplot(iris_df, hue="class")


# ・k平均法
#  ・以下のコードは、k平均法によりデータをグループ分けします。
#  ・品種の数に合わせて、クラスタの数を3に設定しています。
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
model.fit(iris.data)

#  ・グループ分けの結果を散布図で表示します
import matplotlib.pyplot as plt
axis_1 = 2
axis_2 = 3
# ラベルが0のグループ
group_0 = iris.data[model.labels_==0]
plt.scatter(group_0[:, axis_1], group_0[:, axis_2], c="red")
# ラベルが1のグループ
group_1 = iris.data[model.labels_==1]
plt.scatter(group_1[:, axis_1], group_1[:, axis_2], c="blue")
# ラベルが2のグループ
group_2 = iris.data[model.labels_==2]
plt.scatter(group_2[:, axis_1], group_2[:, axis_2], c="green")
plt.xlabel(iris.feature_names[axis_1])
plt.ylabel(iris.feature_names[axis_2])
plt.show()

#  ・k平均法が機能し、グループ分けが行われたように見えます。
#  ・比較のため、元のデータセットのラベルを使ってグループ分けした結果を表示します。
axis_1 = 2
axis_2 = 3
# ラベルが0のグループ
group_0 = iris.data[iris.target==0]
plt.scatter(group_0[:, axis_1], group_0[:, axis_2], c="blue")
# ラベルが1のグループ
group_1 = iris.data[iris.target==1]
plt.scatter(group_1[:, axis_1], group_1[:, axis_2], c="red")
# ラベルが2のグループ
group_2 = iris.data[iris.target==2]
plt.scatter(group_2[:, axis_1], group_2[:, axis_2], c="green")
plt.xlabel(iris.feature_names[axis_1])
plt.ylabel(iris.feature_names[axis_2])
plt.show()
#  ・グループの境界が多少異なりますが、属すべきグループを大まかに捉えていることがわかります。
