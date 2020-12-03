for wating_no in [1, 2, 3, 4]:
    print(wating_no)

print("---------")

for num in range(0, 10):
    print(num)

print("---------")

for num in range(1, 10):
    if num > 5 and num < 7:
        continue
    print(num)

print("---------")

for num in range(1, 10):
    if num > 5:
        break
    print(num)

print("---------")
test2 = [i + 10 for i in range(0, 11)]
print(test2)


print("---------")
test2 = [i.upper() for i in ["a", "b", "c"]]
print(test2)

print("---------")
lst = ["a", "b", "c"]
for index, value in enumerate(lst):
    print(f"インデックスは{index}/値は{value}")
