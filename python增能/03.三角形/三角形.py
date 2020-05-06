a=int(input("請輸入a的邊長"))
b=int(input("請輸入b的邊長"))
c=int(input("請輸入c的邊長"))


if a+b>c:
    print("可以圍成三角形")
    if a*a+b*b>c*c:
        if a==b or b==c:
            if a==c:
                print("並且是正三角形")
            else:
                print("並且是等腰銳角三角形")        
        else:
            print("並且是銳角三角形")        
    elif a*a+b*b==c*c:
        if a==b or b==c:
            print("並且是等腰直角三角形")        
        else:
            print("並且是直角三角形")
    elif a*a+b*b<c*c:
        if a==b or b==c:    
            print("並且是等腰鈍角三角形")
        else:
            print("並且是鈍角三角形")
    
else:
    print("不可以圍成三角形")