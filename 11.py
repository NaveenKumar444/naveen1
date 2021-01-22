# tuples are immutale
num = (1, 2, 3, 4, 5, 6)
print(num[0])
#unpacking
on = (1, 2, 3)
x, y, z = on
print(y)
jk = [2, 3, 4]
u, v, w = jk
print(v)

# dictionaries are mutable
customer = {
    "name": "naveen",
    "age": 22,
    "is_verified": True
}
customer["name"] = "nithish"
customer["birthday"] = "jan 13 1999"
print(customer)

#exercise
go = (input("phone: "))
po = {"1": "one",
      "2": "two",
      "3": "three",
      "4": "four"
 }
k = ""
for i in go:
    k += po.get(i, "!") + " "
print(k)

