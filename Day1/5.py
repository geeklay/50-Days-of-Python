def mydiscount():
    print("What is the price of the item: ")
    price = int(input())
    print("What is the discount amount (%): ")
    discount = input()
    print(price - (price * int(discount[:discount.index('%')]) / 100))

def students(l):
    k = [i.casefold() for i in l ]
    m = k.count("male")
    f = k.count("female") 
    return [("Male", m), ("Female", f)]



mydiscount()
 
a = students(['Male', 'Female', 'male', 'male', 'male', 'female', 'male',
          'Female', 'Male', 'Female', 'Male', 'female'])
print(a)
