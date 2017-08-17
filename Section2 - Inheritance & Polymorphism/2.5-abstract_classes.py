import abc


class AbstractSample(object):

    # the magic attribute that sets this calss to be an abstract class
    __metaclass__ = abc.ABCMeta

    # this means the child classes
    # have to implement this method
    # or an error will be thrown
    @abc.abstractmethod
    def get(self):
        print('Yayya')

    # the actual functionality of abstract methods is ignored by Python
    # i.e. the abstract methods don't do anything
    # they just need to implemented somehow in child classes
    @abc.abstractmethod
    def set(self, bar):
        return bar + 1

    # this method is not required
    def foo(self):
        return


# Abstract class cannot be instantiated, it only serves as a parent class
# z = AbstractSample()
# TypeError: Can't instantiate abstract class AbstractSample with abstract methods get, set


class MyBrokenClass(AbstractSample):
    def set(self):
        return

# TypeError: Can't instantiate abstract class MyBrokenClass with abstract methods get
# x = MyBrokenClass()


class MyClass(AbstractSample):
    def get(self):
        pass

    def set(self):
        return

y = MyClass()
y.get()