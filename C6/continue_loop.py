while True:
    if (value := input("Integer, please [q to quit]:")) == 'q':
        break
    if (number := int(value)) % 2 == 0:
        continue
    print(number, "squared is", number * number)