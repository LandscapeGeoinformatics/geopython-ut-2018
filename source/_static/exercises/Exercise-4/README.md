# Exercise 4

This week we will practice how to do data classification and aggregation in Geopandas. We continue from the last week's exerise with rather similar idea.
The overall aim this week is to define *dominance areas* \[0\] for 8 shopping centers in Helsinki with different travel modes (Public tranport, private car).
The last step is to find out how many people live within the dominance areas of those big shopping centers in Helsinki Region.

*The exercise might be a rather demanding one, so don't panic, the assistants will help you and we will go through the exercise in the following week.*

\[0\]: Here, we define the dominance area of a service as the geographical area from where the given service (shopping center) is the closest one to reach in terms of travel time.

- **Exercise 4 is due by the start of lecture on 27.11**.

- Don't forget to check out the [hints for this week's exercise](https://automating-gis-processes.github.io/2017/lessons/L4/exercise-4-hints.html) if you're having trouble.

- Scores on this exercise are out of **20 points**.

## Problem 1: Join accessibility datasets into a grid and visualize them by using a classifier (6 points)

**Steps:**

 - Download a dataset from [**here**](https://github.com/Automating-GIS-processes/Lesson-4-Classification-overlay/raw/master/data/dataE4.zip) that includes 7 text files containing data about accessibility in Helsinki Region and a Shapefile that contains a Polygon grid that can be used to visualize and analyze the data spatially. The datasets are:
 
     - `travel_times_to_[XXXXXXX]_[NAME-OF-THE-CENTER].txt` including travel times and road network distances to specific shopping center
     - `MetropAccess_YKR_grid_EurefFIN.shp` including the Polygon grid with YKR_ID column that can be used to join the grid with the    accessibility data

 - Read those travel_time data files (one by one) with Pandas and select only following columns from them:
    
    - pt_r_tt
    - car_r_t
    - from_id
    - to_id
  
 - Visualize the **classified** travel times (Public transport AND Car) of at least one of the shopping centers using the classification methods that we went through in the [lesson materials](https://automating-gis-processes.github.io/2017/lessons/L4/reclassify.html). You need to classify the data into a new column in your GeoDataFrame. For classification, you can either:
 
    - Use the [common classifiers from pysal](https://automating-gis-processes.github.io/2017/lessons/L4/reclassify.html#classification-based-on-common-classifiers)
 
    - Or create your own [custom classifier](https://automating-gis-processes.github.io/2017/lessons/L4/reclassify.html#creating-a-custom-classifier). If you create your own, remember to document it well how it works! Write a general description of it and comment your code as well.
 
 - Upload the map(s) you have visualized into your own Exercise 4 repository (they don't need to be pretty). If visualizing takes for ever (as computer instance can be a bit slow), it is enough that you visualize only one map using plotting in Geopandas. If it is really slow, you can do the visualization also using the QuantumGIS in the computer instance or even ArcGIS in the GIS-lab.

## Problem 2: Calculate and visualize the dominance areas of shopping centers (9 points)

In this problem, the aim is to define the dominance area for each of those shopping centers based on travel time. 

How you could proceed with the given problem is: 

 - iterate over the accessibility files one by one
 - rename the travel time columns so that they can be identified 
   - you can include e.g. the `to_id` number as part of the column name (then the column name could be e.g. "pt_r_tt_5987221")
 - Join those columns into MetropAccess_YKR_grid_EurefFIN.shp where `YKR_ID` in the grid corresponds to `from_id` in the travel time data file. At the end you should have a GeoDataFrame with different columns show the travel times to different shopping centers.
 - For each row find out the **minimum** value of **all** pt_r_tt_XXXXXX columns and insert that value into a new column called `min_time_pt`. You can now also parse the `to_id` value from the column name (i.e. parse the last number-series from the column text) that had the minimum travel time value and insert that value **as a number** into a column called `dominant_service`. In this, way are able to determine the "closest" shopping center for each grid cell and visualize it either by travel times or by using the `YKR_ID` number of the shopping center (i.e. that number series that was used in column name).
 - Visualize the travel times of our `min_time_pt` column using a [common classifier from pysal](https://automating-gis-processes.github.io/2017/lessons/L4/reclassify.html#classification-based-on-common-classifiers) (you can choose which one).
 - Visualize also the values in `dominant_service` column (no need to use any specific classifier). Notice that the value should be a number. If it is still as text, you need to convert it first.
 - Upload the map(s) you have visualized into your own Exercise 4 repository (they don't need to be pretty).

## Problem 3: How many people live under the dominance area of each shopping center? (5 points)

Take advantage of the materials last week and find out how many people live under the dominance area of each shopping center. You should first [aggregate](file:///D:/KOODIT/Opetus/Automating-GIS-processes/AutoGIS-Sphinx/build/html/Lesson4-geometric-operations.html#aggregating-data) your dominance areas into a unified geometries using [`dissolve()`](http://geopandas.org/aggregation_with_dissolve.html#dissolve-example) -function in Geopandas. 

## Answers

Write your answers for Problem 3 here.

