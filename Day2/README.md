### Day 6
```python
def user_name():
    print("Insert email: ")
    uname = input()
    assert type(uname)==type('')
    print("Username: " + uname.partition('@')[0])

def zeroed(l):
    l[0] = 0
    l[len(l)-1] = 0
    return l

user_name()
print(zeroed([2,5,7,8,9]))
```
### Day 7
```python
#string_range = takes a single number and returns a string of its range seperated by dots.

def string_range(q):
    return '.'.join(str(i) for i in range(0,q))
#dict_names = returns all names that start with S and includes a count in a dict.
def d_names(l):
    d = dict()
    for i in l:
        if(i[0].casefold()=='s'):
            d[i] = d.get(i,0)+1
    return d

print(string_range(20))
q = d_names(["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"])
print(q)
```
### Day 8
```python
def odd_even(l):
    n = m = 0
    for i in l:
        if(i % 2 == 0 and i > n):
            n=i
        elif(i > m):
            m=i
    return n-m

#Uses sieve of erastothenes... 
def prime_numbers(n):
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j]=False
        
    res = [i for i in range(0,n) if sieve[i]]
    print(res.index(1))
    return res
        

k = odd_even([1,2,4,6])
print(k)
print(prime_numbers(10))


```
### Day 9
```python
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
```
