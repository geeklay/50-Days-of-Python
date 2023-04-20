```python
from math import sqrt
def div_or_square(num):
    if num % 5 == 0: 
        return sqrt(num)
    return num % 5

def longest_value(x):
    l = 0 
    for i in x: 
        if len(str(x[i])) > l:
            l = len(str(x[i]))
            res = x[i] 
    return res             
    
print(div_or_square(int(input())))
print(longest_value(fruits))
```
### "Day 2"
```python
def conv_add(x):
    y = list(map(int,x))
    return y 
#Cake
def check_duplicates(x):
    q = []

    for i in x:
        if i not in q and x.count(i) > 1:
            q.append(i)

    if not len(q):
        return "No duplicates"

    return q 

n = conv_add(['1','2','5','8','10'])
print(n)
print(sum(n))

print(check_duplicates(['apple','orange','banana','apple']))
print(check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark']))
```

### "Day" 3
```python
def register_check(d):
    s = 0
    for i in d:
        if d[i] == 'yes': 
            s+=1
    return s

def lower_name(l):
    return tuple(i for i in l if i.islower())```python
def register_check(d):
    s = 0
    for i in d:
        if d[i] == 'yes': 
            s+=1
    return s

def lower_name(l):
    return tuple(i for i in l if i.islower())
```
### "Day 4"
```python
def only_floats(a, b):
    if type(a) == float and type(b) == float: return 2
    if type(a) == float or type(b) == float: return 1
    return 0

def word_index(l):
    j = 0
    r = 0
    for i in l:
        if len(i) > len(l[r]):
            r = j
        j+=1
    return r
    
a = only_floats(2.1, 0) 
b = only_floats(2.4, 3118.2)
c = only_floats(123, 123807)
words1 = ["Hate", "remorse", "vengeance"]
worse2 = ["Love", "Hate", "Fate", "Gate", "Bate"]
print(word_index(words1))
print(word_index(worse2))
print(a,b,c)
```
