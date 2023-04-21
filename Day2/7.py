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