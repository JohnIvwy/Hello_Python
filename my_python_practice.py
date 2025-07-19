'''This file is to practice my knowledge by Python'''

# To create a list
my_lst = []
lst = list()

#lst = ['John', 'Andrea', 'Carlos', 'Sasy', 'Ana', 'Aleja', 'Martha', 'Thony', 'Jotis']
#some_names = lst[::2] # Toma cada dos items es incluyendo el primero = John, Carlos, Ana...
#print(some_names)

# Exercises from GitHub

lst = list()
lst = [1,2,3,4,5,6,7]
print(len(lst))
print(lst[::3])

mixed_data_types = ['John', 21, 1,70,'Soltero','La Calera']
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[::3])

# Modify
it_companies[0] = 'Notion'
print(it_companies)

# Adding
it_companies.append('SAP')
print(it_companies)
it_companies.insert(3,'WhatsApp')
print(it_companies)

# Mayus
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Joining element
it_companies += ['#;']
print(it_companies)

# Checking exist
print('SAP' in it_companies)

# Sort
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

# Droping
del it_companies[0:3]
print(it_companies)
del it_companies[-3:]
print(it_companies)
it_companies.pop(int(len(it_companies)/2))
print(it_companies)
it_companies.remove('Notion')
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

# Joining
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python')
print(full_stack)


# 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.append(ages[-1])
ages.insert(0, ages[0])
print(ages)

median_age = ages[int(len(ages)/2)]