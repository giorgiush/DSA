def merge(ls1, ls2):
    
    combined = []
    i = j = 0
    
    while i != len(ls1) and j != len(ls2):
        
        if ls1[i] <= ls2[j]:
            combined.append(ls1[i])
            i += 1
        else:
            combined.append(ls2[j])
            j += 1
            
    for n in range(i, len(ls1)):
        combined.append(ls1[n])
    for n in range(j, len(ls2)):
        combined.append(ls2[n])
        
    return combined



def mergeSort(ls):
    
    if len(ls) == 1:
        return ls
    
    mid = len(ls)//2
    left = mergeSort(ls[:mid])
    right = mergeSort(ls[mid:])
    
    return merge(left, right)