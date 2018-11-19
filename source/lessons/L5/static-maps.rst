Static maps
===========

Download datasets
-----------------

Before we start you need to download (and then extract) the dataset zip-package used during this lesson `from this link <../../_static/data/L5/L5.zip>`_.

You should have following Shapefiles in the ``Data`` folder:

  - addresses.shp
  - metro.shp
  - roads.shp
  - TravelTimes_to_5975375_RailwayStation_Helsinki.geojson
  - TravelTimes_to_5975375_RailwayStation.shp
  - Vaestotietoruudukko_2015.shp

Extract the files into a folder called ``Data``:

.. code::

    addresses.cpg             population_square_km.dbf      TravelTimes_to_5975375_RailwayStation.cpg
    addresses.dbf             population_square_km.prj      TravelTimes_to_5975375_RailwayStation.dbf
    addresses.prj             population_square_km.sbn      TravelTimes_to_5975375_RailwayStation.prj
    addresses.shp             population_square_km.sbx      TravelTimes_to_5975375_RailwayStation.shp
    addresses.shx             population_square_km.shp      TravelTimes_to_5975375_RailwayStation.shx
    addresses.txt             population_square_km.shp.xml  TravelTimes_to_5975375_RailwayStation_Helsinki.geojson
    metro.dbf                 population_square_km.shx      TravelTimes_to_5975375_RailwayStation_Helsinki.json
    metro.prj                 roads.dbf                     Vaestotietoruudukko_2015.dbf
    metro.sbn                 roads.prj                     Vaestotietoruudukko_2015.prj
    metro.sbx                 roads.sbn                     Vaestotietoruudukko_2015.shp
    metro.shp                 roads.sbx                     Vaestotietoruudukko_2015.shx
    metro.shx                 roads.shp
    population_square_km.cpg  roads.shx


Static maps in Geopandas
------------------------

We have already seen during the previous lessons quite many examples how to create static maps using Geopandas.

Thus, we won't spend too much time repeating making such maps but let's create a one with more layers on it than just one
which kind we have mostly done this far.

Let's create a static accessibility map with roads and metro line on it.

First, we need to read the data.


.. ipython:: python
   :suppress:

    import os
    import gdal
    import geopandas as gpd
    import maptlotlib.pyplot as plt

    # Filepaths
    grid_fp = os.path.join(os.path.abspath('data'), "TravelTimes_to_5975375_RailwayStation.shp")
    roads_fp = os.path.join(os.path.abspath('data'), "roads.shp")
    metro_fp = os.path.join(os.path.abspath('data'), "metro.shp")


.. code::

    import geopandas as gpd
    import matplotlib.pyplot as plt

    # Filepaths
    grid_fp = r"Data\TravelTimes_to_5975375_RailwayStation.shp"
    roads_fp = r"Data\roads.shp"
    metro_fp = r"Data\metro.shp"


.. ipython:: python

    # Read files
    grid = gpd.read_file(grid_fp)
    roads = gpd.read_file(roads_fp)
    metro = gpd.read_file(metro_fp)


Then, we need to be sure that the files are in the same coordinate system. Let's use the crs of our travel time grid.

.. ipython:: python

    gridCRS = grid.crs
    roads['geometry'] = roads['geometry'].to_crs(crs=gridCRS)
    metro['geometry'] = metro['geometry'].to_crs(crs=gridCRS)

Finally we can make a visualization using the ``.plot()`` -function in Geopandas. The ``.plot()`` function takes all the matplotlib parameters where appropriate.
For example we can adjust various parameters

- ``ax`` if used, then can indicate a joint plot axes onto which to plot, used to plot several times (several layers etc) into the same plot (using the same axes, i.e. x and y coords)
- ``column`` which dataframe column to plot
- ``linewidth`` if feature with an outline, or being a line feature then line width
- ``markersize`` size of point/marker element to plot
- ``color`` colour for the layers/feature to plot
- ``cmap`` `colormaps (*cmap* - parameter) <https://matplotlib.org/users/colormaps.html#grayscale-conversion>`_
- ``alpha`` transparency  0-1
- ``legend`` True/False show the legend
- ``scheme`` one of 3 basic classification schemes ("quantiles", "equal_interval", "fisher_jenks"), beyond that use PySAL explicitly
- ``k`` number of classes for above scheme if used.
- `` vmin`` indicate a minimal value from the data column to be considered when plotting (also affects the classification scheme), can be used to "normalise" several plots where the data values don't aligh exactly
- `` vmax`` indicate a maximal value from the data column to be considered when plotting (also affects the classification scheme), can be used to "normalise" several plots where the data values don't aligh exactly



.. code:: python

    # Visualize the travel times into 9 classes using "Quantiles" classification scheme
    # Add also a little bit of transparency with `alpha` parameter
    # (ranges from 0 to 1 where 0 is fully transparent and 1 has no transparency)
    my_map = grid.plot(column="car_r_t", linewidth=0.03, cmap="Reds", scheme="quantiles", k=9, alpha=0.9, legend=True)

    # Add roads on top of the grid
    # (use ax parameter to define the map on top of which the second items are plotted)
    roads.plot(ax=my_map, color="grey", linewidth=1.5)

    # Add metro on top of the previous map
    metro.plot(ax=my_map, color="red", linewidth=2.5)

    # Remove the empty white-space around the axes
    plt.tight_layout()

    # Save the figure as png file with resolution of 300 dpi
    outfp = r"Data\static_map.png"
    plt.savefig(outfp, dpi=300)

And this is how our map should look like:

.. ipython:: python
   :suppress:

    my_map = grid.plot(column="car_r_t", linewidth=0.03, cmap="Spectral", scheme="quantiles", k=9, alpha=0.9, legend=True);
    roads.plot(ax=my_map, color="grey", linewidth=1.5);
    metro.plot(ax=my_map, color="red", linewidth=2.5);
    @savefig static_map.png width=7in


.. image:: ../../_static/static_map.png


This kind of approach can be used really effectively to produce large quantities of nice looking maps
(*though this example of ours isn't that pretty yet, but it could be*) which is one of the most useful aspects
of coding and what makes it so important to learn how to code.

