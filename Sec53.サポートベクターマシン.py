# サポートベクターマシン

# ・サポートベクターマシン（Support Vector Machine、SVM）とは？
#  ・データを分類して、境界を決める手法である
#  ・パターン識別のための教師あり機械学習の手法である
#  ・境界は、「マージン最大化」により決定される
#    ・「マージン最大化」というアイディアに基づいているが、
#       しばしば優れたパターン識別能力を発揮する
#  ・境界は、「分類器」として機能し、データがどちらのグループに属するか判別できる
#  ・一次元の境界は、「線」で表される
#  ・二次元の境界は、「平面」で表される
#  ・三次元以上の境界は、「超平面」で表される


# ・データセットの読み込み
#  ・今回は、scikit-learnに含まれるワインのデータセットを使用します。
#  ・説明変数は様々なワインの特徴で、
#    アルコール濃度(alcohol)やリンゴ酸濃度(malic_acid)などがあります。
#  ・目的変数classは、0から2の整数でワイン品種を表します。
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
wine = load_wine()
wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)  # data: 説明変数
wine_df["class"] = wine.target  # target: 目的変数
wine_df.head()
#  ・データセットの説明を表示します。
print(wine.DESCR)
#  ・各統計量を表示します。
wine_df.describe()


# ・SVMの実装
#  ・サポートベクターマシンを使い、ワインの分類を行います。
#  ・まずは、データセットを訓練用のデータとテスト用のデータに分割します。
#  ・その上で、StandardScalerを使って標準化し、平均値が0、標準偏差が1になるようにします。
#  ・https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# 訓練データとテストデータに分割
x_train, x_test, t_train, t_test = train_test_split(wine.data, wine.target, random_state=0)
# データの標準化
std_scl = StandardScaler()
std_scl.fit(x_train)
x_train = std_scl.transform(x_train)
x_test = std_scl.transform(x_test)

#  ・今回は、線形サポートベクターマシンを使い、超平面によりデータを分類します。
#  ・fitメソッドにより訓練が行われ、超平面が決定されます。
from sklearn.svm import LinearSVC  # 線形ベクターマシン
model = LinearSVC(random_state=0)
# 全ての説明変数を使い学習
model.fit(x_train, t_train)

#  ・訓練済みのモデルを使い、訓練データ及びテストデータで予測を行います。
#  ・そして、その正解率を測定します。
from sklearn.metrics import accuracy_score
# 予測結果
y_train = model.predict(x_train)
y_test = model.predict(x_test)
print(y_train, y_test)
# 正解率
acc_train = accuracy_score(t_train, y_train)
acc_test = accuracy_score(t_test, y_test)
print(acc_train, acc_test)

#  ・テストデータのグループ分け結果を、matplotlibの散布図で表示します。
#  ・x軸をアルコール濃度、y軸をリンゴ酸濃度として、グループ分けの結果を表示しましょう。
import matplotlib.pyplot as plt
axis_1 = 0
axis_2 = 1
x = np.concatenate([x_train, x_test])
y = np.concatenate([y_train, y_test])
t = np.concatenate([t_train, t_test])
# 0にクラス分類されたグループ
group_0 = x[y==0]
plt.scatter(group_0[:, axis_1], group_0[:, axis_2], c="blue")
# 1にクラス分類されたグループ
group_1 = x[y==1]
plt.scatter(group_1[:, axis_1], group_1[:, axis_2], c="red")
# 2にクラス分類されたグループ
group_2 = x[y==2]
plt.scatter(group_2[:, axis_1], group_2[:, axis_2], c="green")
plt.xlabel(wine.feature_names[axis_1])
plt.ylabel(wine.feature_names[axis_2])
plt.show()
#  ・分類機の訓練には訓練データを使用しましたが、訓練済みの分類機はテストデータ　に対しても機能しているようです。
#  ・適切に訓練が行われれば、サポートベクターマシンの分類器は高い分類能力を発揮します。
