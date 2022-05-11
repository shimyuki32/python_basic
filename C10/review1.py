
class Element:
    def __init__(self, name, symbol, number):
            self.__name = name
            self.__symbol = symbol
            self.__number = number
    @property
    def name(self):
        return self.__name
    
hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name)
hydrogen.__name = 'Argon'
print(hydrogen.name)