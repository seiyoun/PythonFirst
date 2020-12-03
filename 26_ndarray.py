import numpy as np

np_ary = np.array([1, 2, 3, 4])
# 型指定できる
# np_ary = np.array([1, 2, 3, 4, 5, 6, 7], np.int8)
print(np_ary)
print(type(np_ary))

# リストに戻す
lst = np_ary.tolist()
print(lst)
print(type(lst))

# 末尾に要素追加
np_ary = np.append(np_ary, [99, 0])
print(np_ary)

# 指定インデックスに要素を追加
np_ary = np.insert(np_ary, 0, 999)
print(np_ary)

# 指定インデックスの要素を削除
np_ary = np.delete(np_ary, 0)
print(np_ary)

# シャッフル
np.random.shuffle(np_ary)
print(np_ary)

# ソート(昇順)
np_ary = np.sort(np_ary)
print(np_ary)

# ソート(降順)
np_ary = np.sort(np_ary)[::-1]
print(np_ary)
print(type(np_ary))

# すべての要素に掛け算
print(np_ary * 3)

# すべての要素に足し算
print(np_ary + 3)

# 配列結合
np_ary2 = np.append(np_ary, [5, 6, 7, 8])
print(np_ary2)

# 長さ
print(len(np_ary2))

# 要素削除
np_ary3 = np.delete(np_ary2, 0)
print(np_ary3)

# 行列計算
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

b = np.array([
    [1],
    [2],
    [3],
])
print(np.dot(a, b))

# 2次元配列に変換
np_ary4 = np.array([1, 2, 3, 4, 5, 6])
print(np_ary4.reshape(2, 3))

# ループ
# 小数点使用不可
# for i in range(1, 10, 0.1):
#     print(i)

for i in range(1, 10):
    print(i * 0.1)

for i in np.arange(0, 1, 0.1):
    print(i)

# ※注意(参照)
np_ary5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# 参照になる
np_ary6 = np_ary5[:3]

print(np_ary5)
print(np_ary6)

np_ary6[0] = 10

print(np_ary5)
print(np_ary6)

# ※注意(コピー)
np_ary7 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
np_ary8 = np_ary7
# コピー
np_ary8 = np.add(np_ary8, 0)
np_ary8[0] = 999
print(np_ary7)
print(np_ary8)

# 条件に一致するインデックスデータを書き換え
np_ary9 = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
np_ary9[np_ary9 < 0] = 0
np_ary9[np_ary9 > 0] = 5
print(np_ary9)
# 条件に一致する要素はTrue,
print(np_ary9 > 0)
