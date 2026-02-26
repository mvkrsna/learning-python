#TypeCasting = the process of converting a variable from
# one data type to another
#str(), float(), int(), bool()

name = "Hello bro"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

float_age = float(age)
print(float_age)

checkName="Jack"
newName = bool(checkName)
print(newName)#True

checkName=""
newName = bool(checkName)
print(newName)#False

