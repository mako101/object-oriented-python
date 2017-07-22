"""
Any class can inherit from multiple classes
Normally MRO (method resolution order is depth based)
Example:
B inherits from A
    class D(B,C)
    MRO: D, B, A, C

But if multiple parent classes import forom the same 'grandarent class'
ie 'diamond inhertinace', the granparent class will be the last in the MRO
Example:
B inherits from A, C inherits from A
    class D(B,C)
    MRO: D, B, C, A
"""

"""
    Standard MRO
"""


class A(object):
     def do_this(self):
         print('Doing this in A')


class B(A):
    pass


class C(object):
    def do_this(self):
        print('Doing this in C')


class D(B, C):
    pass

d = D()
d.do_this()  # 'Doing this in A'

# mro is is type class method/attribute
print(type(d).mro())
print(type(d).__mro__)
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <type 'object'>]

"""
    Diamond inheritance pattern <>
"""


class A(object):
    def do_this(self):
        print('Doing this in A')


class B(A):
    pass


class C(A):
    def do_this(self):
        print('Doing this in C')


class D(B, C):
    pass


d = D()
d.do_this()  # 'Doing this in C'

# mro is is type class method/attribute
print(type(d).mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>]
