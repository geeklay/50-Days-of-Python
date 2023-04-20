def register_check(d):
    s = 0
    for i in d:
        if d[i] == 'yes': 
            s+=1
    return s

def lower_name(l):
    return tuple(i for i in l if i.islower())