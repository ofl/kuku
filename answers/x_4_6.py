# x_4_6
#
# 入力した文章が全て１行づつ表示されるように修正してください
# ヒント: 文章の長さを測るにはどうすればよかったでしょうか？

text = input('何か文章を入力してください:')

number = 0

while number < len(text):
    print(text[number])
    number += 1
