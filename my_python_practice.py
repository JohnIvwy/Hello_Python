'''This file is to practice my knowledge by Python'''

# To create a Set
my_st = set()
st = {}

# Exercises from GitHub
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Prosol', 'Unitec', 'Aoc'])
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)

# Level 3
new_st = set(age)
print(len(age))
print(len(new_st))