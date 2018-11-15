Exercise 4
==========

This lesson we will practice how to do data classification and aggregation in Geopandas.

- Don't forget to check out the [hints for this lesson's exercise](exercise-4-hints.html) if you're having trouble.

- Scores on this exercise are out of **10 points**.

Sections
--------

Problem: Join accessibility datasets into a grid and visualize them by using a classifier (10 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The overall aim this lesson is to define *dominance areas* \[0\] for 8 shopping centers in Helsinki with different travel modes (Public tranport, private car).
The last step is to find out how many people live within the areas of those big shopping centers in Helsinki Region.
We define the geographical area from where the given service (shopping center) is the closest one to reach in terms of travel time.


**Steps:**

 - Download a dataset from `**here** <../../_static/exercises/Exercise-4/data/E4.zip>`_ that includes 7 text files containing data about accessibility in Helsinki Region and a Shapefile that contains a Polygon grid that can be used to visualize and analyze the data spatially. The datasets are:

     - ``travel_times_to_[XXXXXXX]_[NAME-OF-THE-CENTER].txt`` including travel times and road network distances to specific shopping center
     - ``MetropAccess_YKR_grid_EurefFIN.shp`` including the Polygon grid with YKR_ID column that can be used to join the grid with the    accessibility data

 - Read those travel_time data files (one by one) with Pandas and select only following columns from them:

    - pt_r_tt
    - car_r_t
    - from_id
    - to_id

 - Visualize the **classified** travel times (Public transport AND Car) of at least one of the shopping centers using the classification methods that we went through in the `lesson materials <reclassify.html>`_ . You need to classify the data into a new column in your GeoDataFrame. For classification, you can **either**:

    - Use the `common classifiers from pysal <reclassify.html>`_

    - **OR** create your own `custom classifiers from pysal <reclassify.html>`_. If you create your own, remember to document it well how it works! Write a general description of it and comment your code as well.

 - Submit the code as Jupyter notebook or Python Script and the map(s) you have visualized (as png).
 
 
 --------
 In this excercise you will practice making heatmaps with jupyter gmap.
 
 Problem: Create a heatmap of one fenomena (10 points)

 You may use example dataset about Earthquakes which you can download here `**here** <https://www.kaggle.com/usgs/earthquake-database>` 
 or you may also try to use your own dataset or find some interesting dataset from Kaggle `**Kaggle** <https://www.kaggle.com/datasets>`

**Steps:**

 - Download a dataset from `**here** <https://www.kaggle.com/usgs/earthquake-database>` 
    or use your own dataset which has to be initially in csv format (not shp)
    or  find some interesting dataset from Kaggle `**Kaggle** <https://www.kaggle.com/datasets>`. Dataset has to be in csv format (not shp)

 - Read in your csv file and create point geometry from your coordinates
 - Transform the coordinate system into suitable one for your study area
 - Create heatmap using gmaps
 - Submit the code as Jupyter notebook or Python Script and the heatmap you have visualized (as png).
 
 

