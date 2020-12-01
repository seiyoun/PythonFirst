import pickle

# 書き込み
# file = open("pickle_test.pickle", "wb")
# txt = {"name": "jin shiyuan", "age": 31}
# print(txt)
# pickle.dump(txt, file)
# file.close()

# 読み込み
file = open("pickle_test.pickle", "rb")
txt = pickle.load(file)
print(txt)
file.close()
