import random

class House(object):
    new_houses = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        House.new_houses += 1

    # standard (bound) instance method
    def upgrade(self):
        print('Increasing the value of {}'.format(self.name))
        self.price += self.price * 0.2

    # class method referring to the attribute of the class, not instance
    @classmethod
    def show_new_houses(cls):
        print('Showing {} new houses'.format(House.new_houses))

    # a utility method that can be used indepedently of class ot its instances
    @staticmethod
    def evaluate_property(property_name):
        value = random.choice(['high', 'moderate', 'low'])
        print('The value of {} is {}'.format(property_name, value))


condo = House('condo', 100000)
condo.upgrade()
condo.upgrade()
print(condo.price)


maisonette = House('maisontette', 75000)
House.evaluate_property(maisonette.name)
House.evaluate_property('Town house')

House.show_new_houses()

print(condo.upgrade)  # <bound method House.upgrade of <__main__.House object at 0x02198DF0>>
print(House.upgrade)  # <unbound method House.upgrade>
print(House.evaluate_property)  # <function evaluate_property at 0x021C0930>
print(House.show_new_houses)  # <bound method type.show_new_houses of <class '__main__.House'>>



