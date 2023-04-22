```python
from getpass import getpass
#hide password, just *s out the password and tells the user the number of characters
def hide_password():
    pw = getpass()
    print('Password is ' + str(len(pw)-1)+' characters long.') 
    return ''.join(['*' for i in range(len(pw)-1)])

#the "cheesy" method of adding a thousand separator to a list of numbers.
def convertnum(ln):
    return [f"{i:,}" for i in ln]

def unconvertnum(ln):
    return [f'i' for i in ln]

p = hide_password()
print(p)

o = convertnum([1000000,2356989,2354672,9878098])
print(o)
```
