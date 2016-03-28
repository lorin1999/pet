# Yet another course? Really?

> Everything has been said but not everyone has said it.

> -- Not everyone yet

It's not a course. It's exactly, what it says on the tin. It's a toolkit for exploring Python. in the context of this ~~course~~toolkit I hereby define the word "tool" as anything that might help you to further your knowledge in Python (ha! I can do anything now). If you use these tools regularly for a while you might learn programming in Python as a side effect.

if you already know a different programming language you have some of your own tools already and only need to pick the more Python-specific tools provided here. If you are completely new to programming, you might need all of the tools. Wherever you start, if you work your way through you will also get insights into the culture surrounding the Python language and where you can find more help and resources.

## Toolkit content overview

> Our chief weapon is introspection and software tools ... Our **two** weapons are introspection and software tools ... and exercise... Our **three** weapons are introspection, software tools and exercises and self referential automation. 

> me

It's not as funny now ... [I guess you had to be there](https://www.youtube.com/watch?v=Nf_Y4MbUCLY).

### Introspection

Python is a very introspective language. It contains a lot of functionality that invites you to explore it. For me this is a great way to learn and especially to learn about ones wrong assumptions about how things work by actually investigating what is really happening. This prevents [magical thinking](https://en.wikipedia.org/wiki/Cargo_cult_programming) without completely taking the [magic](http://www.outpost9.com/reference/jargon/jargon_46.html) out :).

[![Introspection](https://goo.gl/sq1OkT)](https://en.wikipedia.org/wiki/Droste_effect)

## Exercises

Try to see the exercises as micro programming projects. You are presented with a problem and you are supposed to solve it by writing Python code. If you look at it this way, writing "real" programs is basically just sticking a lot of completed micro projects together in the right way. The art in writing complex programs is to discombobulate that scary huge problem into a collection of many solvable micro problems/projects. It really is that simple. Just like playing Beethovens' 9th on the piano can be broken down into learning to play many little phrases and chords until you're comfortable and then sticking them all together in the right order. It might take a while to practice them, but once you did that, putting it all together is not too hard anymore.

### How should you go about doing the exercises

This is not about just trying to find out how to this as fast as possible. This is also about getting comfortable with the tools and developing an approach to solving programming problems in general.

Try solving the given exercises one after the other by **only** using the [internal documentation and introspection functions](../introspection/README.md#classic-introspection-in-python). Also: try solving the exercises alternating between the different [software tools](../introspection/README.md#tools-for-exploration). This way you can start to get a feeling for the differences in the tools and the different working styles they support. Try to find out which way of working and exploring feels best for you. This is really a matter of taste and how you tick. People who love the commandline do a lot of their code preparation in Ipython. A lot of scientists love to work in Jupiter notebooks. I do almost everything in PyCharm.

If you are getting frustrated please do not jump right into Google. First try the [howdoi](https://pypi.python.org/pypi/howdoi) command line tool (`pip install howdoi`) and see if you can get unstuck this way. Howdoi is basically almost like gooogling for programmers. It queries [Stack Overflow](http://stackoverflow.com/) (SO), which turned into the de facto help system for many programmers since it's inception in 2008. Using that tool feels astonishingly like asking a human directly on your commandline (which it basically is). 

BTW: there is even [SO code completion for JavaScript](https://emilschutte.com/stackoverflow-autocomplete/) ;)

### Software tools

[![Wenger Giant](https://c2.staticflickr.com/6/5183/5755042801_850b1ffb2c_b.jpg)](https://www.flickr.com/photos/ojimbo/5755042801)

A programming language does not exist in a vacuum. The software tooling that develops around it plays a just as important role. Python has an astonishing set of great and mostly free software tools. 

### Self referential Automation

> I have a well-deserved reputation for being something of a gadget freak, and am rarely happier than when spending an entire day programming my computer to perform automatically a task that would otherwise take me a good ten seconds to do by hand.

> Douglas Adams 

[![relevant XKCD](http://imgs.xkcd.com/comics/automation.png)](http://xkcd.com/1319/)

By creating this toolkit I am also creating a whole new set of problems for myself that have to do with this very toolkit. Are all the executable examples and exercises working properly?  How can I make sure that all the links I am using are working? Are all finished documents included properly in the table of contents? Questions over questions that each one can be dealt with in four different ways (that I know of):
     
* Ignore the problems and accept defeat
* Continuous manual checking for problems
* Use of existing automatic tools
* Creation of custom automatic tools

I chose the last option (but without completely reinventing the wheel ... hopefully). The tools that solve the problems that came into live by creating this toolkit can also serve as material to learn more about Python, because they are part of this toolkit (are you still following?). If only Escher could see me now - he would be proud of me.

[![M.C. Escher, Drawing Hands, 1948](http://c7.staticflickr.com/4/3016/2879644822_34d42d0413_b.jpg)](https://www.flickr.com/photos/jameswy_wang/2879644822/in/photostream/)
