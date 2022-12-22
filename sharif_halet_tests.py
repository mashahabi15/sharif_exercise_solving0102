# print("Hello World\nHow are you?\nHow do you do?")
# comment1
"""
comment2
"""
# first_name = input("Enter your name:\t")
# last_name = input("Enter your family:\t")
#
# # 1
# print("Your name is " + first_name + " " + last_name)  # concatenation
#
# # 2
# print("Your name is {} {}".format(first_name, last_name))  # format
#
# # 3
# print("Your name is {1} {0}".format(last_name, first_name))  # format with index
#
# # 4
# print(f"Your name is {first_name} {last_name}")  # f string


# num = int(input("Please enter a number:\t")) # type casting
# print(num % 3)


# > = < <= >= == != + - * / // % :=
# print(f"{4 // 2} is not {4 / 2}")
#

my_uni = "SharifUniversity"  # ششمین خانه = ایندکس پنج

# print(f"Last char: {my_uni[15]} *** {my_uni[-1]}")  # reverse indexing
#
# print(my_uni[0:6])  # slicing
# print(my_uni[0:11:2])  # slicing with step [start:end:step] default: (start=0, end=last index, step=1)
# print(my_uni[:])  # equal: print(my_uni)
# print(my_uni[::-1])  # reverse a string
# print("Iran" + " " + "Country")  # concatenation
# print("Iran " * 10)  # repetition

# if expr1:
#     # statement 1
# elif expr2:
#     # statement 2
# elif expr3:
#     # statement 3
# .
# .
# .
# else:
# last statement

# = -> assignment تخصیص
# == -> comparision مقایسه

# num = int(input("Enter a number:\t"))
# if num % 2 == 0:
#     print("Even number!")
# else:
#     print("Odd number!")

# salary = int(input("Enter your salary:\t"))
# working_experience_years = int(input("Enter your working experience years:\t"))
#
# if working_experience_years > 5:
#     final_salary = salary + 0.1 * salary
#
# else:
#     final_salary = salary
#
# print(int(final_salary))


# A = int(input("Enter your score"))
# if A < 25:
#     print('F')
# elif 25 <= A and A <= 45: # or
#     print("E")
# ....

# Exception Handling
# try:
#     print("Sharif"[2])
# except IndexError:
#     # do something...
#     print("No such index!")


# 2022.11.24
# if expression
# if False:
#     print("I'm here")
# if True:
#     print("I'm here")
#
# if 1 == 1:
#     print("I'm here")
#
#

# if True and False:
#     print("I'm here")
# if (True and False) or True:
#     print("I'm here")
#
# if not True:
#     print("I'm here")
# if not False: # !false=true
#     print("I'm here")
#
# num = 4
#
# if num in [5, 6, 7]:
#     print("0")
#
# if num == 5 or num == 6 or num == 7:
#     print("1")
#
# if num == 5 or 6:
#     print("2")
# object -> int -> bool
# 0, 0.0, empty list, empty dictionary, empty string => False
# if 0:
#     print("1")
#
# if -1:
#     print("2")
#
# if 100:
#     print("3")
#
# if "":
#     print("4")
#
# if []:
#     print("5")
#
# if {}:
#     print("6")
#
# if 0.0:
#     print("7")
#
# if ():
#     print("8")
# if 0:  # 0.0, '', [], {}, ... (any empty container)
#     print("I'm here")
#
# string, tuple, numbers => immutable

### lists

# furniture = ['table', 'chair', 'rack', 'shelf']  # zero-based string
# a = furniture[0]
# b = furniture[1]
# c = furniture[2]
# d = furniture[3]
# print(furniture[0])  # getting values with indexes
# print(furniture[-3])  # negative indexes -3 = len(furniture) - 3 => 1
# print(furniture[1:3])  # slicing
# print(len(furniture))  # length of a list
# furniture[0] = 'desk'  # changing values with indexes
# print([1, 2, 3] + ['A', 'B', 'C'])  # concatenation
# print(['X', 'Y', 'Z'] * 3)  # repetition
#
# for index, item in enumerate(furniture):  # enumerate todo
#     print(f'index: {index} - item: {item}')
#
# furniture = ['table', 'chair', 'rack', 'shelf']
# price = [100, 50, 80, 40]
# for item, amount in zip(furniture, price):  # Iterate over several iterables in parallel.
#     print(f'The {item} costs ${amount}')
#
# if 'bed' not in ['table', 'chair', 'rack', 'shelf']:  # in and not in
#     print("bed not in furniture!")

# if  "b" in "Sharif":
#     print("Yes!")
# furniture = ['table', 'chair', 'rack', 'shelf']  # zero-based string

#
# table, chair, rack, shelf = furniture  # multiple assignment
# print(furniture.index('chair'))  # index method
# # furniture.append('bed')
# furniture.insert(1, 'bed')
# # del furniture[2]  # removes an item using the index:
# print(furniture)
# furniture.remove('bed')  # removes an item with using actual value of it:
# print(furniture)
# furniture.pop()  # will remove and return the last item of the list. You can also pass the index of the element as an optional parameter
# print(furniture)
# numbers = [2, 5, 3.14, 1, -7]
# numbers.sort()  # sort -> ascending صعودی, descending نزولی
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# print(sorted(numbers, reverse=True))  # built-in sorted
# print(max([1, 2, 3]))
# print(math.sqrt(4))


#
# ### Tuple
# furniture = ('table', 'chair', 'rack', 'shelf')
# print(furniture[0])
# print(furniture[1:3])
# print(len(furniture))
#
# ### Dictionary
# my_cat = {
#     'size': 'fat',
#     'color': 'gray',
#     'disposition': 'loud',
# }
# print(my_cat.get('height'))
# print(my_cat['height'])
# car_info_list = ["red", 2020, "Benz"]
# car_info_dict = {
#     "color": "red",
#     "production_year": 2020,
#     "manufacturer": "Benz",
# }
# car_info_dict = dict(color="red", production_year=2020, manufacturer="Benz")
# car_info_dict["has_roof"] = False
# first_name = "ali"
# print(my_cat.keys())
# print(my_cat.values())
# print(f"My cat is {my_cat.get('color')} color!")
#
# if 'height' not in my_cat:  # in and not in. also check with values and keys
#     my_cat['height'] = 40
# print(my_cat)
# my_cat.pop('height')  # removes and return an item based on a given key
# print(my_cat)
# del my_cat['height']  # removes an item based on a given key.
# print(my_cat)
# my_cat.clear()  # removes all the items in a dictionary.
# print(my_cat)
# dict_a = {'a': 1, 'b': 2}
# dict_b = {'b': 3, 'c': 4}

# dict_c = {**dict_a, **dict_b}  # Python 3.5+
# print(dict_c)

### Set -> A set is an unordered collection with no duplicate elements
# s = {1, 2, 3}
# s = set([1, 2, 3])
# s = {}  # this will create a dictionary instead of a set
# type(s)
# s = {1, 2, 3, 2, 3, 4}  # remove all the duplicate values.
# print(s[0]) # as an unordered data type, they can’t be indexed.
# s.update([2, 3, 4, 5, 6])


### for loop
# print [1,...,10]
# range() function


# for => start, stop, step

# for i in range(200):
#     if i % 2 == 0:
#         print(i)
#
# sum = 0
# for number in range(2001):
#     sum = sum + number # sum = 0 + 1 + 2 + 3 + ...
# print(sum)

# my_dict = {
#     "name": "ali",
#     "family": "mohammadi"
# }
# print(list(my_dict.keys()))

# 1.
# students = ['maryam', 'gholi', 'fateme', 'ali']
#
# # for student_name in students:
# #     print(student_name)
#
# for index in range(len(students)):
#     print(students[index])

# 2.
# list_len = int(input("Enter list length:\t"))
# my_list = []
# # my_list = list()
#
# for i in range(list_len):
#     item = input()
#     my_list.append(item)
#
# for item in my_list:
#     print(item)

# 3.
# list_len = int(input("Enter list length:\t"))
# my_list = input().split(' ')
# print(my_list)

# print('Hi. I am going to Tehran tomorrow, I will call you.'.split(','))

# .3'
# my_list = input().split(' ')
# my_list2 = list()
# for item in my_list:
#     my_list2.append(int(item))
#
# print(my_list2)

# a = input().split(' ')
# print(a)
# print(list(map(int, a)))

# print(list(map(int, input().split(' '))))

# l1 = ['2', '5', '17']
# l2 = []
# for i in l1:
#     l2.append(int(i))
#
# print(l2)

# print(list(map(int, ['2', '5', '17'])))

# my_input = input()  # 5 7 10 4 19 25 46
#
# number_list = list(map(int, my_input.split(' ')))
#
# for item in number_list:
#     if item % 5 == 0:
#         print(item)

# my_input = input()  # 5 7 10 4 19 25 46
#
# number_list = list(map(int, my_input.split(' ')))
#
# even_count = 0
#
# for item in number_list:
#     if item % 2 == 0:
#         even_count = even_count + 1  # event_count += 1
#
# print(even_count)

# x = input() # 5 7 10 4 19 25 46 => [5,7,10,4,19,25,46]
# # print(x.split(' '))
# my_list = [] # list()
#
# for item in x.split(' '):
#     my_list.append(int(item))
#
# print(my_list)


# my_list = []
# for i in range(5):
#     number = int(input())
#     my_list.append(number)

# print('I am Maedeh. I am graduated.'.split(','))

# list, tuple, set, dict, string, ...
#
# a = [8, 7]
# b = [8, 7]
# print(a == b)
# a[0]
# a = {
#     1: 2,
#     3: 4,
# }
# b = {
#     3: 4,
#     1: 2,
# }
# print(a == b)

# mutable / immutable
# 1. int, string, tuple, ...
# my_str1 = "Sharif1"
# my_str2 = my_str1
# my_str2 = "Sharif2"
# print(my_str1)


# 2. list, dict, set,...
# a = [2, 5]
# b = a.copy()  # call by reference
# b[0] = 4  # b= [4, 5]
# print(a)

# 3.
# a = [2, 5]
# b = a.copy()
# b[0] = 4  # b= [4, 5]
# print(a)

# x = input() # 5 7 10 4 19 25 46 => [5,7,10,4,19,25,46]
# my_list = list(map(int, x.split(' ')))
# list_sum = 0
#
# for item in my_list:
#     list_sum = list_sum + item # list_sum += item
#
# print(list_sum)


# my_set = set()
# my_set.add(5)
# my_set.add(10) # my_set = {5, 10}
# my_set.add(10)
# my_list = [5, 10, 10]
# # print(f"set: {my_set}, list: {my_list}")
# print(sorted(my_set))

# list1 = [10, 10, 10, 4, 4, 7, 8]
# list2 = [] # [10,4,7,8]
#
# for item in list1:
#     if item not in list2:
#         list2.append(item)
# print(list2)
#
# print(list(set(list1)))


# n=10 -> 1+2+3+...+10

# n = int(input("Enter a number:\t"))
# numbers_sum = 0
#
# for i in range(1, n+1):
#     numbers_sum = numbers_sum+ i
#
# print(numbers_sum)

# Trace, Debug

# n! = 1 * 2 * 3 * ... * n
# n = int(input())  # 5! = 1 * 2 * 3 * 4 * 5
# factoriel = 1
#
# for i in range(1, n + 1):
#     factoriel = factoriel * i  # factorial *= i
#
# print(factoriel)

# n = int(input()) # 15 => 1,3,5,15 => 4
# # n => 1 <= i <= n and n % i == 0
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

# for i in range(1, 101):
#     # if i == 43 or i == 87 or i == 94:
#     #     continue
#
#     # if i in [43, 87, 94]:
#     #     continue
#
#     if i not in [43, 87, 94]:
#         print(i)

# for i in range(1, 101):
#     print(i)

# while condition:
#     statement ...

# i = 1
#
# while i <= 100:
#     print(i)
#     i = i + 1
#
# num = int(input())
#
# while num != -1:
#     print(num)
#     num = int(input())


# function => input? operation? output?(return value)
# def add_1_to_num(number):  # argument in signature
#     # scope حوزه
#     added_number = number + 1
#     return added_number
#
#
# for i in range(3):
#     num = int(input())
#     # num = num + 1
#     num = add_1_to_num(num)
#     print(num)
#
# age = int(input("Enter your age"))
# # next_year_age = age + 1
# next_year_age = add_1_to_num(age)
# print(f"You'll be {next_year_age} years old by the next year!")


# def print_info(friend_name, friend_age):
#     print(f"Your friend is {friend_name} and he/she is {friend_age} years old.")
#
#
# for i in range(2):
#     name = input("Enter your name:\t")
#     age = int(input("Enter your age:\t"))
#     print_info(name, age)  # positional argument
#     print_info(friend_name=name, friend_age=age)  # keyword argument
#     # print_info(friend_age=age, friend_name=name) # keyword argument

# def print_info():
#     for i in range(2):
#         name = input("Enter your name:\t")
#         age = int(input("Enter your age:\t"))
#         print(f"Your friend is {name} and he/she is {age} years old.")
#
#
# print_info()

# todo default value, mutable/immutable in function

# def summation(num1, num2=5):  # default value مقدار پیشفرض -> immutable
#     sum_value = num1 + num2
#     return sum_value
#
#
# print(summation(num1=10))  # keyword argument

# تابعی بنویسید که اسم یک شخص را دریافت میکند و به او سلام می‌کند. اگر اسمی به آن
# پاس ندادیم hello world را چاپ کند
# Hello Sara!

# for i in [1,2,3,4,5]:
#     print(i)


# x, y = 1, 2  # unpacking
#
# my_dict = {
#     0: "v0",
#     1: "v1",
#     2: "v2",
# }
# print(my_dict.items())


# for k, v in my_dict.items():
#     print(f'key={k} - value={v}')

# for k in my_dict.keys():
#     print(k)

# for v in my_dict.values():
#     print(v)

# my_list = [(0, '0'), (1, '1'), (2, '2')]
# a, b = (1, '1')

# for i in my_list:
#     indx0 = i[0]
#     indx1 = i[1]
#     print(f'{indx0} , {indx1}')

# for indx0, indx1 in my_list:  # unpacking
#     print(f'{indx0} , {indx1}')

# 1
# def add(x):
#     x = x + 1
#
#
# a = 2  # immutable
# add(a)
# print(a)


# 2
# def my_sort(x):
#     x = x.sort()
#
#
# a = [2, 1, 7, 3]  # mutable
# my_sort(a)
# print(a)

# a = [7, 8, 4]
# b = a
# b = [1, 3, 2]
# b = b.sort()
# print(a)  # mutable


# x = 20  # breakpoint
# for i in range(100):
#     x = x + 3
#     print(x)
# a = 5
# print(x)

# friends_file = open('friends.txt', 'w') # r/w/a/w+
# friends_list = list()
#
# for i in range(2):
#     friend_input = input("Please enter your friend name and age:\t") # Sara 24
#     # friends_file.write(f'{friend_input}\n') # a string
#     friends_list.append(f'{friend_input}\n')
#
# friends_file.writelines(friends_list) # a list of string
# friends_file.close()
#
# read_friends_file = open('friends.txt', 'r')
#
# print(read_friends_file.read())
#
# read_friends_file.close()


# todo check
# friends_file = open('friends.txt', 'w+') # r/w/a/w+
# friends_list = list()
#
# for i in range(2):
#     friend_input = input("Please enter your friend name and age:\t") # Sara 24
#     # friends_file.write(f'{friend_input}\n') # a string
#     friends_list.append(f'{friend_input}\n')
#
# friends_file.writelines(friends_list) # a list of string
#
# print(friends_file.read())
#
# friends_file.close()


# 1. scopes حوزه


b = 1


# def f1():
#     a = 1
#     print(b)
#
# f1()

# nested function

# def f1():  # enclosing function
#     x = 1  # local variable
#     print(z)
#
#     def f2():  # nested function
#         y = 2  # local variable
#         print(x)  # non-local variable
#         print(z)
#
#     f2()
#
#
# z = 3  # global variable
# f1()

# z = 3
#
#
# def a():
#     x = 1
#
#     def b():
#         y = 2
#         print(x, y, z)
#
#     b()
#     print(x, z)  # print(x, y, z)
#
#
# a()

# 2. recursion(recursive function) تابع بازگشتی

# def summation(n): # normal
#     s = 0
#     for i in range(1, n+1):
#         s += i
#
#     return s
#
# print(summation(4))

# def rec_summation(n):
#     if n > 1:
#         return n + rec_summation(n-1)
#
#     elif n == 1:
#         return 1
#
# print(rec_summation(4))
# sum(4) => 4 + sum(3) = 10
# sum(3) => 3 + sum(2) = 6
# sum(2) => 2 + sum(1) = 3
# sum(1) = 1
# heap, stack

# def fact(n): # normal
#     p = 1
#     for i in range(1, n+1):
#         p *= i
#
#     return p
#
# print(fact(5))

# recursive

# def fact(n):
#     if n == 1:
#         return 1
#
#     return n * fact(n-1)
# print(fact(5))
# fact(5) = 5 * fact(4) => 4 * fact(3) => 3 * fact(2) => 2 * fact(1) => 2 * 1


s = 0
for i in range(3):
    s += i # s = s + i

print(s)










# 3. lambda
# a = lambda x: x * 2
# print(a(5))

# 4. map map(function, iterable) ->  returns a map object(which is an iterator)

# 5. filter filter(function, iterable) -> iterator
# ages = [5, 12, 17, 18, 24, 32]
#
# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True
#
# adults = filter(myFunc, ages)

# print(list(filter(lambda x: x < 0, range(-5, 5))))
