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
