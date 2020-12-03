# 要素のindexを取得する
list1 = ["a", "b", "c"]
print(list1.index("a"))

# 末尾に要素を追加
list1.append("d")
print(list1)

# 指定インデックスに要素を追加
list1.insert(0, "Z")
print(list1)

# 指定要素を削除
list1.remove("a")
print(list1)

# 末尾の要素を取得
value = list1.pop()
print(value)
print(list1)

# 指定要素を数を首都kう
list1.append("c")
print(list1.count("c"))

# ソート
list2 = [5, 4, 3, 2, 1]
list2.sort()
print(list2)

# 異なる型のリストに追加できる
mix_list = ["a", 20, True]
print(mix_list)

# リスト結合
list2.extend(mix_list)
print(list2)

list3 = [1, 2, 3, 4]

for item in [v + 1 for v in list3]:
    print(item)

for item in [v + 1 for v in list3 if v >= 3]:
    print(item)

# 二重ループ
list4 = [1, 2, 3, 4]
for v1 in list3:
    for v2 in list4:
        v3 = v1 * v2
        print(f"{v1} * {v2} = {v3}")

list5 = [v1 * v2 for v1 in list3 for v2 in list4]
print(list5)

list5 = [(v1, v2, v1 * v2) for v1 in list3 for v2 in list4]
for v in list5:
    print(f"{v[0]} * {v[1]} = {v[2]}")

value = [(v1, v2, v3)
         for v1 in range(0, 5)
         for v2 in range(0, 5)
         for v3 in range(0, 5)]

print(len(value) * 300)
