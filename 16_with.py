import pickle
from pickle import encode_long

# 読み込み(クローズを省略)
# with open("pickle_test.pickle", "rb") as file:
#     print(pickle.load(file))

# with open("with_file.txt", "w", encoding="utf8") as file:
#     file.write("with テスト")

with open("with_file.txt", "r", encoding="utf8") as file:
    print(file.read())
