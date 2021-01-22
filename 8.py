# while loops
i = 1
while  i <= 5:
    print("*" * i)
    i = i + 1
print("Done")

# guessing game

i = 1
while i <= 3:
    nav = int(input("guess: "))
    if nav == 9:
        print("your won!")
        break
    i = i + 1
else:
    print("sorry, you failed... ")



