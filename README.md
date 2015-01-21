# python_challenges

Programming exercises for people trying to learn python.

I've found that the best way to really learn a new programming language is to start using it.
Not only is it a great way to internalize the syntax of the language so you don't have to keep
referring back to the manuals, it's also a great way to _prioritize_ your learning.
The best advice I ever got was "Start doing it, and when you get stuck, get help." You can spend
a lot of time going through the manuals and learning about all the different aspects of the language,
but you won't really know what's most important and you won't have much contextual framework on which
to hang your knowledge. You're left with a lot of data, but very little useful information. Think of
it as the difference between knowing trivia, and understanding.

I'm not going to attempt to teach you python, and certainly not programming in general.
These exercises assume you're familiar with at least basic prgramming concepts and the general
syntax of python.

Each exercise is posed as a problem to solve, and is accompanied by my own
solution (or solutions) to the problem, highly annotated with comments. But remember, the whole
point is to try to solve it yourself, that's the best way to learn. My solutions are provided
so that _after_ you solve the problem yourself, you can check to see if we came up with the
same solution and learn from the differences. This is not to say that my solution is better,
but the differences can help you learn new things as well.

Unless otherwise noted, my provided solutions focus primarily on doing things in
conventional, _pythonic_ ways. There are frequently lots of ways that my solutions can
be optimized, but I will generally avoid this if it makes the code too obscure. In some
cases when I find the optimizations to be particularly interesting, I will offer them
as alternate solutions.


## Anatomy of Solutions

Generally speaking, I try to lay out the solutions python scripts in a conventional
way, just like an experienced python developer would lay out any python script so
you can start to become familiar with it. In general, it looks something like this:

```python
#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:

"""
Doc string for the script.
"""

import math

def solution(input):
    """
    Doc string for the solution function
    """

    #Implementation of the solution to the exercise.


if __name__ == '__main__':
    print solution('input value')

```

There are basically five high-level sections to this file:
    1. header comments
    2. file doc string
    3. package imports
    4. solution function (or functions)
    5. main block

### Header Comments

```python
#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:
```

The first line of a python script should always start with a _shebang_. To python,
this is just a comment and doesn't actually effect the execution in any way, but
on certain environments (e.g, Linux), this line allows the script to be executed
directly and tells the shell how to do that (by passing it to python). It's a small
detail, but it's a good convention to follow. The line as shown is widely considered
to be the most portable.

The second line is another special comment that python actually _does_ look at.
Specifically, it tells python that the file is encoded using utf-8. If you get
this wrong, python may not be able to read your file. Or worse, it might read
your file _incorrectly_ which could lead to subtle flaws that are hard to detect.
So make sure you are actually saving your files in UTF-8, which is probably the
default for most editors. Note that pure ASCII (_not_ extended ASCII) is valid
UTF-8 as well.

There are other ways you can format this second line which python will recognize,
and they are described in (PEP-263)[https://www.python.org/dev/peps/pep-0263/].
The specific line that I use also instructs the _editor_ that I use,
(Vim)[http://www.vim.org/], about the UTF-8 encoding. If you're using Emacs,
for instance, there is an alternative format which both python and Emacs will
recognize.


### File Doc String

```python
"""
Doc string for the script.
"""
```

The first (unassigned) string literal in a file is considered a _doc string_ for the file. This
is used to provide help documentation for the file. Doc strings are widely used in
python to provide documentation for modules, functions, classes, fields, and
variables. The built in `help` function can be used to print out this documentation
for any thing that python knows about, and it is also commonly used to generate stand
alone documentation for a python module or package.

Python itself doesn't parse the contents of a doc string at all, but there are a
few common conventions for marking up a doc string. Mark up allows basic formatting
(bold, italics, etc.), linking to other parts of documentation, and in some cases
advanced formatting like tables, figures, and code snippets. Some mark up also provides
_semantic_ markup, so you can do things like specify the parameters and return values
for a function.

Probably the most widely used markup convention for doc strings is 
(reStructuredText)[http://docutils.sourceforge.net/rst.html], also called _rst_.
In particular, an extended form of rst provided by (Sphinx)[http://sphinx-doc.org/],
which also provides tools for actually generating good looking and very useful
documentation from your doc strings. If you've ever read documentation for a python
package on (pythonhosted.org)[http://pythonhosted.org/] or (Read the Docs)[https://readthedocs.org/],
it was probably generated with Sphinx.

My one main complaint about rst markup is that it can be a little difficult to read
unprocessed. In other words, it can create beautiful looking _output_, but the
_input_ can be kind of ugly. I generally go pretty heavy with markup in my doc strings,
but for the sake of clarity, I will generally keep it pretty limited in these files,
so that you can easily read the strings directly in the source code.

### Package Imports

```python
import math
```

Python allows code to be organized into different modules, and even allows modules to
be organized into packages and subpackages. To use something defined in another module
(e.g., a function, class, or variable), you have to `import` it. By convention, all of
your import statements should generally go at the top of your file, just below the file'
doc string.

Of course, if you don't have anything you need to import, there probably won't be any import
statements.


### Solution Function(s)

```python
def solution(input):
    """
    Doc string for the solution function
    """

    #Implementation of the solution to the exercise.
```

Following the imports is where you actually write the rest of your code. For simple
exercises, this may just be a single function, but in some cases there will be 
multiple functions, maybe even classes or global variables.

Functions and classes have _doc strings_, just like the doc string at the top of
the file. Of course, the doc string for a function or class should generally just
provide documentation for that function or class.

The docstring goes immediately after the opening line of the function or class.
If you are looking for an explanation of what the function is for or what it does,
this is the first place to look.


### Main Block

```python
if __name__ == '__main__':
    print solution('input value')
```

Python doesn't have a concept of a "main" function like C or Java. It simply
executes whatever script you tell it to, from top to bottom.

It is a good convention to set up _every_ python file you write so that it can
be imported as a module by another script. When a module is imported, python again
executes it from top to bottom. This is necessary in order to define whatever
classes, functions, and variables the module provides. However, it means that you
have to be careful about what you execute at the top level of your module.

When your file is imported as a module, the special variable `__name__` will be
defined with a string giving the name of your module. However, when your file is
executed as the top level script, this variable will have the value ``'__main__'``.
So testing the value of this special variable, as shown in the `if` block above,
is a good way (and the recommended way) to test whether or not you are the top
level module. The condition will pass (and the contents of the block will be
executed) _if and only if_ your file is the top level script. If your script was
imported, then this block will _not_ be executed.

So when you're writing a script, you will probably want to do things like read
the command line arguments that were provided to your script, execute some code
in reaction to those arguments, and possibly even call `sys.exit()`.

However, if you're script is being imported as a module, you probably _don't_ want
to do any of these things. So _all of these things should generally go inside the main block_. 
Outside of the main block, you define your classes and functions that you need,
and _inside_ the main block you can use those classes and functions to do your top-level
script stuff. By defining them _outside_ the main block, they will be defined even
if you are imported, so other scripts and modules can use them as well.

### `main` Function

Another good convention, which I _will not use_ in the posted code, is to actually put
all of your "top level script" code inside a function itself, conventionally called
`main`. Then your main block doesn't do anything except
call this function.

By encapsulating your top-level script code inside a function, you can still be imported
as a module from some other code, but then that code can optionally call your `main`
function if they want your top-level script to run, acting like a wrapper around your
script.

For real flexibility, you should define your main function like this:

```python
import sys

# ...

def main(args=None):
    if args is None:
        args = sys.argv
        
    ### run your top level script code, using `args` as the command line arguments.

    return 0
```

This allows importing code to pass you a custom sequence of "command line" arguments
if they want.

Note that if you're using the built in `arparse` module to process the command line
arguments (which is a good idea if you have even slightly complex arguments), you
don't even need to use `sys.argv` as shown, bcause the `parse_args` function works
the same way: if you pass in arguments it uses them, if you pass in `None` (or no
arguments), it uses `sys.argv`.

But as I mentioned, I'm not generally going to use a `main` function in the posted
code, because it adds a significant amount of _visual_ complexity to the script,
when I really want to focus primarily on the solution to the challenge. Additionally,
I don't want to mislead anyone into thinking that there is something intrinsically
special about a function named `main`, like there is in other languages.

