'''
The way this algorithm works is 
first we define a pivot point as a reference we can use any point as a reference but here we are using last value from our input list

and then we make two list namesd as lower and heigher and we append value respective to the pivot point to the respective list 

and we done the same process over and over again till the condition breaks 
'''


def short1(List):
    length = len(List)
    lower = []
    heigher = []
    if length <= 1:
        return List
    else:
        pivot = List.pop()
    for i in List:
        if i >= pivot:
            heigher.append(i)
        else:
            lower.append(i)
    return short1(lower) + [pivot] + short1(heigher)


print(short1([1, 5, 2, 6, 8, 4, 8, 3, 8, 0, 5, 0]))
