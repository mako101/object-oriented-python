#  Common Python operators actually map to 'magic' attributes - "syntactic sugar", e.g:
# 'abc' in x    x.__contains__('abc')
# x == 'abc'    x.__eq__(abc)
# x[1]          x.__getitme__(1)
# x[1:3]        x.__getslice__(1,3)
# len(x)
# print(var)    x.__repr__()

# The magic attributes can be redefined, just like anything else :)


class ListSummary(object):

    def __init__(self, list_object):
        self.my_list = list_object

    # customise '+' operator :)
    def __add__(self, other):
        new_list = [x + y for x, y in zip(
            self.my_list, other.my_list
        )]
        return ListSummary(new_list)

    # customise print operation
    def __repr__(self):
        return 'My cool list: {}'.format(str(self.my_list))


a = ListSummary([1, 2, 3, 4, 5])  # the element without pair is ignored by zip
b = ListSummary([10, 20, 30, 40])
c = a + b
print(c)  # My cool list: [11, 22, 33, 44]


