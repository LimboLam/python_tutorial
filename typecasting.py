# typecasting = Turing a value to one data type to another
#               Explicit vs Implicit

name = 'Liam'
age = 17
gpa = 3.5
is_student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))

# Explicit Conversion

# age = float(age)
# print(type(age))

# gpa = int(gpa)
# print(type(gpa))

# is_student = str(is_student)
# print(type(is_student))

# age = bool(age)
# print(type(age))
# print(age)

# Implicit Conversion

x = 2
y = 2.0

x = x / y

print(type(x))