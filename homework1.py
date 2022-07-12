"""
    16/06/2022
    Adi Mendel homework.
    sela automation
    for katya :)
"""

# exercise 1:

lst = [3, 7, 2]
histo = [item * '*' for item in lst]
print(histo)

# exercise 2:

lst1 = ["a", "b", "c"]
lst2 = ["x", "y", "z"]
lst_res = []
"""The program assumes that the two lists are the same length"""
for i in range(len(lst1)):
    lst_res.append(lst1[i] + lst2[(len(lst1) - 1) - i])
print(lst_res)
