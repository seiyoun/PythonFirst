try:
    value = 10
    value2 = "10"
    value3 = value / value2
except Exception as err:
    print(f"error{err}")
finally:
    print("thank you")

try:
    value = 10
    value2 = "10"
    value3 = value / value2
except:
    print("エラー")

# raiseを利用してエラーにする
try:
    value = 10
    raise ValueError
except ValueError:
    print("ValueError")

# 自作エラー


class TestError(Exception):
    def __init__(self, message):
        self.msg = message

    def __str__(self):
        return self.msg


try:
    value = 10
    raise TestError("エラー発生")
except TestError as err:
    print(err)
