# Create a phonebook:
# add name & number
# search number by name

# phone_book = {}
# n = int(input("How many contacts you want to add: "))
# for i in range(n):
#     name = input("Contact name: ")
#     number = input("Contact number: ")
#     phone_book[name]=number

phone_book = {
    "Shahnawaz": 8595021420,
    "Abdullah": 9891944054,
    "Rayyan": 9315201620,
    "Kaif": 9958455758,
    "Dad": 8802191092,
    "Mom": 9718950410,
    "Arbaz": 9971171706,
    "Arshad": 9311808018,
    "Sajid": 8700638850,
    "Ilma": 8527582495
}
search = input("Search contact: ").capitalize()

if search in phone_book:
    print(search,":",phone_book[search])
else:
    print("No contacts found.")