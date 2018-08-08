# custom exception for YaDisk


class YaDiskException(Exception):
    code = None

    def __init__(self, code, text):
        super(YaDiskException, self).__init__(text)
        self.code = code

    def __str__(self):
        return "%d. %s" % (self.code, super(YaDiskException, self).__str__())