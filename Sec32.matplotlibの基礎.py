# matplotlibの基礎

# ・matplotlibは、グラフの描画や、画像の表示、簡単なアニメーション
#   の作成が行いえる
#  ・データサイエンスにおいて、データを可視化するため、とても有用である
#  ・Numpyと同じく、インポートして使用する
#  ・グラフを表示するためには、matplotlibの「pyplot」を使用する
#     import numpy as np
#     import matplotlib.pyplot as plt

# ・linspace関数
#  ・matplotlibでグラフを描画する際に、
#    Numpyのlinspace関数がよく使用される
#  ・ある区間を、50個に区切って、Numpyの配列にする（分割数の指定も可）
#  ・この配列は、グラフの横軸の値として、よく使われる
print("-" * 50)
import numpy as np
# x = np.linspace(-5, 5) # 3番目の読引数を省略すると、50個に区切りになる
x = np.linspace(-5, 5, 30) # -5～5を、30個に区切る
print(x)
print(len(x))

# ・グラフの描画
#  ・例として、pyplotを使って、直線を描画する
#  ・linspace関数で、x座標を配列として生成し、
#    これに値をかけてy座標とする
#  ・そして、plotで、x座標・y座標のデータをプロットし、
#    showでグラフを表示する
print("-" * 50)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5)
y = 2 * x # xに、2をかけてy座標とする
# plt.plot(x, y)
# plt.show()

# ・グラフの装飾
#  ・軸のラベルやタイトル、凡例などを表示し、
#    線のスタイルを変更してリッチなグラフにする
#  ・↑ の処理を引き継ぐ
y_1 = 2 * x
y_2 = 3 * x
# 軸のラベル
# plt.xlabel("xの値")
# plt.ylabel("yの値")
plt.xlabel("x Value")
plt.ylabel("y Value")
# グラフのタイトル
# plt.title("私のグラフ")
plt.title("My Graph")
# 凡例と線のスタイルを指定する
plt.plot(x, y_1, label="y1")
plt.plot(x, y_2, label="y2", linestyle="dashed") # 破線に設定
plt.legend() # 凡例を表示
# プロットする
plt.show()


# ・散布図の表示
#  ・scatter関数により、散布図を表示できる
#  ・以下は、x座標・y座標から、散布図を描画する
x = np.array([1.2, 2.4, 0.0, 1.4, 1.5])
y = np.array([2.4, 1.4, 1.0, 0.1, 1.7])
plt.scatter(x, y) # 散布図の生成
plt.show() # プロットする


# ・画像の表示
#  ・「pyplot」の imshow関数は、配列を画像として表示できる
#  ・以下は、配列を画像として表示するサンプル
#  ・0が黒、15が白、間は中間色
img = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 13, 14, 15]])
plt.imshow(img, "gray") # グレースケールで表示する
plt.colorbar()          # カラーバーを表示する
plt.show()              # プロットする

