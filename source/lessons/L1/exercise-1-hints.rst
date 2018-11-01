Exercise 1 hints
================

Add below some tips for working on Exercise 1 if needed.

Check of what type an object is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``isinstance(actual_object, variable_type)`` function is a Python builtin function that will answer your question,
if the ``actual_object`` is of the variable typpe ``variable_type``. Basic types are for example:

- str: String
- int: Integer number
- float: Floating point numbers
- list: List of thing aka [ ] brackety things
- dict: Dictionaries, Python versatile data structures, based on associative lists and objects, where you address via named fields (see Python recap lecture)

An example:

.. ipython:: python

    a_string_var = "I am a string"
    an_int_var = 42
    a_float_var = 3.5
    a_boolean_true_false_var = True

    is_string = isinstance(a_string_var, str)
    print(is_string)
    is_int = isinstance(an_int_var, int)
    print(is_int)
    is_float = isinstance(a_float_var, float)
    print(is_float)
    true_or_false = isinstance(a_float_var, str)
    print(true_or_false)


Control flow for checks with ``if`` and ``else``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to make a "left" or "right" decision, you can use Python's if then construct.
For that you need to check a *condition* (or a fact)  if it's *true* or *false*. If it's true, go only through the first block,
if it's false, go only through the else block.

.. code::

    initial_demo_output = 0

    if 3 > 2:
        print("3 is larger than 2")
        initial_demo_output = 3
    else:
        print("3 not larger than 2")
        initial_demo_output = 2

    # guess the final value of ``initial_demo_output`` ?
    print(initial_demo_output)


Reading a CSV file into Pandas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With Python it is basically possible to read data from any kind of input datafile (such as csv-, txt-, etc).
The widely used library Pandas can easily read a file with tabular data and present it to us as a so called dataframe:

.. ipython:: python

    import pandas as pd

    # make sure you have the correct path to your working file, ideally in the same folder
    df = pd.read_csv('source/_static/data/L1/global-city-population-estimates.csv', sep=';', encoding='latin1')

    pd.set_option('max_columns',20)
    print(df.head(5))


Applying a function to every row of a Pandas dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ipython:: python

    # we make a function, that takes a row object coming from Pandas. The single fields per row are addressed by their column name.
    def increase_by_factor_2(row):
        field_value = row['Population_2015']
        calc_value = field_value * 2
        return calc_value

    # Go through every row, and calculate the value for  a new column ``Population_doubled``, by **apply**ing the function from above (downwards row by row -> axis=1)
    df['Population_doubled'] = df.apply(increase_by_factor_2, axis=1)

    print(df.head(5))

