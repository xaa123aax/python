n=int(input("請輸入一個數"))
a=1
while(n!=1):
    a=a+1
    if n%2==1:
        n=3*n+1
        print(int(n))
    else:
        n=n/2
        print(int(n))

print("總共有"+str(a)+"個數字")