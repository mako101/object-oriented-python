import abc


class AbstractSample(object):

    # the magic attribute that sets this calss to be an abstract class
    __metaclass__ = abc.ABCMeta

    # this means the child classes
    # have to implement this method
    # or an error will be thrown
    @abc.abstractmethod
    def get(self):
        return

    @abc.abstractmethod
    def set(self):
        return

    # this method is not required
    def foo(self):
        return


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