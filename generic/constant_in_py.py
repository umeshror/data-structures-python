def constant(f):
    def fset(self, value):
        """
        function to be used for setting an attribute value
        Will Throw error if executes
        """
        raise TypeError

    def fget(self):
        """
        function to be used for getting an attribute value
        """
        return f()
    return property(fget, fset)


class _Const(object):
    @constant
    def FOO():
        return 0xBAADFACE

    @constant
    def BAR():
        return 0xDEADBEEF


CONST = _Const()

print(CONST.FOO)

##3131964110

CONST.FOO = 0
##Traceback (most recent call last):
##    ...
##    CONST.FOO = 0
##TypeError
