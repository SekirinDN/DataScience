# 演習
# Pythonのコードを修正し、エラーが発生しないようにしましょう

# ・課題１
#  ・以下の、リストに奇数を格納し表示するコードを実行するとエラーが発生します。
#  ・問題箇所を修正し、実行してもエラーが発生しないようにしましょう。
# a = []
# for i range(0, 10):
#     if i%2 == 1:
#         a.append(i)
# print (a)

# ・回答１
print("-" * 50)
a = []
for i in range(0, 10):
    if i%2 == 1:
        a.append(i)
print (a)


# ・課題２
#  ・以下の、インスタンスを2つ生成し、リストに格納して表示するコードを実行するとエラーが発生します。
#  ・問題箇所を修正し、実行してもエラーが発生しないようにしましょう。
#  ・なお、修正箇所は一箇所とは限りません。
# class Cat:
#     def set_cat(self, n, a):
#         self.name = n
#         self.age = a
# cat1 = Cat()
# cat1.set_cat("Tama", 4)
# cat2 = Cat()
# cat2.set_cat("Hana" 14)
# cats = [cat1, cat2]  # リストに格納
# for c in cats
#     print(c.name, c.age)

# ・回答２
print("-" * 50)
class Cat:
    def set_cat(self, n, a):
        self.name = n
        self.age = a
cat1 = Cat()
cat1.set_cat("Tama", 4)
cat2 = Cat()
cat2.set_cat("Hana", 14)
cats = [cat1, cat2]  # リストに格納
for c in cats:
    print(c.name, c.age)
