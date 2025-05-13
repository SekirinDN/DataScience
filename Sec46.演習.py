# 演習
# 相関係数を計算するコードを、NumPyが用意した関数を使わずに自分で実装してみましょう

# ・相関係数の計算
#  ・以下の X 、 Y 2組のデータを考えます。それぞれ、データの個数は n とします。
#     X = x1,x2,⋯,xn
#     Y = y1,y2,⋯,yn
#  ・これらのデータの共分散 Cov(X,Y) は、以下の式で表されます。
#     Cov(X,Y) = 1/n * (∑k=1) * (xk−μx)(yk−μy)
#  ・ここで、 μx は X の平均、 μy は Y の平均です。
#  ・相関係数 ρ は、XとYの共分散 Cov(X,Y) およびXとYそれぞれの
#    標準偏差 σX 、 σY を用いて以下の式で表されます。
#     ρ = (Cov(X,Y)) / (σX * σY)
#  ・今回の演習では、この相関係数を、NumPy の corrcoef()関数を使わずに計算するコードを実装します。
#  ・以下のセルの、指定された箇所にコードの追記を行い、相関係数が正しく計算できるようにしましょう。

# 問題
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([50, 70, 40, 60, 80])  # 数学の点数
# y = np.array([60, 80, 50, 50, 70])  # 英語の点数
# print("--- 相関係数: corrcoef関数を使用 ---")
# print(np.corrcoef(x, y))  # 相関係数
# print("--- 相関係数: 自分で実装 ---")
# cov_xy =  # ← 共分散を計算するコードを書く
# rho =  # ← 相関係数を計算するコードを書く
# print(rho)
# plt.scatter(x, y)
# plt.xlabel("x", size=14)
# plt.ylabel("y", size=14)
# plt.grid()
# plt.show()

# 回答
import numpy as np
import matplotlib.pyplot as plt
x = np.array([50, 70, 40, 60, 80])  # 数学の点数
y = np.array([60, 80, 50, 50, 70])  # 英語の点数
print("--- 相関係数: corrcoef関数を使用 ---")
print(np.corrcoef(x, y))  # 相関係数
print("--- 相関係数: 自分で実装 ---")
cov_xy = np.average((x - np.average(x)) * (y - np.average(y)))  # ← 共分散を計算するコードを書く
rho = cov_xy / (np.std(x) * np.std(y))  # ← 相関係数を計算するコードを書く
print(rho)
plt.scatter(x, y)
plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()
