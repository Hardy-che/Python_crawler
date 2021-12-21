def price(age):
    if age < 6:
        print('price is 0')
    elif age < 18:
        print('price is 50')
    elif age < 60:
        print('price is 100')
    else:
        print('price is 60')
        
age = int(input("input you age"))
price(age)
