# 演習
# お好きな機械学習の手法を使って、乳がんを診断するモデルを構築しましょう

# ・データセットの読み込み
#  ・今回は、scikit-learnに含まれる乳がん診断のデータセットを使用します。
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
bc = load_breast_cancer()
bc_df = pd.DataFrame(bc.data, columns=bc.feature_names)  # data: 説明変数
bc_df["class"] = bc.target  # target: 目的変数
bc_df.head()
#  ・データセットの説明を表示します。
print(bc.DESCR)
#  ・各統計量を表示します。
bc_df.describe()
#  ・ライブラリseabornのpairplotにより、説明変数同士、
#    及び説明変数と目的変数の関係を一覧表示します。
import seaborn as sns
sns.pairplot(bc_df, hue="class")


# ・モデルの構築
#  ・まずは、データセットを訓練用のデータとテスト用のデータに分割し、標準化します。
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# 訓練データとテストデータに分割
x_train, x_test, t_train, t_test = train_test_split(bc.data, bc.target, random_state=0)
# データの標準化
std_scl = StandardScaler()
std_scl.fit(x_train)
x_train = std_scl.transform(x_train)
x_test = std_scl.transform(x_test)

# 問題
# from sklearn.svm import   # ←ここにコードを追記する
# model =   # ←ここにコードを記述する
# # モデルの訓練
#   # ←ここにコードを記述する


# 回答
from sklearn.svm import LinearSVC  # ←ここにコードを追記する
model = LinearSVC(random_state=0)  # ←ここにコードを記述する
# モデルの訓練
model.fit(x_train, t_train)  # ←ここにコードを記述する


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
