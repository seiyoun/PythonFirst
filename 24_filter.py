def inc2(value):
    if value % 2 == 0:
        return True
    return False


for item in filter(inc2, list):
    print(item)
