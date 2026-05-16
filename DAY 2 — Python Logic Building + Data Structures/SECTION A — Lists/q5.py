# Dictionaries and Dictionary Methods
# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:

# Print the value of "name".
# Change "grade" to "A+".
# Add a new key "city" with value "Delhi".
# Create a dictionary of three friends and their phone numbers. Use:

# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])
student["grade"] = "A+"
print(student["grade"])
student["city"] = "Delhi"
print(student)

phone_no = {"Shahnawaz": 8595021420, "Abdullah": 9891944054, "Rayyan": 9315201620}

print(phone_no.keys())
print(phone_no.values())
# print(phone_no.items())

for x, y in phone_no.items():
    print(x,y)