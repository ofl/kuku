# x_7_5
#
# 「桃太郎はヒットポイント:1800,攻撃力:230,守備力:200」のように１行づつ表示してください

members = [
    {
        '名前': '桃太郎',
        'ヒットポイント': 1800,
        '攻撃力': 230,
        '守備力': 200,
    },
    {
        '名前': 'いぬ',
        'ヒットポイント': 1300,
        '攻撃力': 180,
        '守備力': 150,
    },
    {
        '名前': 'さる',
        'ヒットポイント': 1400,
        '攻撃力': 150,
        '守備力': 180,
    },
    {
        '名前': 'きじ',
        'ヒットポイント': 1100,
        '攻撃力': 130,
        '守備力': 220,
    }
]

for member in members:
    print(member['名前'] + 'はヒットポイント:' + str(member['ヒットポイント']) +
          ',攻撃力:' + str(member['攻撃力']) + ',守備力:' + str(member['守備力']))
