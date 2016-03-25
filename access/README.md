# Access restrictions and information hiding

# Restricting access to objects and their functionality

Many other languages have concepts of private and public members to restrict access to functionality that is considered private by the author. Python hasn't. The philosophical idea behind that has been boiled down to the phrase "We are all consenting adults" - although it [has been noted](https://github.com/kennethreitz/python-guide/issues/525) that a significant part of people programming in Python is actually under the age of consent, so we should rephrase it to "We are all responsible users". But I digress. Python has no way of completely hiding information as it was suggested by David Parnas a long time ago. Python actually flaunts all the information you might want about pretty much anything, which I personally consider to be one of the big strengths of the language. Pretty much every aspect of a program in execution is explorable and even changeable, which makes it the perfect language for people who want to see how things work on their chosen level of abstraction and who like to tinker. I suspect that is one of the reasons, why Python is so strong among scientists and engineers (which usually are curious people who like to tinker).

So in Python you're left with different levels of politely telling the user "Please don't touch this" ([demo](access.ipynb)) and this seems to be good enough. People new to the language are shocked by this laissez fair approach but they quickly come around or move on to [Haskell](https://www.haskell.org/) or [Clojure](https://clojure.org/).

# Restricting Write access to objects

A lot of other languages have so called `constants` (something you set once and that never changes - guaranteed by the language). Python has not. This is due to the nature of the language and the way Python doesn't really have variables, only names. The thing with names is the they can always bind to something else, so a name can by definition never contaion a value that can't change, because you can just change the thing the name binds to. Don't get me wrong. Python has objects that never change. Quite a lot actually, but that still does not get you constants, as you can't tell a name, that it is not allowed to bind to a changing number of unchangeable (a.k.a. immutable) objects.
 
 The fact that Python does not have constants does not seem to pose a big problem either. If you read the section about constants in the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/#constants) ...
  
  > Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.
  
... you could actually start to believe that Python has constants but all PEP8 does is describe a convention which basically says: Please do not change this. That's all. But it seems to be enough.

# Add access restrictions and information hiding to your programs

*Don't get your hopes up :)*

There are definitely ways to modify a program in a way that bindings can act like constants. Because if you think about it, having a constant just means that you have an object, which raises an Exception if a value that was once set is being changed. This is definitely possible and it has been done. If you really need to do this at some point of your programming life, you will find ways to do this. [That's all I will say for now](http://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991).

There are also ways to create more rigid restrictions to attribute access and information hiding. But these are advanced topics and you definitely don't need to know about them just yet.
