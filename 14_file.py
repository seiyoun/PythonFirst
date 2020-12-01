# 書き込み(上書き)
# testFile = open("file.txt", "w", encoding="utf8")
# print("test", file=testFile)
# testFile.close()

# 書き込み(追記)
# testFile = open("file.txt", "a", encoding="utf8")
# testFile.write("test3\n")
# testFile.close()

# 読み込み(全体)
# testFile = open("file.txt", "r", encoding="utf8")
# txt = testFile.read()
# print(txt)
# testFile.close()

# 読み込み(行)
# testFile = open("file.txt", "r", encoding="utf8")
# # end=""改行しない
# print(testFile.readline(),end="")
# print(testFile.readline())
# print(testFile.readline())
# print(testFile.readline())
# testFile.close()

# 読み込み(全体)
# testFile = open("file.txt", "r", encoding="utf8")
# while True:
#     line = testFile.readline()
#     if not line:
#         break
#     print(line, end="")
# testFile.close()

# 読み込み(全体)
testFile = open("file.txt", "r", encoding="utf8")
lines = testFile.readlines()
for line in lines:
    print(line, end="")
testFile.close()
