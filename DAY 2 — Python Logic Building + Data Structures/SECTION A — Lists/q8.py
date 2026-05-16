# Write a program that merges two dictionaries into one.

products = {
    "Laptop": 94999,
    "Mobile": 46000,
    "Headphones": 2500,
    "Smartwatch": 8000
}

phone_no = {
    "Shahnawaz": 8595021420, 
    "Abdullah": 9891944054, 
    "Rayyan": 9315201620
    }

new_dict = products|phone_no
print(new_dict)