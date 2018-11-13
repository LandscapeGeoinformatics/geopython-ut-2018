Data reclassification
=====================

Reclassifying data based on specific criteria is a common task when doing GIS analysis.
The purpose of this lesson is to see how we can reclassify values based on some criteria which can be whatever, such as:

.. code::

    1. if available space in a pub is less than the space in my wardrobe

    AND

    2. the temperature outside is warmer than my beer

    ------------------------------------------------------

    IF TRUE: ==> I go and drink my beer outside
    IF NOT TRUE: ==> I go and enjoy my beer inside at a table

Even though, the above would be an interesting study case, we will use slightly more traditional cases to learn classifications.
We will use Corine land cover layer from year 2012, and a Population Matrix data from Estonia to classify some features of them based on our own
self-made classifier, or using a ready made classifiers that are commonly used e.g. when doing visualizations.

The target in this part of the lesson is to:

1. classify the bogs into big and small bogs where

    - a big bog is a bog that is larger than the average size of all bogs in our study region
    - a small bog ^ vice versa

2. use travel times and distances to find out

   - good locations to buy an apartment with good public tranportation accessibility to city center
   - but from a bit further away from city center where the prices are lower (or at least we assume so).

3. use ready made classifiers from pysal -module to classify travel times into multiple classes.

Download data
-------------

Download (and then extract) the dataset zip-package used during this lesson `from this link <../../_static//L4/L4.zip>`_.

You should have following Shapefiles in the ``data`` folder:

.. code::

    corine_legend/    corine_tartu.shp            population_admin_units.prj
    corine_tartu.cpg  corine_tartu.shp.xml        population_admin_units.sbn
    corine_tartu.dbf  corine_tartu.shx            population_admin_units.sbx
    corine_tartu.prj  L4.zip                      population_admin_units.shp
    corine_tartu.sbn  population_admin_units.cpg  population_admin_units.shp.xml
    corine_tartu.sbx  population_admin_units.dbf  population_admin_units.shx


Data preparation
----------------

Before doing any classification, we need to prepare our data a little bit.

Let's read the data in and have a look at the columnsand plot our data so that we can see how it looks like on a map.

.. ipython:: python
    :suppress:

      import gdal
      import geopandas as gpd
      import matplotlib.pyplot as plt
      import os

      fp = os.path.join(os.path.abspath('data'), "corine_tartu.shp")
      data = gpd.read_file(fp)

      import pandas as pd
      fp2 = os.path.join(os.path.abspath('data'), "corine_legend")
      fp_clc = os.path.join(fp2, "clc_legend.csv")
      data_legend = pd.read_csv(fp_clc, sep=';', encoding='latin1')



.. code::

   import pandas as pd
   import geopandas as gpd
   import matplotlib.pyplot as plt

   # File path
   fp = r"Data\corine_tartu.shp"

   data = gpd.read_file(fp)

   import pandas as pd
   fp_clc = r"Data\corine_legend\clc_legend.csv"
   data_legend = pd.read_csv(fp_clc, sep=';', encoding='latin1')

Let's see what we have.

.. ipython:: python

   data.head(5)

We see that the Land Use in column "code_12" is numerical and we don't know right now what that means.
So we should at first join the "clc_legend" in order to know what the codes mean:

.. code::

   import pandas as pd
   import geopandas as gpd
   import matplotlib.pyplot as plt

   # File path
   fp = r"Data\corine_tartu.shp"

   data = gpd.read_file(fp)

   import pandas as pd
   fp_clc = r"Data\corine_legend\clc_legend.csv"
   data_legend = pd.read_csv(fp_clc, sep=';', encoding='latin1')
   data_legend.head(5)


We could now try to merge / join the two dataframes, ideally by the 'code_12' column of "data" and the "CLC_CODE" of "data_legend".

.. code::

    display(data.dtypes)
    display(data_legend.dtypes)
    data = data.merge(data_legend, how='inner', left_on='code_12', right_on='CLC_CODE'))

But if we try, we will receive an error telling us that the columns are of different data type and therefore can't be used as join-index.
So we have to add a column where have the codes in the same type. I am choosing to add a column on "data", where we transform the String/Text based "code_12" into an integer number.

.. ipython:: python

    def change_type(row):
        code_as_int = int(row['code_12'])
        return code_as_int

    data['clc_code_int'] = data.apply(change_type, axis=1)
    data.head(2)

Here we are "casting" the String-based value, which happens to be a number, to be interpreted as an actula numeric data type.
Using the  ``int()`` function. This can go wrong if the String cannot be interpreted as a number, and we should be more defensive.

Now we can merge/join the legend dateframe into ourcorine landuse dataframe:

.. ipython:: python

    data = data.merge(data_legend, how='inner', left_on='clc_code_int', right_on='CLC_CODE', suffixes=('', '_legend'))


We have now also added more columns. Let's drop a few, so we can focus on the data we need.

.. ipython:: python

    selected_cols = ['ID','Remark','Shape_Area','CLC_CODE','LABEL3','RGB','geometry']

    # Select data
    data = data[selected_cols]

    # What are the columns now?
    data.columns

Let's plot the data and use column 'CLC_CODE' as our color.

.. ipython:: python

   data.plot(column='CLC_CODE', linewidth=0.05)

   # Use tight layout and remove empty whitespace around our map
   @savefig corine-CLC_CODE.png width=7in
   plt.tight_layout()


.. image:: ../../_static/corine-CLC_CODE.png

Let's see what kind of values we have in 'code_12' column.

.. ipython:: python

   print(list(data['CLC_CODE'].unique()))
   print(list(data['LABEL3'].unique()))

Okey we have different kind of land covers in our data. Let's select only bogs from our data. Selecting specific rows from a DataFrame
based on some value(s) is easy to do in Pandas / Geopandas using the indexer called ``.loc[]``, read more from `here <http://pandas.pydata.org/pandas-docs/stable/indexing.html#different-choices-for-indexing>`_.

.. ipython:: python

   # Select bogs (i.e. 'Peat bogs' in the data) and make a proper copy out of our data
   bogs = data.loc[data['LABEL3'] == 'Peat bogs'].copy()
   bogs.head(2)

Calculations in DataFrames
--------------------------

Okey now we have our bogs dataset ready. The aim was to classify those bogs into small and big bogs based on **the average size of all bogs** in our
study area. Thus, we need to calculate the average size of our bogs.

Let's check the coordinate system.

.. ipython:: python

   # Check coordinate system information
   data.crs

Okey we can see that the units are in meters and we have a `projected coordinate system.  <http://spatialreference.org/ref/epsg/etrs89-etrs-laea/>`_

Let's calculate first the are of our bogs.

.. ipython:: python

   # Calculate the area of bogs
   bogs['area'] = bogs.area

   # What do we have?
   bogs['area'].head(2)

Notice that the values are now in square meters. Let's change those into square kilometers so they are easier to read. Doing calculations in Pandas / Geopandas
are easy to do:

.. ipython:: python

   bogs['area_km2'] = bogs['area'] / 1000000

   # What is the mean size of our bogs?
   l_mean_size = bogs['area_km2'].mean()
   l_mean_size

Okey so the size of our bogs seem to be approximately 1.58 square kilometers.

.. note::

   It is also easy to calculate e.g. sum or difference between two or more layers (plus all other mathematical operations), e.g.:

   .. code:: python

      # Sum two columns
      data['sum_of_columns'] = data['col_1'] + data['col_2']

      # Calculate the difference of three columns
      data['difference'] = data['some_column'] - data['col_1'] + data['col_2']


Classifying data
----------------

Creating a custom classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's create a function where we classify the geometries into two classes based on a given ``threshold`` -parameter.
If the area of a polygon is lower than the threshold value (average size of the bog), the output column will get a value 0,
if it is larger, it will get a value 1. This kind of classification is often called a `binary classification <https://en.wikipedia.org/wiki/Binary_classification>`_.

First we need to create a function for our classification task. This function takes a single row of the GeoDataFrame as input,
plus few other parameters that we can use.

.. code::

   def binaryClassifier(row, source_col, output_col, threshold):
       # If area of input geometry is lower that the threshold value
       if row[source_col] < threshold:
           # Update the output column with value 0
           row[output_col] = 0
       # If area of input geometry is higher than the threshold value update with value 1
       else:
           row[output_col] = 1
       # Return the updated row
       return row


.. ipython:: python
   :suppress:

      def binaryClassifier(row, source_col, output_col, threshold):
          # If area of input geometry is lower that the threshold value
          if row[source_col] < threshold:
              # Update the output column with value 0
              row[output_col] = 0
          # If area of input geometry is higher than the threshold value update with value 1
          else:
              row[output_col] = 1
          # Return the updated row
          return row

Let's create an empty column for our classification

.. ipython:: python

   bogs['small_big'] = None

We can use our custom function by using a Pandas / Geopandas function called ``.apply()``.
Thus, let's apply our function and do the classification.

.. ipython:: python

   bogs = bogs.apply(binaryClassifier, source_col='area_km2', output_col='small_big', threshold=l_mean_size, axis=1)

Let's plot these bogs and see how they look like.

.. ipython:: python

   bogs.plot(column='small_big', linewidth=0.05, cmap="seismic")

   @savefig small-big-bogs.png width=6in
   plt.tight_layout()


.. image:: ../../_static/small-big-bogs.png

Okey so it looks like they are correctly classified, good. As a final step let's save the bogs as a file to disk.

.. code:: python

    outfp_bogs = r"Data\bogs.shp"
    bogs.to_file(outfp_bogs)

.. ipython:: python
   :suppress:

    outfp_bogs = os.path.join(os.path.abspath('data'), "bogs.shp")
    bogs.to_file(outfp_bogs)

.. note::

   There is also a way of doing this without a function but with the previous example might be easier to understand how the function works.
   Doing more complicated set of criteria should definitely be done in a function as it is much more human readable.

   Let's give a value 0 for small bogs and value 1 for big bogs by using an alternative technique:

   .. code:: python

      bogs['small_big_alt'] = None
      bogs.loc[bogs['area_km2'] < l_mean_size, 'small_big_alt'] = 0
      bogs.loc[bogs['area_km2'] >= l_mean_size, 'small_big_alt'] = 1


.. todo::

   **Task:**

   Try to change your classification criteria and see how your results change! Change the LandUse Code/Label and see how
   they change the results.


Classification based on common classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Pysal <http://pysal.readthedocs.io/en/latest/>`_ -module is an extensive Python library including various functions and tools to
do spatial data analysis. It also includes all of the most common data classifiers that are used commonly e.g. when visualizing data.
Available map classifiers in pysal -module are (`see here for more details <http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html>`_):

 - Box_Plot
 - Equal_Interval
 - Fisher_Jenks
 - Fisher_Jenks_Sampled
 - HeadTail_Breaks
 - Jenks_Caspall
 - Jenks_Caspall_Forced
 - Jenks_Caspall_Sampled
 - Max_P_Classifier
 - Maximum_Breaks
 - Natural_Breaks
 - Quantiles
 - Percentiles
 - Std_Mean
 - User_Defined


For this we will use the Adminstrative Units dataset for population.
It is in the Estonian "vald-kond" level, which compares to the level at municipality.
It has the following fields:

- VID, an Id for the "vald"
- KOOD, a unique code for the Statistics Board
- NIMI, the name of the municipality
- population, the population, number of people living
- geometry, the polygon for the municpality district border

Let's apply one of those classifiers into our data and classify the travel times by public transport into 9 classes.

.. ipython:: python
    :suppress:

      import gdal
      import geopandas as gpd
      import matplotlib.pyplot as plt
      import os

      fp = os.path.join(os.path.abspath('data'), "population_admin_units.shp")
      acc = gpd.read_file(fp)


.. code::

   import geopandas as gpd
   import matplotlib.pyplot as plt

   # File path
   fp = r"Data\population_admin_units.shp"
   acc = gpd.read_file(fp)



.. ipython:: python

  import pysal as ps

  # Define the number of classes
  n_classes = 5

The classifier needs to be initialized first with ``make()`` function that takes the number of desired classes as input parameter.

.. ipython:: python

  # Create a Natural Breaks classifier
  classifier = ps.Natural_Breaks.make(k=n_classes)

Now we can apply that classifier into our data quite similarly as in our previous examples.

.. ipython:: python

  # Classify the data
  acc['population_classes'] = acc[['population_int']].apply(classifier)

  # Let's see what we have
  acc.head()

Okey, so we have add a column to our DataFrame where our input column was classified into 5 different classes (numbers 0-4) based on `Natural Breaks classification <http://wiki.gis.com/wiki/index.php/Jenks_Natural_Breaks_Classification>`_.

Great, now we have those values in our population GeoDataFrame. Let's visualize the results and see how they look.

.. ipython:: python

    # Plot
    acc.plot(column="population_classes", linewidth=0, legend=True);

    # Use tight layour
    @savefig natural_breaks_population.png width=7in
    plt.tight_layout()

.. image:: ../../_static/natural_breaks_population.png

.. todo::

   **Task:**

   Try to test different classification methods 'Equal Interval', 'Quantiles', and 'Std_Mean' and visualise them.

