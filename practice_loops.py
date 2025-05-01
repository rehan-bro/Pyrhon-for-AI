# que:1 => Print all elements in a list using for loop
# list1 = [1,2,3,4,5] 
#output: 1 2 3 4 5

print("Enter 5 numbers:")
list1 = []
for i in range(5):
    list = int(input()) 
    list1.append(list)
print(list1)

# print(help(list1))


# 1 2 3 4 5 
nums = list(map(int, input("Enter 5 numbers: ").split()))
print(nums)

n = int(input("Enter range number: "))
list = []
for i in range(n):
    num = int(input("Enter numbers: "))
    list.append(num)
    
print(f"The numbers are: {list}")
    
    
# calculate the sum of all numbers in a list using for loop

n = int(input("Enter range number: "))
list = []
for i in range(n):
    num = int ( input("Enter numbers: "))
    list . append(num)

print(f"The numbers are: {list}")
sum = 0
for i in range(len(list)):
    sum += list[i]

print(f"The sum of all numbers is: {sum}")



# use nested for loop to print a pattern
# *
# * *
# * * *
# * * * *

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()



# use while loop to find the first number divisible by 7 starting from 50

num = 50 # initialization
while num>=50: # condition
      if num % 7 == 0:
          print(num)
          break
      num += 1 # increment
      
      
      