"""
    Adi Mendel homework 23/6/22
    Sela Automation Bootcamp
    for katya :)
"""


"""Exercise 1:"""


str_ = "dabaxyddab"
dict = {}
# section 1:
for char in str_:
    dict[char] = dict.get(char, 0) + 1
for k, v in sorted(dict.items()):
    print(k, v)
# section 2:
reversedDict = {}
for key, value in dict.items():
    if reversedDict.get(value) is None:
        reversedDict[value] = list(key)
    else:
        reversedDict[value].append(key)
print(reversedDict)


"""Exercise 2:"""


lst1 = [11,  7, 5,  8, 5,  37,  11, 5]
lst2 = [22, 8, 10, 1,1, 11]
lsr3 = [ 71, 3, 22, 8,2, 2, 14, 1]
cummun_values = []
# section 1:
given_lists = [lsr3, lst2, lst1]
for list_ in given_lists:
    if not len(set(list_)) == len(list_):
        print(f"list {list_} has common values")
    else:
        cummun_values.append(list_)

# section 2:

if len(cummun_values) == 2:
    list_to_set = set(cummun_values[0])
    common_values = list(list_to_set.intersection(cummun_values[1]))
    print(f"common values of two lists are {common_values}")
elif len(given_lists) == 1:
    print(f"common values of one list is {cummun_values[0]}")

else:
    print("These no lists to check..empty")


"""Exercise 3:"""


lst = [31, 99, 3, 1943]
sort_order = "asc"
s = set(tuple([digit for digit in str(lst) if digit.isdigit()]))  # get each digit from lst
"""Now checking the sort_order var and print each digit"""
if sort_order == "asc":
    for digit in sorted(s):
        print(digit, end=", ")
elif sort_order == "desc":
    for digit in sorted(s, reverse=True):
        print(digit, end=", ")
