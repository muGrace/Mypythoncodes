def address(street, city, postal_code):
     print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")
happy_new_year()    
def wishes():
     return "Happy Birthday!"

w = wishes()

print(w)    # outputs: Happy Birthday!





