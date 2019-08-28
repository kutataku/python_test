
#テスト
print('Hello, World!')
print(1 + 2)



#携帯電話料金シミュレーター

# ギガ数
print('①毎月インターネットはどれくらい使いますか')
print ('次の1,2,3,4から該当する数字を入力してください。')
print('①１ギガ未満\n②２ギガ\n③３ギガ\n④それ以上')

input_count = input('①毎月使用するギガ数を上の番号から入力してください：')

count = int(input_count)
au_gb=0
sb_gb=0
dc_gb=0


if count == 1:
    au_gb = 1980
    dc_gb = 2980
    sb_gb = 2480
elif count == 2:
    au_gb = 2980
    dc_gb = 4000
    sb_gb = 4480
elif count == 3:
    au_gb = 3980
    dc_gb = 4000
    sb_gb = 5980
elif count <= 4:
    au_gb = 4980
    dc_gb = 5000
    sb_gb = 6980


#通話
print ('②通話はどれくらい使いますか。')
print ('次の1,2,3から該当する数字を入力してください。')
print ('1,ほとんど使わない \n2,５分以内で終わる通話がほとんど \n3,頻繁に通話を使用する')

input_call = input('毎月の通話量を上の番号から選択してください。：')

au_call=0
sb_call=0
dc_call=0
count2 = int(input_call)

if count2 == 1:
    print('ほとんど使わない')
    au_call = 980
    sb_call=1200
    dc_call=980
elif count2 == 2:
    print('５分以内で終わる通話がほとんど')
    au_call = 1480
    sb_call=1700
    dc_call=1200
elif count2 == 3:
    print('頻繁に通話を使用する')
    au_call = 2480
    sb_call=2700
    dc_call=2700


#スマートバリュー
print('③お家のインターネット環境は携帯会社とセットでしょうか。')
print('1,はい\n2,いいえ')

input_sv = input('ネット環境の有無を上の番号から入力してください：')

sv = int(input_sv)
au_sv=0
sb_sv=0
dc_sv=0


if sv == 1:
    au_sv = -500
    sb_sv= -1000
    dc_sv= -1000
elif sv == 2:
    sv_count = 0
    sb_sv=0
    dc_sv=0

au = int(au_gb)+int(au_call)+int(au_sv)
sb = int(au_gb)+int(sb_call)+int(sb_sv)
dc = int(au_gb)+int(dc_call)+int(dc_sv)

print('auにした場合、毎月の携帯代金は')
print(au)
print('になります')

print('softbankにした場合、毎月の携帯代金は')
print(sb)
print('になります')

print('ドコモにした場合、毎月の携帯代金は')
print(dc)
print('になります')
