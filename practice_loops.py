# que:1 => Print all elements in a list using for loop
# list1 = [1,2,3,4,5] 
#output: 1 2 3 4 5

print("Enter 5 numbers:")
list1 = []
for i in range(5):
    list = int(input()) 
    list1.append(list)
    list1.__reversed__(sort())
print(list1)

# print(help(list1))