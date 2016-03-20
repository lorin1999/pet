"""
We are all consenting adults ...
"""


class PrivacyDemo(object):
    def __init__(self):
        """Special class part of a protocol or language mechanics"""
        print "I am called after object creation to initialize the object"

    @staticmethod
    def _private_by_convention():
        """can be accessed normally, but underscore hints it as internal"""
        print "I am not really private, but my name suggests it"

    @staticmethod
    def __semi_private_by_name_mangling():
        """can still be accessed, but under a different name"""
        print "I am only private if you don't know how to guess my name"

PrivacyDemo()
PrivacyDemo._private_by_convention()
PrivacyDemo._PrivacyDemo__semi_private_by_name_mangling()
