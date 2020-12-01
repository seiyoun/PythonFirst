jinshiyuan = "jinshiyuan"

# インデックス指定
print(jinshiyuan[2])
# 範囲指定
print(jinshiyuan[0:2])
# 0から指定インデックスまで
print(jinshiyuan[:6])
# 0から最後まで
print(jinshiyuan[6:])
# 後ろから取得
print(jinshiyuan[-4:])

python = "Python is Amazing"
# 小文字変換
print(python.lower())
# 大文字変換
print(python.upper())
# 大文字判定
print(python[0].isupper())
# 文字の長さ
print(len(python))
# リプレース
print(python.replace("Python", "Java"))
# 文字インデックス取得
index = python.find("i")
print(index)
# 指定インデックス以降から検索
index = python.find("i", index + 1)
print(index)
# あり：インデックス　なし: -1
print(python.find("Python"))
# あり：インデックス　なし: エラー findと基本同じ、ない場合はエラー
# print(python.index("Python-"))
# 指定数値がの個数を取得
print(python.count("n"))
# 文字列結合
print("a" + "b")
# 文字列結合 ,がスペースになる
print("a", "b")

print("結合テスト %d" % 20)
print("結合テスト %s" % "成功")
print("結合テスト %c功" % "成")
# 基本sでよい
print("結合テスト %s%s" % ("成", "功"))
print("結合テスト {0}".format("成功"))
print("結合テスト {}{}".format("成", "功"))
print("結合テスト {0}{1}".format("成", "功"))
print("結合テスト {1}{0}".format("成", "功"))
print("結合テスト {a}{b}".format(a="成", b="功"))
print("結合テスト {b}{a}".format(a="成", b="功"))

# python3.6から
a = 20
b = "f"
print(f"結合テスト {b}{a}")

# \n 改行
print("fjdklasjfklas\njfladlsfal")

print("fjdklasjf\"klas\"jfladlsfal")

print("fjdklasjf\\klas\\jfladlsfal")

# \r 先頭に移動
print("fjd klasjf\raaa")
# \b 最後に移動
print("fjd klasjf\baaa")
# \t タブ
print("fjd klasjf\taaa")

test = "http://naver.com"
test = test[7:]
print(test)

# test = test.replace(".com", "")
test = test[:test.find(".")]
print(test)

a = test[0:3]
b = len(test)
c = test.count("e")

final = f"{a}{b}{c}!"
# final =  test[:3] + len(test) + test.count("e") + "!"
print(final)

# 0埋める
for num in range(1, 21):
    print(str(num).zfill(3))
