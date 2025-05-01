# que:1 => Print all elements in a list using for loop
# list1 = [1,2,3,4,5] 
#output: 1 2 3 4 5

# print("Enter 5 numbers:")
# list1 = []
# for i in range(5):
#     list = int(input()) 
#     list1.append(list)
# print(list1)

# print(help(list1))


# 1 2 3 4 5 
# nums = list(map(int, input("Enter 5 numbers: ").split()))
# print(nums)

n = int(input("Enter range number: "))
list = []
for i in range(n):
    num = int(input("Enter numbers: "))
    list.append(num)
    
print(f"The numbers are: {list}")
    