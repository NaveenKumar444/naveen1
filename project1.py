## weight converter

weight = int(input('weight: '))
tpw = input('(L)bs or (K)g: ')
if tpw.upper() == "L":
    print(f"you are { weight * 0.45 } kilos")
elif tpw.upper() =="K":
    print(f"you are {weight / 0.45} pounds")
else :
    print("please enter the correct value")
