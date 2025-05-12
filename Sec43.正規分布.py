# 正規分布
#  最もよく使われるデータの分布である、「正規分布」について解説します

# ・ネイピア数のべき乗
#  ・ネイピア数 e は数学的に扱いやすい値なので、分布や確率を扱う際によく使われます。
#  ・ネイピア数のべき乗 ex は、以下のように exp を使ってよく表されます。
#     exp(x)
#  ・NumPyでは、np.eによりネイピア数を取得することができます。
#  ・また、np.exp( )関数によりネイピア数のべき乗を計算することができます。
print("-" * 50)
import numpy as np
print(np.e)  # ネイピア数
print(np.exp(1))  # ネイピア数の1乗
print(np.e**2)  # ネイピア数の2乗
print(np.exp(2))  # ネイピア数の2乗
#  ・ネイピア数を使った以下の式により、釣鐘状の曲線を描くことができます。
#     y = exp(−x ** 2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 3)
y = np.exp(-x**2)
plt.plot(x, y)
plt.show()
#  ・↑ このような釣鐘状の曲線が、正規分布で利用されます。


# ・正規分布とは？
#  ・「正規分布」（normal distribution）は、
#    自然界の様々な現象に対してよく当てはまるデータの分布です。
#  ・例えば、身長や体重、テストの成績、工業製品のサイズなどは正規分布におおよそ従います。
#  ・正規分布において、ある値 x が得られる確率 f(x) は、
#    以下の確率密度関数と呼ばれる関数で表されます。
#     f(x)=1σ2π−−√exp(−(x−μ)**2/2σ2) ？？？
#  ・ここで、 μ は平均値で分布の中央となり、 σ は標準偏差で分布の広がり具合を表します。
#  ・上記の式は少々複雑ですが、平均値を0、標準偏差を1とすると、
#    以下のように比較的シンプルな形になります。
#     f(x)=12π−−√exp(−x**2/2) ？？？
#  ・それでは、確率密度関数を使って正規分布の曲線を描画しましょう。
#  ・平均値は0に固定し、標準偏差を3通りにして3つの曲線を描画します。
import numpy as np
import matplotlib.pyplot as plt
def pdf(x, mu, sigma):  # mu: 平均値  sigma: 標準偏差
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2 / (2*sigma**2))  # 確率密度関数
x = np.linspace(-5, 5)
y_1 = pdf(x, 0.0, 0.5)  # 平均値が0で標準偏差が0.5
y_2 = pdf(x, 0.0, 1.0)  # 平均値が0で標準偏差が1
y_3 = pdf(x, 0.0, 2.0)  # 平均値が0で標準偏差が2
plt.plot(x, y_1, label="σ: 0.5")
plt.plot(x, y_2, label="σ: 1.0")
plt.plot(x, y_3, label="σ: 2.0")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
#  ・標準偏差は値のばらつき具合を表すのですが、
#    これが小さいと曲線の幅が狭くなり、大きいと幅が広くなります。
#  ・また、正規分布の曲線とx軸に挟まれた領域の面積は1になります。
#  ・これは、確率の総和が1であることに対応します。


# ・正規分布に従う乱数
#  ・正規分布に従う乱数は、NumPyのrandom.normal()関数を使って生成することがます。
#  ・以下のコードは、生成されたデータの分布を、
#    matplotlib の hist()関数でヒストグラムとして表示します。
import numpy as np
import matplotlib.pyplot as plt
# 正規分布に従う乱数を生成
s = np.random.normal(0, 1, 10000)  # 平均0、標準偏差1、10000個
# ヒストグラム
plt.hist(s, bins=25)  # binsは棒の数
plt.xlabel("x", size=14)
plt.grid()
plt.show()
#  ・生成されたデータの分布は、釣鐘状の形状となりました。
#  ・確率密度関数の形状とほぼ同じですね。
