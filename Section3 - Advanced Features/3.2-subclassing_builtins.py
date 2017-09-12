# We modify the builtin getitem/setitem
# To use index starting with 1, not zero :)


class MyList(list):

    @staticmethod
    def __correct_index(index):
        if index == 0:
            raise IndexError('Using index 0 is forbidden!')
        else:
            index -= 1
        return index

    def __getitem__(self, index):
        index = MyList.__correct_index(index)
        return super(MyList, self).__getitem__(index)

    def __setitem__(self, index, value):
        index = MyList.__correct_index(index)
        return super(MyList, self).__setitem__(index, value)


my_list = MyList(['a', 'b', 'c', 'd'])

my_list[1] = 'o'
print(my_list)  # ['o', 'b', 'c']

my_list[3] = 'u'
print(my_list)

# my_list[0] = 'foo'  # IndexError: Using index 0 is forbidden!

