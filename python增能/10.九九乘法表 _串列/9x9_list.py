listA=[]
listB=[]

for i in range(1,10):
    for j in range(1,10):
        listA.append(str(i)+"*"+str(j)+"="+str(i*j))
    listB.append(listA[:])  #冒號前後不加數字代表全部
    listA.clear()   #清空串列中的所有元素
    
#print(listA)
print(listB)