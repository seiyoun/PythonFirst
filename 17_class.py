from typing import NamedTuple


class Unit:
    def __init__(self, name, arg):
        """コンストラクタ

        Args:
            name ([type]): [description]
            arg ([type]): [description]
        """
        self.name = name
        self.arg = arg
        print(self.name)
        print(self.arg)

    def test_function(self):
        """テスト関数
        """
        print("test_function")


test = Unit("Unit", 31)
print(test.name)
print(test.arg)

test.name = "no jin"
print(test.name)

# other追加できる
test.other = "other"
print(test.other)

test.test_function()

# --------------------継承


class Unit2(Unit):
    def __init__(self, name, arg, language):
        #Unit.__init__(self, name, arg)
        super().__init__(name, arg)
        self.language = "china"

        print(self.language)


test2 = Unit2("Unit2", 31, "china")
print(test2.language)

test2.test_function()

# --------------------多重継承


class Weapon:
    def __init__(self, name):
        self.name = name


class Unit3(Unit, Weapon):
    def __init__(self, name, age, weapon_name):
        Unit.__init__(self, name, age)
        Weapon.__init__(self, weapon_name)


weapon = Unit3("Unit3", 31, "銃")
print(weapon.name)

# -------------------オーバーライド


class Unit4(Unit):
    def __init__(self):
        Unit.__init__(self, "Unit4", 31)

    def test_function(self):
        super().test_function()

        """テスト関数
        """
        print("Unit4 test_function")

    def test_function2(self):
        self.test_function()


unit4 = Unit4()
unit4.test_function()
unit4.test_function2()
