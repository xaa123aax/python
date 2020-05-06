import random

English = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]

#ord取得ASCII A為65
EnglishUID=chr(random.randint(0, 25)+65)
Englishnumber=English[ord(EnglishUID)-65]

j=7
UID = []

#print(EnglishUID)
#print(Englishnumber)


total=Englishnumber//10+Englishnumber%10*9
first=random.randint(1,2)
total=total+first*8

UID.append(int(Englishnumber / 10))
UID.append(Englishnumber % 10)
UID.append(first)
#print(UID)
for i in range(1,8):    
    a=random.randint(0,9)
    UID.append(a)
    total=total+a*j

last=int(10-total%10)
UID.append(last)
print(total)
print(UID)

print(EnglishUID+str(UID[2])+str(UID[3])+str(UID[4])+str(UID[5])+str(UID[6])+str(UID[7])+str(UID[8])+str(UID[9])+str(UID[10]))