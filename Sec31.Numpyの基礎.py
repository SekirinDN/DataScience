# Numpyの基礎
# 導入

# ・Pythonでは、importの記述により、モジュールをどうにゅうできる
# ・Numpyはモジュールなので、以下のコードで、使えるようにする

import numpy as np

# 一次元配列
print("-" * 50)
nums = np.array([0, 1, 2, 3, 4, 5])
print(nums)

# 二次元配列
print("-" * 50)
nums = np.array([[0, 1, 2], [3, 4, 5]])
print(nums)
print(nums[1][1])

# 三次元配列
print("-" * 50)
nums = np.array([[[0, 1, 2], [3, 4, 5]],[[0, 11, 2], [3, 88, 5]]])
print(nums)
print(nums[1][1][1])

# 配列の演算
print("-" * 50)
nums = np.array([[0, 1, 2], [3, 4, 5]])
print(nums)
print()
print(nums + 3)
print()
print(nums * 5)
print()

# 配列同士の演算
print("-" * 50)
nums2 = np.array([[0, 1, 2], [3, 4, 5]])
nums3 = np.array([[2, 0, 1], [5, 3, 4]])
print(nums2)
print()
print(nums3)
print()
print(nums2 + nums3)
print()
print(nums2 * nums3)
print()

# ・ブロードキャストの活用
#  ・ブロードキャストという機能により、特定の条件を満たしていれば、
#    形状の異なる配列同士でも演算が可能である
#   （どちらかの形状（次元）方向に伸ばすことのできる形状は、変換可）
print("-" * 50)
nums4 = np.array([[1, 1],
                  [3, 4]]) # 二次元配列
nums5 = np.array([2, 3]) # 一次元配列
print(nums4 + nums5)
print()
print(nums4 * nums5)
print()


#  ・形状の変換
#   ・shapeメソッドにより、配列の形状を得ることができる
print("-" * 50)
nams = np.array([[0, 1, 2],
                 [3, 4, 5]])
print(nams.shape) # (2, 3)

#   ・reshapeメソッドを使うと、配列の形状を変換することができる
#   ・以下は、要素数が「8」の一次元配列を、形状が(2,4)の二次元配列に変換
print("-" * 50)
nums = np.array([0, 1, 2, 3, 4, 5, 6, 7])
nums2 = nums.reshape(2, 4)
print(nums2)

#   ・reshapeの引数を「-1」にすることで、
#     どの様な形状でも一次元配列に変換できる
nums3 = np.array([[0, 1, 2],
                 [3, 4, 5]])
nums4 = np.array([[[0, 1, 2], [3, 4, 5]],[[0, 11, 2], [3, 88, 5]]])
print("-" * 50)
nums5 = nums3.reshape(-1) # 二次元配列 ⇒ 一次元配列 へ変換
print(nums5)
nums6 = nums4.reshape(-1) # 三次元配列 ⇒ 一次元配列 へ変換
print(nums6)

#  ・要素へのアクセス
#   ・配列の各要素へのアクセスは、リストの場合と同様にインデックスを使う
print("-" * 50)
nums = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(nums[2]) # 2
nums2 = np.array([[0, 1, 2],
                 [3, 4, 5]])
print(nums2[1][2]) # 5
print(nums2[1, 2]) # 5（上と同じ意味）


# ・関数と配列
#  ・半数の引数や戻り値として、Numpyの配列が使用可能である
#  ・以下は、引数として配列を受け取り、戻り値として配列を返している
print("-" * 50)
def my_func(x):
    y = x * 2 + 1
    return y
nums = np.array([[0, 1, 2],
                 [3, 4, 5]])
nums2 = my_func(nums)
print(nums)
print(nums2)


# ・Numpyの様々な機能
#  ・sum、average、max、min（合計、平均、最大、最小）
print("-" * 50)
# 標準配列でも一部可能だが、表示（考え方が番うので事実上使用できない）
# nums = ([[0, 1, 2],
#          [3, 4, 5]])
# Numpyの二次元配列
nums = np.array([[0, 1, 2],
                 [3, 4, 5]])
print(nums)
print(f"合計：{np.sum(nums)}")
print(f"平均：{np.average(nums)}")
print(f"最大：{np.max(nums)}")
print(f"最小：{np.min(nums)}")

 # ・引数に、「axis」を指定すると、特定の方向で演算ができる
print("-" * 50)
print(nums)
print(f"合計2：{np.sum(nums, axis=0)}") # 縦方向で合計
print(f"合計3：{np.sum(nums, axis=1)}") # 横方向で合計
