#Take string and return largest odd number -- '23569' = 9 "Use list comprehension"
# Pretty sure this isn't the solution solution... but it'll do...
def biggest_odd(st):
    return max(int(i) for i in st) 

#Puts 0 at end of list. If there are no 0s it sorts the list in ascending order.
def zeros_last(l):
    if(l.count(0)==0):
        l.sort()
        return l
    while(l.index(0) != len(l)-l.count(0)): 
        l.remove(0)
        l.append(0)
    return l


print(biggest_odd("23569123"))

print(zeros_last([1,4,6,0,7,0,9]))

print(zeros_last([2,1,4,6,7]))

print(zeros_last([1,4,0,1,4,9,91,0,0,1,3,0,6,0,7,0,9]))