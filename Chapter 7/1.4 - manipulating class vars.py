class InstanceCounter(object):
    __count = 0
    __foo = 0

    def __init__(self, val):
        self.val = val
        # this changes the value of the parent class attribute
        InstanceCounter.__count += 1
        # this changes the value of instance attribute only
        self.__foo += 1

    def display(self):
        print('Value is {}'.format(self.val))
        print('Count is {}'.format(self.__count))
        print('Foo is {}'.format(self.__foo))
        print('\n')

i1 = InstanceCounter('a')
i1.display()
i2 = InstanceCounter('b')
i2.display()
