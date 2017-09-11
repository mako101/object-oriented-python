# Inheritance can be brittle:
# A change somewhere in the chain of inheritance can break code elsewhere
# Decoupled classes are independent of each other
# But they can work with each other  as long as interface is maintained
# Its pythonic not to check that the interface is actually available -_-

import StringIO


class WriteWrapper(object):

    def __init__(self, writer):
        self.__writer = writer

    def write(self):
        message = "Foobarrr!!!!"
        # we just call write method, assuming it is available
        self.__writer.write(message)

# this has write() method
file_handler = open('test.txt', 'w')

# so does this!
string_io = StringIO.StringIO()

writer1 = WriteWrapper(file_handler)
writer1.write()
file_handler.close()

writer2 = WriteWrapper(string_io)
writer2.write()

print('File object: {}'.format(open('test.txt', 'r').read()))
print('String_IO object: {}'.format(string_io.getvalue()))
