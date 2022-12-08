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
furniture = ['table', 'chair', 'rack', 'shelf']  # zero-based string

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
numbers = [2, 5, 3.14, 1, -7]
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
my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud',
}
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

