# Pythonの基礎2
# リストや分岐、ループなどについて学んでいきます

# ・リスト
#  ・リストは、複数の値をまとめて扱う場合に使用します。
#  ・リストは全体を[]で囲み、各要素は「,」で区切ります
print("-" * 50)
a = [2011, 2012, 2013, 2014, 2015]  # リストの作成
print(a[0])  # 先頭から0番目の要素
print(a[1])  # 先頭から1番目の要素
print(a[2])  # 先頭から2番目の要素

#  ・リストでは、変数名の直後に[ ]を記述することで各要素を取り出すことができます。
#  ・Pythonのリストはどのような値でも格納することができます。
print("-" * 50)
b = 2016
c = [b, 2017, 20.1, "Hello", "Hi"]
print(c[1:4])  # 先頭から1番目以上、4番目未満の範囲

#  ・リストの中にリストを格納することもできます。
print("-" * 50)
d =[[2012, 2013, 2014], [2015, 2016, 2017]]
print(d[0])  # 先頭から0番目の要素
print(d[0][1])  # 先頭から0番目の要素の1番目の要素

#  ・リストは、作成後に要素を変更することができます。
#  ・また、appendにより要素を追加することができます
print("-" * 50)
e = ["Py", 543.21, 79, "thon", [2018, 2019, 2020]]
print(e)
# 要素の変更
e[2] = 99
print(e)
# 要素の追加
e.append(2021)
print(e)
#  ・リストにより、多くの値を効率よく扱うことが可能になります。


# ・タプル
#  ・タプルはリストと同じく複数の値をまとめて扱いたいときに利用しますが、
#    要素の追加や削除、入れ替えなどはできません。
#  ・タプルは全体を()で囲み、各要素は,で区切ります。
#  ・要素を変更する予定が無い場合は、リストよりもタプルを使用する方がベターです。
#  ・以下では、リストとタプルを比較しています。
print("-" * 50)
a = [2012, 2013, 2014]  # リスト
b = (2012, 2013, 2014)  # タプル
print(a)
print(b)
print(a[1])
print(b[1])
a[1] = 2016
print(a)
# b[1] = 2016  # エラーが発生
# print(b)
a.append(2015)
print(a)
# b.append(2015)  # エラーが発生
# print(b)
#  ・タプルの要素を変更したり、タプルに要素を追加しようとするとエラーが発生します。


# ・辞書
#  ・辞書は、キーと値の組合せでデータを格納します。　
#  ・以下は、Pythonの辞書を扱う例です。
#  ・文字列をキーとして辞書を作成し、値の取得や入れ替え、要素の追加を行なっています。
print("-" * 50)
a = {"Taro":1985, "Hanako":1986}  # 辞書の作成
print(a)  # 辞書の表示
print(a["Taro"])   # "Taro"のキーを持つ値を取得
a["Hanako"] = 1987  # 要素の入れ替え
print(a)
a["Jiro"] = 1989  # 要素の追加
print(a)
#  ・辞書は、キーを使って多数の値を管理したい際に使用します。


# ・if文
#  ・if文により条件分岐を行うことができます。
#  ・ifの右側がTrueであればその次の処理が、Falseであればelseの次の処理が実行されます。
#  ・以下のコードは、aの値が5であれば足し算を行い、5でなければ掛け算を行います。
print("-" * 50)
a = 5
# a = 2
if a == 5:  # aと5は等しいのでifの右はTrue
    print(f"3 + 4 = {3 + 4}")
else:
    print(f"3 * 4 = {3 * 4}")

#  ・分岐後の処理の行頭には、複数のスペースからなる「インデント」を挿入します。
#  ・インデントは通常半角スペース4つを使用します。
#  ・3つ以上の分岐を行う際には、elifを使用します。
print("-" * 50)
b = 4
# b = 2
# b = 10
if b < 3:
    print("Hello!")
elif b < 5:  # ifの右側がFalseの場合
    print("Hi!")
else:  # if、elifの右側がFalseの場合
    print("Yeah!")

#  ・elifを並べることで、さらに多くの分岐を行うことが可能になります。
print("-" * 50)
time = 20
# time = 10
# time = 15
# time = 23
if time < 12:
    print("Good morning!")
elif time < 17:
    print("Good afternoon!")
elif time < 21:
    print("Good evening!")
else:
    print("Good night!")


# ・for文
#  ・for文を使えば、同じ処理を繰り返し実行することができます。
#  ・以下の例は、リストをとfor文を使ったループ処理です。
print("-" * 50)
a = [2001, 2002, 2003, 2004, 2005]
for i in a:  # iにはリストaの各要素が入る
    print(i + 10)  # 行頭にインデントを入れる
#  ・繰り返し行う処理には行頭にインデントを挿入します。
#  ・ループ内で連番の整数を使う場合は、rangeを使用します。
#  ・以下の例では、iに0から5までの整数が入ります。
print("-" * 50)
for i in range(0, 6):  # iには0以上6未満の整数が入る
    print(i * 2)
#  ・for文によるループを使うことで、冗長なコードを簡潔にまとめることが可能になります。


# ・while文
#  ・ある条件が満たされている間ループするためには、while文を用います。
print("-" * 50)
print("--- 10未満 ---")
a = 0
while a < 10:  # aが10未満である間ループ
    print(a)
    a += 1  # aに1を加える
print("--- 10と等しくない ---")
b = 0
while b != 10:  # bが10と等しくない限りループ
    print(b)
    b += 1


# ・分岐とループの組み合わせ
#  ・分岐とループを組み合わせることで、
#    条件が満たされた処理のみをループ内で実行することが可能になります。
print("-" * 50)
a = []  # 空のリスト
for i in range(0, 10):
    if i % 2 == 0:  # 偶数であれば
        a.append(i)
print (a)
