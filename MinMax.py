def getMinMax(arr): 
    n = len(arr) 
    if(n % 2 == 0):                 # If array has even number of elements then  
         mx = max(arr[0], arr[1])   # initialize the first two elements as  minimum and maximum
         mn = min(arr[0], arr[1]) 
         i = 2                     # set the starting index for loop
    else:
        mx = mn = arr[0]
        i = 1                      # set the starting index for loop
    
    while(i < n - 1):               ## In the while loop, pick elements in pair and  
        if arr[i] < arr[i + 1]:                          # compare the pair with max and min so far  
            mx = max(mx, arr[i + 1]) 
            mn = min(mn, arr[i]) 
        else: 
            mx = max(mx, arr[i]) 
            mn = min(mn, arr[i + 1]) 
            i += 2

    return (mx,mn)


arr = [1000, 11, 445, 1, 330, 3000] 
print(getMinMax(arr)) 
