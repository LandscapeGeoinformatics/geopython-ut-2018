Recap Python Basics
===================

This lesson contains a curated collection of Jupyter Notebooks of
introductory materials about programming in Python.

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code,
equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling,
data visualization, machine learning, and much more.


Getting started - Set up a project folder
-----------------------------------------

You need to organise your files and scripts in a folder, that you find again, is easy to navigate to, and sits on a hard drive on your computer.

On Windows you have your local user folder, typically ``C:\Users\Alexander``. Open with the Windows File Explorer and create a new folder in this folder, with the name "geopython".

If you don't have the Anaconda Prompt open, please open it and activate your correct Python environment:

.. code::

    (C:\dev\conda3)  activate geopython-environment

    (geopython-environment)

As this is still the "normal" Windows command line, you can navigate through the folders. Change your working directory of the Command line window to your "geopython" folder:

.. code::

    c:
    cd C:\Users\Alexander\geopython

You can see which files are inside this folder by using the ``dir`` command. (On Mac and Linux it is ``ls``) and it will print information and files of your current folder.

.. code::

    c:
    cd C:\Users\Alexander\geopython
    
    dir

    ... output below
    
    Volume in drive C is Windows
    Volume Serial Number is 5E4C-FED5
    
    Directory of C:\Users\Alexander\geopython
    
    29.10.2018  15:00    <DIR>          .
    29.10.2018  15:00    <DIR>          ..

It is important to understand, that you are always "residing" somewhere in some folder. Therefore, make sure you navigate explicitly into your correct working folder "geopython".

Python Refresher as Jupyter Notebooks
-------------------------------------

In the previous sections you should have installed all required packages for your conda environment, including the Jupyter Notebook.

Download the linked **.ipynb** files (Jupyter Notebook files) and save them into your "geopython" folder.
Go back into the console/commandline prompt, make sure you are in the directory where you extracted the materials. There you should now start the Jupyter notebook.

All you need to do to play notebooks is to type the following command in your project folder:

.. code::

    cd C:\Users\Alexander\geopython

    (geopython-environment) jupyter notebook

A browser window will open, with the files listed from your geopython folder. In order to start a Notebook, click on the respective **.ipynb** file.
This will open a new tab in the browser and now you have a running Jupyter notebook session.
Cells are tyically either Code (Python) that you can run/execute, or descriptive text in Markdown format.

- `Chapter 1: Variables, Strings and Numbers.ipynb <../../_static/data/L0/01%20Variable%20Strings%20and%20Numbers.ipynb>`_ In this section, you will learn to store information in variables.

- `Chapter 2: Lists, Tuples and Sets.ipynb <../../_static/data/L0/02%20List%20and%20Tuples%20and%20Sets.ipynb>`_ In this notebook, you will learn to store more than one valuable in a single variable.

- `Chapter 3: If Statements <../../_static/data/L0/03%20If%20Statements.ipynb>`_ In this section, you will learn how to test for certain conditions, and then respond in appropriate ways to those conditions.

- `Chapter 4: Loops and Input.ipynb <../../_static/data/L0/04%20While%20Loops%20and%20User%20input.ipynb>`_ While loops are really useful because they let your program run until a user decides to quit the program. They set up an infinite loop that runs until the user does something to end the loop. This section also introduces the first way to get input from your program's users.

- `Chapter 5: Dictionaries.ipynb (Data Structures) <../../_static/data/L0/05%20Dictionaries.ipynb>`_ Dictionaries allow us to store connected bits of information. For example, you might store a person's name and age together.

- `Chapter 6: Introducing Functions.ipynb <../../_static/data/L0/06%20Introduction%20to%20Functions.ipynb>`_ Functions mean less work for us as programmers, and effective use of functions results in code that is less error-prone.

- `Chapter 7: Classes and OOP.ipynb <../../_static/data/L0/07%20Classes%20and%20OOP.ipynb>`_ In this section you will learn about the last major data structure, classes. Classes are quite unlike the other data types, in that they are much more flexible. Classes allow you to define the information and behavior that characterize anything you want to model in your program.

- `Chapter 8: Exceptions.ipynb <../../_static/data/L0/08%20Exceptions.ipynb>`_ Exceptions which are events that can modify the *flow* of control through a program. In Python, exceptions are triggered automatically on errors, and they can be triggered and intercepted by your code.

- `Appendix: Python Coding Style.ipynb <../../_static/data/L0/Python%20Coding%20Style.ipynb>`_ You are now starting to write Python programs that have a little substance. Your programs are growing a little longer, and there is a little more structure to your programs. This is a really good time to consider your overall style in writing code.


License and Sharing Material
----------------------------

Valerio Maggio `<https://github.com/leriomaggio/python-in-a-notebook>`_

.. raw:: html

    <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.