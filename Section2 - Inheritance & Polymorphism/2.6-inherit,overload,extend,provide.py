import abc


class GetSetParent(object):

    __metaclass__ = abc.ABCMeta

    def __int__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return