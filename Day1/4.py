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