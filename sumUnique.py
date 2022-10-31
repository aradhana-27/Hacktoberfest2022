def sumUnique(li):
    s=set()
    for i in li:
        s.add(i)
    sum=0
    for i in s:
        sum= sum + i
    return sum 


print(sumUnique([1,2,3,1,5,2,3,4,8,5,1,2]))