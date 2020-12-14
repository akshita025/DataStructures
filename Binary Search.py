def BinSrch(ls,l,r,x):
    #[1,2,3,4,5,6,7]
    while l<=r:
        mid=(l+r)//2
        #Check if x is present at mid
        if ls[mid]==x:
            return mid
        
        #Check if x is greater than mid value, ignore the left hand part
        elif x>ls[mid]:
            l=mid+1
            
        #Check if x is less than mid value, ignore the right hand part
        else:
            r=mid-1
    # -1 will be returned if l>r, i.e. x is not present in the sequence        
    return -1

ls = [2,3,4,10,40] 
x = 40
        
result=BinSrch(ls,0,len(ls)-1,x)
    
if result != -1:
    print("Element is present in the given sequence at index:", result )
else:
    print("Element is not present in the given sequence")