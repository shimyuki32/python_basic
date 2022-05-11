class Car:
    def exclaim(self):
        print("I'm a car!")
    pass
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo")
    pass

print(issubclass(Yugo, Car))
print(issubclass(Car, Yugo))

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()