def quicksort(ls):
    #move all the elements to the left that are less than first element
    pivot = swap = 0
    for i in range(len(ls)):
        if ls[i] < ls[pivot]:
            swap += 1
            ls[i], ls[swap] = ls[swap], ls[i]
    ls[pivot], ls[swap] = ls[swap], ls[pivot]
    
    #base case
    if len(ls) <2:
        return ls
    
    #split and sort recursively
    right = quicksort(ls[swap+1:])
    left = quicksort(ls[:swap+1])
    return left + right