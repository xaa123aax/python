import math


s=[1,2,5,6,1]

print(s)

def mergeList(leftList, rightList):

     if len(leftList) == 0: 
         return rightList 
     elif len(rightList) == 0: 
         return leftList 
    
     elif leftList[0] < rightList[0]:
         return [leftList[0]] + mergeList(leftList[1:], rightList)

     else: 
         return [rightList[0]] + mergeList(leftList, rightList[1:])


def chopList(sourceList):
    

     if 1 >= len(sourceList):
         return sourceList

     centerKey = int(round(len(sourceList)/2))
     leftList = []
     rightList = []

     leftList = sourceList[0:centerKey]
     rightList = sourceList[centerKey:]

     leftData = chopList(leftList)
     rightData = chopList(rightList)

     return mergeList(leftData, rightData)


print(chopList(s))

 
