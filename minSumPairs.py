# An Array of integers is given, both +ve and -ve. You need to find the two 
#elements such that their sum is closest to zero.
def minSumPair(arr,n):
    c=0
    if n<2:
        print("invalid input")
        return
    min_l,min_r = 0,1
    min_sum = arr[0] + arr[1]
    for i in range(n-1):
        for j in range(i+1,n):
            s = arr[i] + arr[j]
            if abs(min_sum) > abs(s):
                min_sum = s
                min_l = i
                min_r = j
    print(arr[min_l], arr[min_r])
    
arr = [1, 60, -10, 70, -80, 85] 
minAbsSumPair(arr, 6)


                
