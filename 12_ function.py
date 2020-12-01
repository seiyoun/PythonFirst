def test():
    """テスト関数
    """
    print("call test")


test()


def return_test():
    """戻り値テスト関数

    Returns:
        string: 適当な文字
    """
    return "call return test"


print(return_test())


def return_test2(money):
    """引数ありテストテスト

    Args:
        money (int): 適当

    Returns:
        string: 適当な文字
    """
    return f"call return test {money}"


print(return_test2(10))


# tuple型を返す
def return_test3(cat, dog):
    """tuple戻り値テスト関数

    Args:
        cat ([type]): [description]
        dog ([type]): [description]

    Returns:
        [type]: [description]
    """
    cat = cat.upper()
    dog = dog.upper()
    return cat, dog


print(return_test3("Cat", "doG"))


def profile(name, age, lang="china"):
    """デフォルト引数

    Args:
        name ([type]): [description]
        age ([type]): [description]
        lang (str, optional): [description]. Defaults to "china".
    """
    print(f"名前:{name} 年齢:{age} 言語:{lang}")


profile("jin", 31, "japan")
profile("jin2", 31)

profile(name="jin", lang="china", age=31)


def profile2(*language):
    """引数テスト関数
    """

    for lang in language:
        print(lang)


profile2("china", "english")

value = 10


def checkpoint():
    global value
    value += 1


print(value)


def checkpoint2(value):
    return value + 1


value = checkpoint2(value)
print(value)
