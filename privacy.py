"""
We are all consenting adults ...

About levels of privacy in Python:

* Attributes starting with an underscore are considered private by convention
* Attributes starting with two underscores are made private with name mangling
* Attributes starting and ending with two underscores are part of internal
  mechanics and protocols
"""
def contains_undefined_name():
    adrfse

print "after undefined name"  # Will this be executed?

def i_contain_broken_syntax():
    definitely broken syntax :)

print "after broken syntax"  # and this?
