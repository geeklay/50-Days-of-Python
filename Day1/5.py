def mydiscount():
    print("What is the price of the item: ")
    price = int(input())
    print("What is the discount amount (%): ")
    discount = input()
    print(price - (price * int(discount[:discount.index('%')]) / 100))

mydiscount()