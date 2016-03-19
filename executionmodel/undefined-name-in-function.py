def contains_undefined_name():
    maybeIamDefinedMaybeNot

print "after undefined name in function"  # Will this be executed?

if False:
    adrfse = 'I am defined as global to the module'

contains_undefined_name()
