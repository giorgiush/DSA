from random import randint
from time import time


def bubblesort(list):
    remaining = len(list)
    for _ in list:
        sorted = True
        for i in range(remaining-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        remaining -= 1
        if sorted:
          return list
    return list
        

def selectionsort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[min_index], list[i] = list[i], list[min_index]
    return list


def insertionsort(list):
    for i in range(len(list)-1):
        current = i+1
        while current != 0 and list[current] < list[current-1]:
            list[current], list[current-1] = list[current-1], list[current]
            current -= 1
    return list


randlist = [randint(1, 100657657650000) for _ in range(2000)]


start = time()
x = bubblesort(randlist)            
print(x[0], x[1], x[-1])
print(time()-start)

print(f"\n")

start = time()
x = selectionsort(randlist)            
print(x[0], x[1], x[-1])
print(time()-start)

print(f"\n")

start = time()
x = insertionsort(randlist)       
print(x[0], x[1], x[-1])
print(time()-start)