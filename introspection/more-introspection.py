import sys
import sysconfig
import inspect

print sys.path
print sys.executable
print sys.exec_prefix
print sys.real_prefix

print sysconfig.get_platform()
print sysconfig.get_python_version()

print inspect.getargspec(inspect.getcallargs)
