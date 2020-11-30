list = ["a", "b", "c"]
print(list.index("a"))

list.append("d")
print(list)

list.insert(0, "Z")
print(list)

list.remove("a")
print(list)

value = list.pop()
print(value)
print(list)

list.append("c")
print(list.count("c"))

list.sort()
print(list)

list1 = [5, 4, 3, 2, 1]
list1.sort()

print(list1)

mix_list = ["a", 20, True]
print(mix_list)

list1.extend(mix_list)
print(list1)
