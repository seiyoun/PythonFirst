# 重複不可、順番なし
my_set = {"1", "2", "3", "3", "3", "3"}
print(my_set)

my_set = {"1", "2", "3", "3", "3", "3"}
my_set2 = {"1", "2", "4", "5", "6", "7"}

print(my_set & my_set2)
print(my_set.intersection(my_set2))

print(my_set | my_set2)
print(my_set.union(my_set2))

print(my_set - my_set2)
print(my_set.difference(my_set2))

# add
my_set.add("a")
print(my_set)

# remove
my_set.remove("a")
print(my_set)

a = my_set
print(a, type(a))

a = list(my_set)
print(a, type(a))

a = tuple(my_set)
print(a, type(a))
