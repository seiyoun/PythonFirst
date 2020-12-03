import functools

# -------------------------map
list = [1, 2, 3, 4]


def inc(value):
    return value + 1


m = map(inc, list)

for item in m:
    print(item)

for item in map(lambda v: v + 1, list):
    print(item)

# -------------------------

list2 = ["A", "B", "C", "D"]


def inc2(value):
    return value + "add"


m2 = map(inc2, list2)

for item in m2:
    print(item)


# -------------------------reduce


def add(value1, value2):
    return value1 + value2


m3 = functools.reduce(add, list)

print(m3)
