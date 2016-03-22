def i_am_a_function():
    pass


class IAmAClass(object):
    """I am a docstring"""
    def i_am_a_class_method(self):
        pass

anInt = 1
aList = [1, 2, 3]  # containing ints
aString = "hello"
aDictionary = {
    'key1': anInt,
    'key2': aString,
    'key3': 'some other string',
}


# Now we access some attributes of the objects ...
print i_am_a_function.__name__
print IAmAClass.__doc__
print anInt.bit_length()

# and now we do some tidying up ...
del i_am_a_function
del IAmAClass
del anInt
del aList
del aString
del aDictionary
print "All gone!"
