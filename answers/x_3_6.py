# x_3_6
#
# 実行すると「好きなどうぶつを入力してください:」と表示され、キーボードから動物名が入力できます
# 「ねこ」の鳴き声を表示できるようにコードを追加してください

animal = input('好きなどうぶつを入力してください:')

if animal == 'いぬ':
    print('ワンワン')
elif animal == 'さる':
    print('ウッキッキー')
elif animal == 'にわとり':
    print('コケコッコー')
elif animal == 'ねこ':
    print('ニャーニャー')
else:
    print('？？？')
