while True:
    identity = input('請輸入身份證字號')
        #檢驗第一位是否為大寫       #檢驗第二位是否為1或2(男性1女性2)               #總長度要為10
    if identity[0].isupper() and (identity[1] == '1' or identity[1] == '2' and len(identity) == 10):
        break
    else:
        print("格式錯誤，請再輸入一次")
English = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]

#ord取得ASCII A為65
Englishnumber=English[ord(identity[0])-65]

j=8

#第一個數字除十取整加上第二個數字取餘數*9
total=Englishnumber//10+Englishnumber%10*9

#print(total)

for i in identity[1:]:    

    total=total+int(i)*j
    #print(int(i))
    #print(j)
    #print(int(i)*j)

    #最後兩個數字是1
    if j!=1:
        j=j-1
    print(total)

if total%10==0:
    print("正確")
else:
    print("錯誤")


