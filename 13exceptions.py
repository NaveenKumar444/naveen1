# how to handle errors in python program
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('age cannot be zero')
except ValueError:
    print('invalid value')