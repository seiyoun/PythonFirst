from random import *

print(random())  # 0.0~1.0ランダム
print(int(random() * 10))  # 0~9ランダム
print(int(random() * 10) + 1)  # 1~10ランダム

print(int(random() * 45) + 1)  # 1~10ランダム

print(int(randrange(1, 46)))  # 1~45ランダム
print(randint(1, 45))  # 1~45ランダム
