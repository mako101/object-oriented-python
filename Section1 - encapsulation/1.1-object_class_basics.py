import re


class MyClass(object):
    foo = 1

this = MyClass()

print(this)

setattr(this, 'foo', 10)

# list all attributes and their values
for x in (dir(this)):
    print('Name: {}'.format(x))
    print('Value: {}'.format(getattr(this, x)))


# get class_name
class_name = re.findall('__main__.(\w+)', str(MyClass))[0]
print class_name
