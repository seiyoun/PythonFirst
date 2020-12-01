# -----------------Module File Path
# import inspect
# import random

# print(inspect.getfile(random))

# -----------------Dir
# print(dir())
# print(dir(random))

# list = [1, 2, 3]
# print(dir(list))

# import glob
# print(glob.glob("*.py"))

# -----------------OS

# import os
# カレントディレクトリ
# print(os.getcwd())

# フォルダチェック
# if os.path.exists("sample"):
#     print("True")
#     # フォルダ削除
#     os.rmdir("sample")
# else:
#     print("False")
#     # フォルダ生成
#     os.makedirs("sample")

# 全ファイル取得
# print(os.listdir())

# -----------------Time
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H-%M-%S"))

# -----------------DateTime
# import datetime
# print(datetime.date.today())

# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print(today + td)
