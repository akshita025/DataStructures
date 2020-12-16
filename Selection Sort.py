def selectionSort(l):
    for i in range(0,len(l)):
        """
        The current value will be set in minIndex
        """
        minIndx=i
        for j in range(i+1,len(l)):
            if l[minIndx]>l[j]:
                minIndx=j
        """
        Swapping the current index value and minIndex value
        """
        l[i],l[minIndx]=l[minIndx],l[i]
    return l

selectionSort([11,5,4,10,9,15,17,12,2])