
#テスト
print('Hello, World!')
print(1 + 2)

# ギガ数
gb_price=1000
print('①毎月インターネットはどれくらい使いますか')
print ('次の1,2,3,4から該当する数字を入力してください。')
print('①１ギガ未満\n②２ギガ\n③３ギガ\n④それ以上')

input_count = input('①毎月使用するギガ数を上の番号から入力してください：')

count = int(input_count)
total_price = gb_price * count
gb_count=0

if count == 1:
    gb_count = 1980
elif count == 2:
    gb_count = 2980
elif count == 3:
    gb_count = 3980
elif count == 4:
    gb_count = 4980


#通話
print ('②通話はどれくらい使いますか。')
print ('次の1,2,3から該当する数字を入力してください。')
print ('1,ほとんど使わない \n2,５分以内で終わる通話がほとんど \n3,頻繁に通話を使用する')

input_call = input('毎月の通話量を上の番号から選択してください。：')

call_count=0
count2 = int(input_call)

if count2 == 1:
    print('ほとんど使わない')
    call_count = 980
elif count2 == 2:
    print('５分以内で終わる通話がほとんど')
    call_count = 1480
elif count2 == 3:
    print('頻繁に通話を使用する')
    call_count = 2480


#スマートバリュー
print('③お家のインターネット環境はauでしょうか。')
print('1,はい\n2,いいえ')

input_sv = input('ネット環境の有無を上の番号から入力してください：')

sv = int(input_sv)
sv_count=0

if sv == 1:
    sv_count = -500
elif sv == 2:
    sv_count = 0


print('毎月の携帯代金は')
print (+int(gb_count)+int(call_count)+int(sv_count))
print('円になります。')
