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