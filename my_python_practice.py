'''This file is to practice my knowledge by Python'''

company = 'Coding For All'
print(company)
print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company.strip('Coding '))
print(company.index('Coding'))
print(company.replace('All', 'Everyone'))
print(company.split())

companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))

print(company[0])
print(company.rindex('l'))

script = 'You cannot end a sentence with because because because is a conjunction'
print(script.strip('because '))