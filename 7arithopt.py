print(10 + 3)
print(10 - 3)
print(10 / 3)
print(10 // 3)
print(10 * 3)
print(10 ** 3)
print(10 % 3)
x = 10
# augumented operators
x = x + 3
x += 3
print (x)
x = 10
x -= 3
print(x)
# operator precedence
#parenthesis,exp,mul,div,add,sub
x = (10 + 3) * 2 ** 2
print(x)
#math functions
x = 2.9
print(round(x))
print(abs(-2.9))  # abs returns the positive value
import math
print(math.ceil(2.9))
print(math.floor(2.9))
# if statements

is_hot = True
if is_hot:
    print("it's a hot day")
print("enjoy your day")
is_hot = False
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
else:
    print("it's a cold day")
    print("wear warm clothes")
print("enjoy your day")
is_cold = False
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")
print("enjoy your day")
# exercise
house_price = 1000000
good_credit = True
if good_credit:
    down_payment = (10 / 100) * house_price
else:
    down_payment = (20 / 100) * house_price
print(f"down payment: {down_payment}")
# logical operators
## if applicant has high income and good credit, then he is elisible for loan
has_good_income = False
has_good_credit = True
if has_good_income and has_good_credit:
    print("eligible for loan")
else:
    print("not eligible for loan")
## if applicant has high income or good credit, then he is elisible for loan
has_good_income = False
has_good_credit = True
if has_good_income or has_good_credit:
    print("eligible for loan")
# not operator
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("eligible for loan")
# comparison operators
temperature = 35

if temperature > 30:
    print("it's a hot day")
else:
    print("it's not a hot day")
 #exercise

name = input('enter the name ')
if len(name) < 3:
    print("name mmust be atleast 3 characters")
elif len(name) > 50:
    print("name can be maximum of 50 characters")
else:
    print("name loos good")










