# 変更不能リスト
menu = ("a", "b")
print(menu[0])
print(menu[1])

(a, b, c) = ("a", "b", "c")
print(a, b, c)

(a, *b, c) = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)
