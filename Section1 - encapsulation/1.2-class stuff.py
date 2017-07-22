
class Object(object):

   def callme(self):
       print('I\'m an instance of Object class')
       print self


foo = Object()
bar = Object()

for x in [foo, bar]:

    x.callme()
    print(x)


# self can be renamed but it shouldn't be!
class Foo(object):
    def callme(bob):
        print('I\'m an instance of Object class')
        print bob

git = Foo()
bot = Foo()

for x in [git, bot]:

    x.callme()
    print(x)


# Adding instance-only attributes - bad practice??

class Morph(object):

    def change(self):
        self.new = 5


bob = Morph()
print(bob)
print(bob.new)  # <= AttributeError exception
bob.change()
print(bob.new)
print(bob)

