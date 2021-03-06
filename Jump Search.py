def jump_search(l,x):
    import math
    n=len(l)
    #calculating the step count with which we have to jump in the sequence
    step= int(math.sqrt(n))
    #Counter for step count
    cnt=0
    #maximum index of the list
    maxindex=l.index(l[-1])
    #Flag to check if value is present or not in the sequence
    flag=0
    #Flag to check if value is find using the indexes on which we'll jump using the step count
    stop=0
    #If the value present at the indexes using step count is greater than the value which is to be searched, the loop breaks
    while l[cnt]<=x:
        if l[cnt]==x:
            print(cnt)
            stop=1
            break
        else:
            cnt=cnt+step
            # To check if the step count is greater than the max index of the sequence
            if cnt>maxindex:
                break
    #Previous (prev) is the value after difference of current step count and step count found initially
    prev=cnt-step
    if stop==0:
        for i in range(prev+1,l.index(l[-1])+1):
            if l[i]==x:
                flag=1
                break
        if flag==1:
            return i
        else:
            return "not found in list"
