
class Animal(object):

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super(Dog, self).__init__(name)
        self.breed = breed


d = Dog('Sparky', 'Alsatian')
print(d.name)
print(d.breed)