import math
# Finding the unique elements in a list
def unique_element(list):
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
u = unique_element(list)
print(u)
# returning a new list containing the elements common to two lists.
def unique (list1, list2):
    li = set(list1) & set(list2)
    return li
list1 = [1,2,3,9,10]
list2 = [1,3,10,12,15]
u = unique(list1,list2)
print(u)

# finding all strings with a length > 4
def length_sup_four(list):
    li = []
    for i in list:
        if len(i) > 4:
            li.append(i)
    return li
fruits = ["apple", "banana", "fig"]
fruits_list = length_sup_four(fruits)
print(fruits_list)

# finding the integers > 10 
def sup_ten(list):
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
sup = sup_ten(list)
print(sup)

# Converting strings to uppercase
def string_upper_case(list):
    li = []
    for i in list:
        li.append(i.upper())
    return li
list = ["hello","world"]
li_upper = string_upper_case(list)
print(li_upper)

# sum of elements in a list
def somme(list):
    s = 0
    for i in list:
        s += i
    return s
list = [1,2,3,4]
print("The sum of all the elements in the given list is ", somme(list))

# returning a list of the square of integers.
def square_list(list):
    racine_liste = []
    for i in list:
        racine_liste.append(math.sqrt(i))
    return racine_liste
list = [1,2,4]
li_square = square_list(list)
print(li_square)

# returning a list of the powers of integers.

def pow_list(list):
    carres_liste = []
    for i in list:
        carres_liste.append(i ** i)
    return carres_liste
list = [1,2]
li_pow = pow_list(list)
print(li_pow)
