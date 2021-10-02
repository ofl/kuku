# x_3_2
#
# 正しいか正しくないかを表すデータの型を「真偽値(boolean)」と呼びます
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

print(100 > 90 and 85 < 90)
print(100 < 90 and 85 < 90)
print(100 >= 90 or 85 < 90)
print(100 == 90 or 85 < 90)

a = 100 < 70 or 70 > 65                  # => True
b = 60 >= 60 and (60 > 100 or 97 < 100)  # => True
c = 60 < 30 or not 40 < 60               # => False
d = 75 != 89 and not (100 < 50)          # => True(「not」は右の判定の否定)

# print(a)
# print(b)
# print(c)
# print(d)
