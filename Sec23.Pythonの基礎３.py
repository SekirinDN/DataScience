# Pythonの基礎3
# 関数とクラス、ファイルの保存について解説します

# ・関数
#  ・関数を用いることで、処理を一括りにして何度も呼び出すことができます。
#  ・以下はシンプルな関数の例です。
print("-" * 50)
def say_hello():  # defの後に関数名を記述
    print("Hello world!")  # 行頭にインデントを挿入
say_hello()  # 関数の呼び出し
#  ・一度関数を定義しておけば、あとから何度でも呼び出すことができます。
print("-" * 50)
def say_gm():
    print("Good morning!")
say_gm()
say_gm()
say_gm()


# ・引数
#  ・関数は、外部からの値を引数として受け取ることができます。
#  ・以下は、引数を伴うシンプルな関数です。
print("-" * 50)
def say_number(a):  # aが引数
    print(a)
say_number(123)
say_number("あいうえお")

#  ・関数を呼び出す際に、( ) 内に値を渡すとそれを関数が受け取ります。
#  ・引数が複数の場合は、,（カンマ）で区切ります。
print("-" * 50)
def add(a, b, c):  # 引数は3つ
    d = a + b + c
    print(d)
add(3, 4, 5)


# ・返り値
#  ・返り値を用いると、関数から外部に値を渡すことができます。
#  ・以下は、返り値のシンプルな例です。
print("-" * 50)
def get_number():
    a = 123
    return a  # 返り値
b = get_number()
print(b)
#  ・関数の内部にreturnを記述すると、その直後の値を関数の外部に渡します。
#  ・以下は、引数と返り値を組み合わせた例です。
print("-" * 50)
def add(a, b):
    c = a + b
    return c
result1 = add(3, 4)
print(result1)
result2 = add(7, 8)
print(result2)
#  ・以上のような関数を使うことで、コードの再利用が可能になります。


# ・変数のスコープ
#  ・関数内で定義された変数がローカル変数、関数外で定義された変数がグローバル変数です。
print("-" * 50)
glob_1 = 123  # グローバル変数
def show_number():
    loc_1 = 456  # ローカル変数
    print(glob_1, loc_1)
show_number()
#  ・ローカル変数は同じ関数内からのみアクセスできますが、
#    グローバル変数はどこからでもアクセスできます。
#  ・以下のコードでは、関数の外でローカル変数loc_2にアクセスしようとしているため、
#    エラーが発生します。
glob_2= 123 # グローバル変数
def setNum():
    loc_2 = 456 # ローカル変数
setNum()
# print(glob_2, loc_2) # エラーが発生
print(glob_2)


# ・クラス
#  ・クラスを用いると、複数の「関数のようなもの」をまとめることができます。
#  ・この「関数のようなもの」は、メソッドと呼ばれます。
#  ・Pythonでクラスを定義するためには、classの表記を用います。
#  ・メソッドはクラス内で定義するのですが、関数と同様にdefの直後にメソッド名を記述します。
#  ・以下の例では、Calcクラス内にaddメソッドが記述されています。
#  ・クラスからインスタンスを生成し、このインスタンスからメソッドを呼び出すことができます。
print("-" * 50)
class Calc:  # Calcクラス
    def add(self, a, b):  # addメソッド
        print(a + b)

    def multiply(self, a, b):  # multiplyメソッド
        print(a * b)
cl = Calc()  # インスタンスclを生成
cl.add(2, 3)
cl.multiply(4, 5)
#  ・関数とは異なり、メソッドの最初の引数はselfと書く必要があります。
#  ・このselfを用いて、インスタンスは値を保持することができます。
#  ・インスタンス内で値を保持する変数を、インスタンス変数といいます。
#  ・以下の例では、set_numberメソッドの中でインスタンス変数を設定しています。
print("-" * 50)
class Box:
    def set_number(self, n1, n2):
        self.num1 = n1  # num1がインスタンス変数
        self.num2 = n2
bx = Box()
bx.set_number(123, 456)
print(bx.num1)  # インスタンス変数の値を表示
print(bx.num2)
bx.num1 = 999  # 値を変更
print(bx.num1)
#  ・インスタンス変数は、インスタンスごとに異なる値を設定することができます。
#  ・以下の例では、Dogクラスからdog1、dog2、2つのインスタンスを生成し、インスタンス変数にそれぞれ異なる値を設定しています。
#  ・その上で、これらのインスタンスをリストに格納し、ループ内で値を表示します。
print("-" * 50)
class Dog:
    def set_dog(self, n, a):
        self.name = n
        self.age = a
dog1 = Dog()
dog1.set_dog("Pochi", 5)
dog2 = Dog()
dog2.set_dog("Hachi", 12)
dogs = [dog1, dog2]  # リストに格納
for d in dogs:
    print(d.name, d.age)
#  ・クラスを使うことで、複雑な構造を持つ処理を簡潔に記述することが可能になります。


# ・ファイルの保存と読み込み
#  ・with構文を用いて、ファイルの読み込みや保存を簡潔に記述することができます。
#  ・以下は、文字列をファイルに保存する例です。
#  ・保存されたファイルは、サイドバーで確認することができます。
print("-" * 50)
greetings = "Good morning! Good night!"
with open("greetings.txt", "w") as f:
    f.write(greetings)  # ファイルに保存
#  ・以下は、上記で保存されたファイルを読み込んで表示する例です。
with open("greetings.txt", "r") as f:
    print(f.read())  # ファイルの読み込み
