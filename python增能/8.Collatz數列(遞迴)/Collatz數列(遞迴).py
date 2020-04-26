n=int(input("請輸入一個數"))
a=0
max=0

def collatz(n):
    print(n)
    global a
    global max
    a=a+1
    if n>=max:
        max=n

    if n!=1:
        if n%2==1:
            collatz(3*n+1)
        else:
            collatz(n/2)

collatz(n)


print("總共有"+str(a)+"個數字")
print('最大數字='+str(max))