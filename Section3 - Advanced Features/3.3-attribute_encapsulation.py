class MyClass(object):

    def __init__(self, value):
        self.__attribute = value

    # this sets method to be used as a property
    # a "var" property in this case
    # also allows to have some control over hidden property
    # by exposing "public" ways of manipulating it
    # this MUST be set in order for the methods below to work!
    # Without methods below var can be READ, but not MODIFIED!!
    @property
    def var(self):
        print('Getting the "var" attribute')
        return self.__attribute

    # Without setter we cant SET var
    @var.setter
    def var(self, value):
        print('Setting the "var" attribute')
        self.__attribute = value * 2
        print("var is now {}".format(self.__attribute))

    # Without deleter we cant DELETE var
    @var.deleter
    def var(self):
        print('Deleting the "var" attribute')
        self.__attribute = 0
        print("var is now {}".format(self.__attribute))


foo = MyClass(1)

print(foo.var)  # print var "property"

foo.var = 5  # calls var.setter! We can manipulate the var as well ;)

print(foo.var)

del foo.var  # calls var.deleter

print(foo.var)

