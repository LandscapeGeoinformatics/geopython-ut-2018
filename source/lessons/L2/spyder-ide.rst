Working with an IDE (Spyder)
============================

*Different ways to program in Python:*

- on the command line by running "python"
- on the command line by running "ipython" (has more features than plain Python)
- via Jupyter in the browser (formerly IPython notebook -> recognize the origin?)
- with a so called **Integrated Development Environment** (IDE)

All of these use the same Python language underneath, they just give you different ways to interact with Python.
Each way has advantages and disadvantages, depending on what you want to do.

Programming on the console is practical for quickly testing/prototyping of a function or a short computation.

With Jupyter notebooks it is easy to share workflows, because they can contain actual Python code, longer explanations with nicely formatted tables and figures in separate Markdown cells, and also the computed results.

With an IDE you get a *super-charged* editor that helps you with writing more sophisticated code, manage a Python coding project, analyse functions and modules and helps you with auto-completing / typing-suggestion for function calls and Python code in general. Consider the following:

*Modules in Python:*

You are aware that you can add functions to your Python program from exisitng packages (aka libraries, aka modules):

To use a module in Python, e.g., the math module, you import it: ``import math``
You can then use a math function as follows: ``y = math.exp(x)``
Modules are an elegant way of separating functionality, to avoid clashes where two functions have the same name but do different things.

The IDE "knows" about modules and will help you importing the right one, telling you what's inside such a modules and then provides suggestions while you type, based on the modules you have imported.

*Data types in Python*

- Python knows basic data types (such as integers or floating point numbers)
- Basic data types can be combined in lists, e.g., ``lst = [1, 2.3, "hi there"]``
- Lists can also be nested: ``nested_list = [1, [2, 3]]``
- List elements can be retrieved by using indices: ``lst[1]`` returns the second element (indexing starts at 0 for the first element)
- Dictionaries are indexed lists: ``mydict = {"a" : 1984, "b": 1995}``
- You can now use the index "b" to return the second element: ``mydict["b"]``

The IDE knows these structures and will help you type those correctly.
It wlll also often be able to show you if you missed brackets or quotes.

*Functions and scope*

Functions are a way of bundling up some task that should be repeated many times, e.g., divide a number by 2:

.. code::

    def dividebytwo(number):
        return number/2

The indentation is important: every line after the line that starts with "def" and that is indented belongs to the function.
The function has a different "scope" than the surrounding program: variables that are defined inside the function only exist there, not outside the function.

The IDE will advise you regarding indentation and also "knows" which functions are available.

*Installing Spyder IDE into our environment*

https://docs.spyder-ide.org/

Open ``Anaconda Prompt`` from the the Windows Start Menu, the command line window should be like so:

.. code::

    (base) C:\Users\Alexander>

    or

    (C:\dev\conda3) C:\Users\Alexander>


In order to show all environments that have already been created you can ask conda to list these:

.. code::

    (C:\dev\conda3)  conda env list

Now we want to activate that environment and start working with it:

.. code::

    (C:\dev\conda3)  activate geopython-environment


On the command line type command ``conda install spyder`` in order to install the light-weight scientific Python IDE Spyder with the conda tool into your environment.

.. code::

    (geopython-environment) C:\Users\Alexander> conda install spyder


On the command line type command ``conda install spyder`` in order to install the light-weight scientific Python IDE Spyder with the conda tool into your environment.

.. code::

    (geopython-environment) C:\Users\Alexander> conda install spyder


If the install ended correctly you can start the Spyder Python IDE directly from the commandline inside of your environment. In this way, The Python interpreter and code analyser in Spyder knows already all your installed packages.

.. code::

    (geopython-environment) C:\Users\Alexander> cd geopython

    (geopython-environment) C:\Users\Alexander\geopython> spyder


You can now try programming and scripting with Spyder instead of a Jupyter notebook.

.. note::

    Spyder has a lot of features. See https://docs.spyder-ide.org/editor.html for more details.

