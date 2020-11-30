# 一般
def test():
    print("call test")


test()


# 戻り値
def return_test():
    return "call return test"


print(return_test())


# 引数
def return_test2(money):
    return f"call return test {money}"


print(return_test2(10))


# tuple型を返す
def return_test3(cat, dog):
    cat = cat.upper()
    dog = dog.upper()
    return cat, dog


print(return_test3("Cat", "doG"))

# デフォルト引数


def profile(name, age, lang="china"):
    print(f"名前:{name} 年齢:{age} 言語:{lang}")


profile("jin", 31, "japan")
profile("jin2", 31)

profile(name="jin", lang="china", age=31)


def profile2(*language):
    for lang in language:
        print(lang)


profile2("china", "english")
