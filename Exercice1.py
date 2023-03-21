from functools import reduce
import operator

# declaring the list
li = [170, 3.8, 0, 22, 7.2, 55, 18]
# Sorting the list
li.sort()
# Displaying the list
print(li)
# adding <<0.05>> to the list
li.append(.05)
print(li)
# dropping 170 from the list
li.remove(170)
print(li)
# finding the index of 22
print("the index of 22: ", li.index(22))
# printing a sub-list that starts from the 3rd element of the list and goes up to the end of the list
print(li[2:])
# calculating the sum of all the element of the list
sum = 0
for i in li:
    sum += i
print("the sum is: ", sum)
# calculating the multiplication
mul_list = reduce(operator.mul, li[0: ])
print("the mul is: ", mul_list)
# Creating a sequence of integers from 0 to 15 (not included) in steps of 3
for i in range(0, 15, 3):
    print(i)

