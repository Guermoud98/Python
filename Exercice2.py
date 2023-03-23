import math
# Finding the unique elements in a list
def unique(list):
    li = []
    for i in list:
        if i not in li:
            li.append(i)
    return li
t = 5
list = []
while t != 0:
    num = int(input("give me an integer: "))
    list.append(num)
    t = t - 1
u = unique(list)
print(u)
# returning a new list containing the elements in common of two lists.
def unique (list1, list2):
    li = set(list1) & set(list2)
    return li
list1 = [1,2,3,9,10]
list2 = [1,3,10,12,15]
u = unique(list1,list2)
print(u)

# finding all the strings with a length > 4
def lengthSupFour(list):
    li = []
    for i in list:
        if len(i) > 4:
            li.append(i)
    return li
fruits = ["apple", "banana", "fig"]
fruits_list = lengthSupFour(fruits)
print(fruits_list)

# finding the integers > 10 
def supTen(list):
    li = []
    for i in list:
        if i > 10:
            li.append(i)
    return li
t = 5
list = []
while t != 0:
    num = int(input("give me an integer: "))
    list.append(num)
    t = t - 1
sup_ten = supTen(list)
print(sup_ten)

# Converting strings to Uppercase
def stringUpperCase(list):
    li = []
    for i in list:
        li.append(i.upper())
    return li
list = ["hello","world"]
li_upper = stringUpperCase(list)
print(li_upper)

# sum of elements in a list
def somme(list):
    s = 0
    for i in list:
        s += i
    return s
list = [1,2,3,4]
print("The sum of all the elements in the given list is ", somme(list))

# rteurning a list of the squares of integers.
def powList(list):
    carres_liste = []
    for i in list:
        carres_liste.append(math.sqrt(i))
    return carres_liste
list = [1,2,4]
li_pow = powList(list)
print(li_pow)

