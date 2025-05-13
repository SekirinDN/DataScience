# 回帰
# 回帰は、教師あり学習の一種で、変数間の関係を予測します
# 今回は、単回帰と重回帰の２つを解説します

# ・データセットの読み込み
#  ・ボストン住宅価格のデータセットを読み込みます。
#  ・このデータセットには、説明変数と目的変数が含まれます。
#  ・説明変数: 何かの原因となっている変数
#  ・目的変数: その原因を受けて発生した結果である変数
import pandas as pd
from sklearn import datasets
boston = datasets.load_boston()
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)  # data: 説明変数
boston_df["PRICE"] = boston.target  # target: 目的変数
boston_df.head()
#  ・説明変数が様々な住宅の特徴で、目的変数が住宅の価格であることが分かります。
#  ・各列のラベルの意味は、DESCRにより表示することができます。
print(boston.DESCR)  # データセットの説明
#  ・データセットの特徴を把握するために、統計量を表示します。
boston_df.describe()
#  ・データセットを、訓練用のデータとテスト用のデータに分割します。
from sklearn.model_selection import train_test_split
# 訓練データとテストデータに分割
x_train, x_test, t_train, t_test = train_test_split(boston.data, boston.target, random_state=0)


# ・単回帰
#  ・単回帰では、直線を使い1つの説明変数で目的変数を予測します。
#  ・x を説明変数、 y を目的変数、 a を係数、 b を切片としたとき、
#    単回帰は以下の式で表されます。
#     y = a * x + b
#  ・以下のコードでは、linear_model.LinearRegressionにより線形回帰のモデルを生成し、
#    fitメソッドにより、モデルの訓練を行います。
#  ・説明変数にRM（部屋数）のみを使うことで単回帰になります。
#  ・訓練の結果、式の係数と切片が最適化されます。
from sklearn import linear_model
# RM（部屋数）の列を取得
x_rm_train = x_train[:, [5]]
x_rm_test = x_test[:, [5]]
model = linear_model.LinearRegression() # 線形回帰モデル
model.fit(x_rm_train, t_train)  # モデルの訓練
#  ・訓練済みのモデルから、式の係数と切片を取得します。
a = model.coef_ # 係数
b = model.intercept_ # 切片
print("a: ", a)
print("b: ", b)
#  ・取得した係数と切片を使った回帰直線を、元のデータとともにグラフで表示します。
import matplotlib.pyplot as plt
plt.scatter(x_rm_train, t_train, label="Train")
plt.scatter(x_rm_test, t_test, label="Test")
y_reg = a * x_rm_train + b  # 回帰直線
plt.plot(x_rm_train, y_reg, c="red")
plt.xlabel("Rooms")
plt.ylabel("Price")
plt.legend()
plt.show()
#  ・上記の結果は、回帰直線は、部屋数が多くなると価格が上がるという
#    データの傾向をシンプルに表しています。
#  ・次に、モデルのMSE（平均二乗誤差 Mean Squared Error）を計算します。
#  ・MSEは、 E を誤差、 yk を予測値、 tk を正解値として以下の式で定義されます。
#     E = 1n∑k=1n(yk−tk)2 ？？？
#  ・この誤差が小さいほどモデルの誤差が小さくなります。
#  ・以下のコードは、訓練データとテストデータ、
#    それぞれでmean_squared_errorによりMSEを計算します。
from sklearn.metrics import mean_squared_error
# 訓練データ
y_train = model.predict(x_rm_train)
mse_train = mean_squared_error(t_train, y_train)
print("MSE(Train): ", mse_train)
# テストデータ
y_test = model.predict(x_rm_test)
mse_test = mean_squared_error(t_test, y_test)
print("MSE(Test): ", mse_test)


# ・重回帰
#  ・重回帰では、複数の説明変数を使い目的変数を予測します。
#  ・重回帰は、 xk を各説明変数として以下の式で表されます。
#     y = ∑k=1nakxk+b ？？？
#  ・今回は、13種類の説明変数を全て使って重回帰分析を行います。
#  ・単回帰の場合と同じく、linear_model.LinearRegressionを使います。
model = linear_model.LinearRegression() # 線形回帰
# 全ての説明変数を使い学習
model.fit(x_train, t_train)
#  ・各説明変数に対応した係数を取得します。
a_df = pd.DataFrame(boston.feature_names, columns=["Exp"])
a_df["a"] = pd.Series(model.coef_)
print(a_df)
#  ・切片を取得します。
print("b: ", model.intercept_)
#  ・訓練データとテストデータ、それぞれでMSE（平均二乗誤差）を計算します。
# 訓練データ
y_train = model.predict(x_train)
mse_train = mean_squared_error(t_train, y_train)
print("MSE(Train): ", mse_train)
# テストデータ
y_test = model.predict(x_test)
mse_test = mean_squared_error(t_test, y_test)
print("MSE(Test): ", mse_test)
#  ・単回帰の場合よりも誤差が小さくなりました。
#  ・ただ、テストデータの誤差は訓練データの誤差よりも大幅に大きくなりました。
#  ・モデルが訓練データに過剰に適合していないか、慎重に判断する必要があります。
