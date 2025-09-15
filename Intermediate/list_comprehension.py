'''This file is to practice my knowledge by Python'''

### List comprehension ###

# Meaning: is a compact way of creating a list from a sequence.

# syntax
# [i for i in iterable if expression]



# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_nums_cero = [i for i in numbers if i < 0 or i == 0]
print(neg_nums_cero)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [i for lt_out in list_of_lists for lt in lt_out for i in lt]
print(flatten_list)