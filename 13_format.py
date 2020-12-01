# スペースを10個確報(左)
print("{0: >10}".format(500))

print("{0: >+10}".format(500))

print("{0: >+10}".format(-500))

print("{0:_<10}".format(-500))

# カンマ区切り
print("{0:,}".format(10000000))

print("{0:,}".format(-10000000))

print("{0:^<30,}".format(-10000000))

# 小数点
print("{0:f}".format(10))
# 小数点2桁まで
print("{0:.2f}".format(10))


