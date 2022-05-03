import random
secret = random.randrange(1, 10)
print(secret)

while True:
    guess = int(input("type a number:"))
    if secret < guess:
        print("too high")
    elif secret > guess:
        print("too low")
    else:
        print("just right")
        break
        