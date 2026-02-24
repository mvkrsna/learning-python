#Variable - is a container to hold values of (string, integer, float, boolean)

#strings
name = "Bro"
print(name)

#Formatted Variables
formatted_name = f"hello {name}"
print(formatted_name)

#Integers
age = 25
print(age)
print(f"Hello {name} you are {age} years old")
print("Hello " + name + " you are " + str(age) + " years old")
print("Hello", name, "you are", age, "years old")
print("Hello %s you are %d years old" % (name, age))


#Float
price= 10.99
print(f"The price is {price} Dollars")
print("The Price is", price, "Dollars")


#Boolean
is_student = False

if is_student:
    print("you are a student")
else:
    print("you are NOT a student")

#2nd Example
for_sale = True
if for_sale:
    print("That item is for Sale")
else:
    print("That time is NOT for available")

#3rd Example
is_Online = True
if is_Online:
    print(f"hey {name}, you are Online")
else:
    print(f"hey {name}, you are Offline")
