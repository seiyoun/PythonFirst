# weather = input("今日の天気は:")

# if weather == "晴れ":
#     print("熱い")
# elif weather == "曇り":
#     print("涼しい")
# else:
#     print("寒い")


temp = (int)(input("数値を入力してください"))
if temp > 50:
    print("{0}>50".format(temp))
elif temp > 40:
    print(f"{temp} > 40")
else:
    print("{a} > 0".format(a=temp))
