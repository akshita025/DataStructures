def insertion_sort(l):
    for i in range(1,len(l)):
        key=l[i]
        flag=0
        flag1=0
        for j in range(i-1,-1,-1):
            if l[i]<l[j]:
                flag=1
                continue
            else:
                flag1=1
                break
        if flag==1:
            l.remove(key)
            if flag1==1:
                l.insert(j+1,key)
            else:
                l.insert(j,key)
    return l
insertion_sort([4,3,7,1,8,0,2])