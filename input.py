name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")

#if you want to check the types of the variables
# without defining them , its always string as str
print(type(name), type(age))

#if you want age as int
age = int(age)
print(f"Hello, {name}! You are {age} years old.")

#here age is int
print(f"Here age is {age} and type of age is {type(age)}")
#here name is str   
print(f"Here name is {name} and type of name is {type(name)}")

