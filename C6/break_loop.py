while True:
    if (stuff := input("String to capitalize [type q to quit]: ")) == "q":
        break
    print(stuff.capitalize())