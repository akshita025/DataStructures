def bubbleSort(l):
    while True:
        x=0
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
                x=1
        if x==0:
            return l
            break
bubbleSort([67,12,34,0,90])