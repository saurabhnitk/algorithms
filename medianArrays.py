def getMedian(arr1,arr2,n):
    i,j=0,0
    count=0
    m1,m2 = -1,-1
    while count < n+1:
        count += 1
        if i==n:
            m1=m2
            m2 = arr2[0]
            break
        elif j==n:
            m1=m2
            m2 = arr1[0]
            break
        if arr1[i] < arr2[j]:
            m1=m2
            m2 =  arr1[i]
            i += 1
        else:
            m1 = m2
            m2 = arr2[j]
            j += 1
    return (m1+m2)/2

arr1 = [1, 12, 15, 26, 38] 
arr2 = [2, 13, 17, 30, 45] 
n1 = len(arr1) 
n2 = len(arr2) 
if n1 == n2: 
    print("Median is ", getMedian(ar1, ar2, n1)) 
else: 
    print("Doesn't work for arrays of unequal size") 
