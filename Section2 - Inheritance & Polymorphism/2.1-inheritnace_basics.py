class Foo(object):
    foo = 1


class Bar(Foo):  # Foo is added to attribute lookup path!
    bar = 1

b = Bar()
print(b.foo)
print(b.bar)

print(dir(object))   # base atributes list
print(dir(Foo))      # base atributes list + a few more(?) + foo
print(dir(Bar))      # base atributes list + a few more(?) + foo + bar

# TODO - find out why object class attrs are not the same as its subclasses

var = 'hello'
var2 = 'HI'
var3 = 'Hola'

for x in var, var2, var3:
    print(x.swapcase())