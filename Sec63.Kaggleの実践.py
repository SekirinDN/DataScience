# タイタニック号生存者の予測
# 「ランダムフォレスト」により、タイタニック号の生存者を予測します
# 訓練済みのモデルによる予測結果は、csvファイルに保存して提出します


# ・データの読み込み
#  ・タイタニック号の乗客データを読み込みます。
#  ・訓練データには乗客が生き残ったどうかを表す"Survived"の列がありますが、
#    テストデータにはありません。
#  ・訓練済みのモデルに、テストデータを入力して判定した結果を提出することになります。
import numpy as np
import pandas as pd
train_data = pd.read_csv("/kaggle/input/titanic/train.csv")  # 訓練データ
test_data = pd.read_csv("/kaggle/input/titanic/test.csv") # テストデータ
train_data.head()


# ・データの前処理
#  ・判定に使用可能なデータのみを取り出し、データの欠損に対して適切な処理を行います。
#  ・また、文字列などのカテゴリ変数に対しては、数値に変換する処理を行います。
#  ・以下のコードでは、訓練データ及びテストデータから判定に使える列のみを取り出しています。
test_id = test_data["PassengerId"]  # 結果の提出時に使用
labels = ["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
train_data = train_data[labels + ["Survived"]]
test_data = test_data[labels]
train_data.head()

#  ・info()によりデータの全体像を確認することができます。
#  ・Non-Null Countにより欠損していないデータの数が確認できるので、
#    データの欠損が存在する列を確認しておきます。
train_data.info()
test_data.info()

#  ・AgeとFare、Embarkedに欠損が存在します。
#  ・AgeとFareの欠損値には平均値を、Embarkedの欠損値には最頻値をあてがって対処します。
# Age
age_mean = train_data["Age"].mean()  # 平均値
train_data["Age"] = train_data["Age"].fillna(age_mean)
test_data["Age"] = test_data["Age"].fillna(age_mean)
# Fare
fare_mean = train_data["Fare"].mean()  # 平均値
train_data["Fare"] = train_data["Fare"].fillna(fare_mean)
test_data["Fare"] = test_data["Fare"].fillna(fare_mean)
# Embarked
embarked_mode = train_data["Embarked"].mode()  # 最頻値
train_data["Embarked"] = train_data["Embarked"].fillna(embarked_mode)
test_data["Embarked"] = test_data["Embarked"].fillna(embarked_mode)

#  ・get_dummies()により、カテゴリ変数の列を0か1の値を持つ複数の列に変換します。
cat_labels = ["Sex", "Pclass", "Embarked"]  # カテゴリ変数のラベル
train_data = pd.get_dummies(train_data, columns=cat_labels)
test_data = pd.get_dummies(test_data, columns=cat_labels)
train_data.head()


# ・モデルの訓練
#  ・入力と正解を用意します。
#  ・"Survived"の列が正解となります。
t_train = train_data["Survived"]  # 正解
x_train = train_data.drop(labels=["Survived"], axis=1)  # "Survived"の列を削除して入力に
x_test = test_data

#  ・ランダムフォレストは、複数の決定木を組み合わせた「アンサンブル学習」の一種です。
#  ・アンサンブル学習は複数の機械学習を組み合わせる手法で、しばしば高い性能を発揮します。
#  ・以下のコードでは、RandomForestClassifier()を使い、
#    ランダムフォレストのモデルを作成して訓練します。
#  ・多数の決定木の多数決により、分類が行われることになります。
from sklearn.ensemble import RandomForestClassifier
# n_estimators: 決定木の数  max_depth: 決定木の深さ
model = RandomForestClassifier(n_estimators=100, max_depth=5)
model = model.fit(x_train, t_train)


# ・結果の確認と提出
#  ・feature_importances_により各特徴量の重要度を取得し、棒グラフで表示します。
import matplotlib.pyplot as plt
labels = x_train.columns
importances = model.feature_importances_
plt.figure(figsize = (10,6))
plt.barh(range(len(importances)), importances)
plt.yticks(range(len(labels)), labels)
plt.show()

#  ・テストデータを使って予測を行い、形式を整えた上で提出用のcsvファイルとして保存します。
# 判定
y_test = model.predict(x_test)
# 形式を整える
survived_test = pd.Series(y_test, name="Survived")
subm_data = pd.concat([test_id, survived_test], axis=1)
# 提出用のcsvファイルを保存
subm_data.to_csv("submission_titanic.csv", index=False)
subm_data
