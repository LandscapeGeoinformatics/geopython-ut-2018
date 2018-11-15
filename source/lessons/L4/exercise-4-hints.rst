Exercise 4 hints
================

General
-------

- Documentation of the Travel Time Matrix dataset and explanation for different column names can be found at the Accessibility Research Group website: `Helsinki Region Travel Time Matrix 2015 <http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015>`__
- If visualizing takes for ever (as computer instance can be a bit slow), it is enough that you visualize only one map using plotting in Geopandas. If it is really slow, you can do the visualization also using the QGIS in the computer instance or even ArcGIS in the GIS-lab.

Problem 1
---------

- Note that the input travel time data is stored in text files when reading in the data.
- Keep columns `'from_id'`,`'to_id'`,`'pt_r_tt'` and `'car_r_t'` in the travel time data files
- Join the data using columns `'from_id'` from the travel time data, and `'YKR_ID'` in the grid-shapefile
- See hints for joining the travel time data to the grid shapefile from our earlier materials from the lesson regarding classifying the bogs via the landuse legend file.
- Plotting the data takes a while (be patient!)


Reading multiple files efficiently
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we are reading multiple files from a folder. We could write the filepaths to all of those files but **it is not efficient!**
Instead, you should use `glob()` -function from module glob to get a filtered list of those files that you want to read and then read the files by iterating over the list.

Listing and searching for file path names from file system can be done using a specific module called `glob <https://docs.python.org/3/library/glob.html>`__.

The glob library contains a function, also called glob, that finds files and directories whose names match a pattern.
We provide those patterns as strings: the character * matches zero or more characters, while ? matches any one character.

- We can use this to get the names of all files in the data directory (C:\Users\Alex\geopython\L4):

.. code:: python

  In [0]: import glob
  In [1]: my_files = glob.glob('Data\\*')
  In [2]: print(my_files)
  ['Data\\inflammation-08.csv',
   'Data\\inflammation-10.csv',
   'Data\\inflammation-11.csv',
   'Data\\inflammation-06.csv',
   'Data\\inflammation-12.csv',
   'Data\\small-03.csv',
   'Data\\small-02.csv',
   'Data\\inflammation-07.csv',
   'Data\\inflammation-05.csv',
   'Data\\small-01.csv',
   'Data\\inflammation-03.csv',
   'Data\\inflammation-04.csv',
   'Data\\inflammation-02.csv',
   'Data\\inflammation-01.csv',
   'Data\\inflammation-09.csv']

- We can also search for only specific files and file formats. Here, we search for files that starts with the word 'small' and ends with file format '.csv':

.. code:: python

  In [3]: csv_files = glob.glob('Data\\small*.csv')
  In [4]: print(csv_files)
   ['Data\\small-03.csv', 'Data\\small-02.csv', 'Data\\small-01.csv']

Now we have successfully filtered only certain types of files and as a result we have a list of files that we
can loop over and process.

Renaming column based on 'to_id' value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We want to rename our column from `pt_r_tt` into `pt_r_tt_XXXXXXX` where XXXXXX is a `to_id` of our datafile which is identical for every row. How you should proceed this problem is following:

 - Extract a **single** value from `to_id` column into a variable called `destination` ==> you might want to use `.loc[]` functionality of Pandas
 - Convert the integer value of `destination` variable as **string**
 - Rename the `pt_r_tt` value:

    - Parse the new column name where you combine `pt_r_tt` text and text from `destination` variable into a new variable called `new_name`.
    - Rename the `pt_r_tt` column using value from `new_name` variable.

Finding out which shopping center is the closest

We can find out the minimum value from multiple columns simply by applying a `.min()` function to those columns of a row that we are interessted in:

.. code:: python

    # Define the columns that are used in the query
    value_columns = ['center1', 'center2', 'center3']

    # Find out the minimum value of those column of a given row in the DataFrame
    minimum_values = row[value_columns].min()

It is also possible to find out which column contains that value by applying ``.idxmin()`` -function (`see Pandas docs <http://pandas.pydata.org/pandas-docs/version/0.18.1/generated/pandas.DataFrame.idxmin.html>`__).

.. code:: python

    # Find out which column contains the minimum value
    closest_center = row[value_columns].idxmin()

In order to calculate the results for each row, you can take advantage of the `.iterrows()` and `.loc()` -functions in (geo)pandas.
We already practiced these functions before.