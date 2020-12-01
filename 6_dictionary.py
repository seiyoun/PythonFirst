cabinet = {3: "a", 100: "v"}
print(cabinet)

print(cabinet[3])

print(cabinet.get(3))

# エラー発生
# print(cabinet[5])

# Noneを返す
print(cabinet.get(5))

print(cabinet.get(5, "not found 5"))

# True
print(3 in cabinet)

# add
cabinet[4] = "d"
print(cabinet)

# remove
del cabinet[4]
print(cabinet)

# keys
print(cabinet.keys())

# values
print(cabinet.values())

# クリア
# print(cabinet.clear())

print(cabinet.items())

score = {"a": 1, "b": 2}
for a, b in score.items():
    print(a, end="-")
    print(b)
