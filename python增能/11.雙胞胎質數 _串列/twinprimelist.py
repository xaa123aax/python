primelist = []
twinlist = []

#質數
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True

#一萬以內如果是質數就丟入list
for i in range(2, 10001):
    if prime(i):
        primelist.append(i)


for j in range(1,len(primelist)-1): #計算總list長度=總數
    if primelist[j+1]-primelist[j]==2: #兩個質數相減等於2
        twinlist.append([primelist[j],primelist[j+1]])
        
print(twinlist)
print('共有' + str(len(twinlist)) + '對孿生質數')