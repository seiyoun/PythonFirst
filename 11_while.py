call = "call"
index = 5

while index > 0:
    print(call)
    index -= 1

    if index == 0:
        print(index)

# 無限ループ
index = 0
while True:
    print(call + str(index))
    index += 1
