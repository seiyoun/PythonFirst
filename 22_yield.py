def no_list():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 5


# g = no_list()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for no in no_list():
#     print(no)


def my_range(start_no, end_no):
    no = start_no
    while end_no > no:
        yield no
        no += 1


for no in my_range(1, 6):
    print(no)
