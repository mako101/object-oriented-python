class Foo(object):

    def __init__(self, x=10):
        print('Initialising Foo object')
        self.__x = x

    def display(self):
        print(self.__x)


foo = Foo(5)


foo.display()
# print(foo.__x)


class Classy():
    classvar = 10

    def set_val(self):
        self.instvar = 'x'

cl = Classy()
cl.set_val()
print(cl.classvar)
cl.classvar = 20
print(cl.classvar)
del cl.classvar
print(cl.classvar)

print(cl.instvar)
cl.instvar = 'y'
print(cl.instvar)
del cl.instvar
print(cl.instvar)