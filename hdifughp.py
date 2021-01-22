def hj(nav):
    nav = nav.split(" ")
    emoji = {
        ":)": "haha",
        ":(": "uff"
    }
    output = ""
    for i in nav:
        output += emoji.get(i, i) + " "
    return output


nav = input("> ")
print(hj(nav))
