# x_2_9
#
# 実行すると「バナナを何房買いましたか？:」と表示され、キーボードから数字が入力できます
# バナナとリンゴを買った合計金額を表示してください

banana = 200
apple = 100

banana_count = input('バナナを何房買いましたか？:')
apple_count = input('リンゴを何個買いましたか？:')

total = banana * int(banana_count) + apple * int(apple_count)

print('合計は' + str(total) + '円です')
