
# -------------- RANGE --------------
# The range() function is used list of numbers. The range(start, end, step)
# takes three parameters: starting, ending and increment.
# By default it starts from 0 and the increment is 1.
# The range sequence needs at least 1 argument (end).
rg = list(range(0,20,3))
print(rg)

# -------------- PASS --------------
# In python when statement is required (after semicolon), but we don't like 
# to execute any code there, we can write the word pass to avoid errors. 
# Also we can use it as a placeholder, for future statements.
# Example:
for number in range(6):
    pass