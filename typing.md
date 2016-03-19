#  Typing

This is not about typing in code but about what kind of language Python is. There are two main ways people talk about how typing is implemented .

## Weak vs strong typing

This is basically unhelpful for almost all important languages in use today. See if you can make sense of [the Wikipedia article](https://en.wikipedia.org/wiki/Strong_and_weak_typing). This post is helpful to understand the weaknesses of making those distinctions: [C# is strongly and weakly typed](http://ericlippert.com/2012/10/15/is-c-a-strongly-typed-or-a-weakly-typed-language/)

With this in mind: on a scale from 1 to 10 Python is maybe an 8 on the strongness of typing, as it does little coercion and no casting, but only type conversion by creating new objects (e.g. `int('3')` is creating a new int object from the information given by the string).

## Static vs dynamic

This is easier: Python is dynamically typed. You never explicitly declare a type when you create an object and you don't have to explicitly state which types are expected as parameters in function definitions.
 
 One important concept in Python follows from that: [duck typing](http://c2.com/cgi/wiki?DuckTyping). This means, that as long as an object contains the data or exhibits the behaviour I care about, I don't actually care about the concrete type.

# Examples

## Python vs Java

[Java variables are like picky club bouncers](http://www.pythontutor.com/visualize.html#mode=edit):

    public class JavaVariables {
        public static void main(String[] args) {
        int a = 1;
        String b = "hello";
        a = b;
        }
    }

[Python names (**better not call them variables**) are like post-its](http://goo.gl/trzP3j)
