# 決定木

# ・決定木とは？
#  ・決定木（Decision Tree）では、木の枝のような構造を用いて分類を行う
#  ・学習結果を視覚化が可能で、ルールを明確に表記できる（メリット）


# ・データセットの読み込み
#  ・今回は、Irisデータセットを使用します。以下はこのデータセットの説明変数です。
#   ・sepal length (cm): がくの長さ
#   ・sepal width (cm): がくの幅
#   ・petal length (cm): 花弁の長さ
#   ・petal width (cm): 花弁の幅
#  ・目的変数classは0から2の整数で、花の品種を表します。
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()


# ・決定木の実装
#  ・tree.DecisionTreeClassifierにより決定木のモデルを作成します。
from sklearn import tree
model = tree.DecisionTreeClassifier(max_depth=3)
#  ・fitメソッドにより訓練が行われ、決定木が構築されます
model = model.fit(iris.data, iris.target)
#  ・predictメソッドにより予測を行い、正解率を測定します。
predicted = model.predict(iris.data)
print("正解率:", sum(predicted == iris.target) / len(iris.target))
#  ・graphvizとpydotplusを使い、決定木を可視化します。
import graphviz
import pydotplus
from IPython.display import Image
dot_str = tree.export_graphviz(
    model,
    feature_names=iris.feature_names,
    out_file=None,
    filled=True,
    rounded=True
    )
graph = pydotplus.graph_from_dot_data(dot_str)

file_name = "iris_tree.png"
graph.write_png(file_name)
Image(file_name)
