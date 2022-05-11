class Person:
    def __init__(self, name):
        self.name = name
        
class EmailPerson(Person):
        def __init__(self, name, email):
            super().__init__(name)
            self.email = email

bob = EmailPerson('Bob Frappples', 'bob@frapples.com')
print(bob.name)


print(bob.email)

class Dog:
    def __init__(self, name):
       self.name = name

class UltraDog(Dog):
    def __init__(self, name, type_):
        super().__init__(name)
        self.type = type_

ud1 = UltraDog("taro", "akita")
print(ud1.name)
