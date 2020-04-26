n1=int(input("請輸入一個數"))
n2=int(input("請再輸入一個數"))
print(str(n1)+"跟"+str(n2))

def gcd(n1,n2):
    if n1%n2!=0:
        left=n2
        right=n1%n2
        gcd(left,right)
    else:
        print('的最大公因數為'+str(n2))

gcd(n1,n2)
