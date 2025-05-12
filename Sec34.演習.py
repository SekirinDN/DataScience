# Sec3nの演習
# NumPy、matplotlib、Pandasの扱いに慣れる

# 課題１
# ・reshape()メソッドによる、配列形状の操作
#  ・以下のコードはエラーが発生する
#  ・reshape()メソッドにより、配列あの形状を変更し、エラーが出ない様にしてください
import numpy as np
a = np.array([0, 1, 2, 3, 4, 5]) # この配列の形状を、reshape()メソッドで変更する
b = np.array([[5, 4, 3], [2, 1, 0]])
# 答え１
a = a.reshape(2, 3) # 2行3列の形状に変更する
# -----------------------------------------
print("-" * 50)
print(a + b)

# 課題２
# ・三次関数の描画
#  ・以下の三次元関数の曲線を、matplotlibを使って描画する
#     y = x^3 - 12x
#  ・以下のコードを補完してください
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4, 4)
# 答え２
# この下のコードを補完する
y = x ** 3 - 12 * x
plt.xlabel("x_value")
plt.ylabel("y_value")
plt.plot(x, y)
plt.show()

# 課題３
# ・DataFrameの作成
#  ・以下にコードを追記し、行と列にラベルの付いたDataFrameを作成してください
import pandas as pd
import  numpy as np
a_list = [[80, 60, 70, True],
          [90, 80, 70, True],
          [70, 60, 75, True],
          [40, 60, 50, False],
          [20, 30, 40, False],
          [50, 20, 10, False],]
a_index = ["Taro", "Hanako", "Jiro", "Sakuko", "Saburo", "Yoko"]
a_columns = ["Japanese", "English", "Math", "Judge"]
# 答え３
# ここから、コードを追記する
a = pd.DataFrame(a_list, index=a_index, columns=a_columns)
# 以下の3行に分けても良い
# a = pd.DataFrame(a_list)
# a.index = a_index
# a.columns = a_columns
print("-" * 50)
print(a)
