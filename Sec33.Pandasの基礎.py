# Pandasの基礎

# ・Pandasは、Pythonでデータ分析を行うためのライブラリ
# ・データの読み込み、編集、統計量の表示などを、簡単に行える
# ・主要なコードは、Cython または C言語で書かれており、高速に動作する
# ・これらの理由により、Pandasは、データサイエンスにおいて、とても有用である

# ・Pandasの導入
#  ・Pandasのデータ構造には、Series（一次元）と、DataFrame（二次元）がある
#  ・Pandasモジュールをインポートする
import pandas as pd
import numpy as np

# ・Seriesの作成
#  ・Seriesは、ラベル付きの一次元配列で、整数・少数・文字列など、
#    様々な型のデータを格納できる
#  ・以下は、リストからSeriesを作る例で、ラベルは index で指定する
print("-" * 50)
a = pd.Series([60, 80, 70, 50, 30],
        index=["Japanese", "English", "Math", "Science", "History"])
print(type(a))
print(a)

# np.array でも、指定できる
print("-" * 50)
a = pd.Series(np.array([60, 80, 70, 50, 30]),
        index=np.array(["Japanese", "English", "Math", "Science", "History"]))
print(type(a))
print(a)

# 辞書でも指定できる
print("-" * 50)
a = pd.Series({
    "Japanese": 60,
    "English": 80,
    "Math": 70,
    "Science": 50,
    "History": 30})
print(type(a))
print(a)

# ・Seriesの操作
print("-" * 50)
a = pd.Series([60, 80, 70, 50, 30],
        index=["Japanese", "English", "Math", "Science", "History"])
# print(a[1]) # インデックスで指定
# b = pd.Series([20], index=["Art"]) # うまく動作しない
# a = a.append(b)                    # うまく動作しない
print(a)
print(f"数学は、{a["Math"]}点です。") # ラベルを指定


# DataFrameの作成
# ・DataFrameは、ラベル付きの二次元配列で、整数・少数・文字列など様々なデータを格納できる
# ・以下は、二次元リストからDataFrameを作る例である
print("-" * 50)
a = pd.DataFrame([[80, 60, 70, True],
                  [90, 80, 70, True],
                  [70, 60, 75, True],
                  [40, 60, 50, False],
                  [20, 30, 40, False],
                  [50, 20, 10, False],])
print(a)
print("-" * 50)

# DataFrameは、Series・辞書・NumPyの配列から作ることが可能
# 行と列には、ラベルを付けることができる
a.columns = ["Japanese", "English", "Math", "Judge"]
a.index = ["Taro", "Hanako", "Jiro", "Sakuko", "Saburo", "Yoko"]
print(a)


# データの特徴
# ・shapeにより、データの行数・列数を取得できる
print(a.shape)
# ・最初のn行や、最後のn行を表示するには、head()・tail()を使う
# ・特に行数が覆う場合、データの概要を把握するのに便利
print("-" * 50)
print(a.head(3))
print(a.tail(3))
print("-" * 50)
print(a.head()) # 引数を省略すると先頭5行を表示する
print(a.tail()) # 引数を省略すると終端5行を表示する
# ・基本的な統計量は、describe()で一度に表示できる
print("-" * 50)
print(a.describe())
# ・各メソッドで個別にも取得可能
print("-" * 50)
print(a.count())
print("-" * 50)
print(a.mean())
print("-" * 50)
print(a.std())
print("-" * 50)
print(a.min())
print("-" * 50)
print(a.max())


# DataFrameの操作
# ・インデックスやラベルを使って、DataFrameのデータの操作を行う事ができる
# ・以下は、loc()メソッドを使って範囲を指定し、Seriesデータを取り出す
print("-" * 50)
tr = a.loc["Taro", :] # 特定の1行取り出す（Taro）
print(type(tr))
print(tr)
print("-" * 50)
tr = a.loc["Jiro", :] # 特定の1行取り出す（Jiro）
print(tr)

# 同様に、DataFrameから列を取り出すこともできる
print("-" * 50)
ma = a.loc[:, "English"] # 特定の1列取り出す（English）
print(ma)

# iloc() メソッドを使うと、行番号・列番号で指定できる
print("-" * 50)
r = a.iloc[1:4, :2] # 行番号1～3、列番号0～1を取り出す
print(r)

# loc() メソッドを使い、行を追加することもできる
print("-" * 50)
a.loc["Kenta"] = pd.Series([80, 70, 60, True],
                           index=["Japanese", "English", "Math", "Judge"],
                           name="Kenta") # 行を追加
print(a)

# ・列のラベルを指定しs、列（のデータ）を追加できる
a["Science"] = [80, 70, 60, 50, 60, 40, 80] # 列をリストとして追加
print("-" * 50)
print(a)

# ・sort_values()メソッドにより、DataFrameをソートできる
print("-" * 50)
a.sort_values("Math", ascending=False, inplace=True) # Mathの列で降順にソート
print(a)