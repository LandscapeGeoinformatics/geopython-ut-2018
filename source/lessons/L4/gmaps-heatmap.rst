Heatmaps with the Jupyter Gmaps plugin
======================================

Heatmaps are a good way of getting a sense of the density and clusters of geographical events. They are a powerful tool for making sense of larger datasets.
The `Jupyter **gmaps** plugin <https://jupyter-gmaps.readthedocs.io/en/latest>`_ is a python library that work with the Google maps API to enable users to create great and meaningful maps.

The target in this part of the lesson is to:

- import csv file about offences against property (thefts, robbery etc) in Estonia
- create spatial geometry based on coordinates
- and then create a heatmap and visualise with ``gmaps``

Crime data is open data and originates from Estonian Police and Border Guard Board `open data page <https://www2.politsei.ee/et/organisatsioon/analuus-ja-statistika/avaandmed.dot>`_.
On the police website there are several different datasets for offenses and crimes, such as:

- Avaliku korra vastased ja avalikus kohas toime pandud varavastased süüteod: offenses committed against public order and in public places `avalik_3.csv <https://opendata.smit.ee/ppa/csv/avalik_3.csv>`_
- Varavastased süüteod: Offenses Against Property `vara_1.csv <https://opendata.smit.ee/ppa/csv/vara_1.csv>`_


Environment Preparations
------------------------

Activate your environments and install the `jupyter Gmap plugin <https://jupyter-gmaps.readthedocs.io/en/latest>`_. The easiest way to install gmaps is with conda anyway:

.. code::

    (geopython-environment) C:\Users\Alexander\geopython> conda install -c conda-forge gmaps

Enable ipywidgets widgets extensions:

.. code::

    (geopython-environment) C:\Users\Alexander\geopython> jupyter nbextension enable --py --sys-prefix widgetsnbextension

Then tell Jupyter to load the extension with:

.. code::

    (geopython-environment) C:\Users\Alexander\geopython> jupyter nbextension enable --py --sys-prefix gmaps


Most operations on Google Maps require that you tell Google who you are. As the Gmaps plugin uses the Google Maps Java Script API a lot under the hood we need to follow the `Authentication workflow <https://jupyter-gmaps.readthedocs.io/en/latest/authentication.html>`_ and creating a key, and activate it

For todays lesson we will provide an API key that you'll be able to use for the lesson. However, if you want to use it in other projects you should consider activating your own key, as we will disable this key soon again.

To authenticate with Google Maps, follow the `Google API console instructions <https://console.developers.google.com/flows/enableapi?apiid=maps_backend,geocoding_backend,directions_backend,distance_matrix_backend,elevation_backend&keyType=CLIENT_SIDE&reusekey=true>`_ for creating an API key:


Data download and pre-processing
--------------------------------

This Crime data we will use today is open data and regularly updated and published online at the same spot, so in order to add some more automation we will add the download of the data into our workflow.

.. ipython:: python

    # import common libraries
    import pandas as pd
    import geopandas as gpd
    from shapely.geometry import box, Polygon
    import numpy as np
    # import the very practical urlib library from Python for web transactions, such as file download
    import urllib.request
    # urlretrieve directly downloads the file into a local file handle
    local_file, headers = urllib.request.urlretrieve("https://opendata.smit.ee/ppa/csv/avalik_3.csv")


``urlretrieve(url, filename)`` copies a network object denoted by a URL to a local file (API documentation `here <https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve>`_)

The function returns a tuple ``(filename, headers)`` where filename is the local file name under which the object can be found, because urlretrieve will save in some temporary folder.
And ``headers`` is a more technical information object containing status information for the http request and response.

.. ipython:: python
    print(local_file)


You can also call urlretrieve(url, filename)  with a second argument: if present, specifies the file location to copy to (if absent, the location will be a tempfile with a generated name, as seen above).


.. ipython:: python

    # read the CSV and strip whitespace
    df = pd.read_table(local_file)
    # replace all empty strings with actual NoData values
    df[df == ""] = np.nan
    # show the data
    df.head()


We have many columns, for example:

- JuhtumId: just an Id for each event
- ToimKpv: date of the event
- ToimKell: time of the event
- ToimNadalapaev: weekday
- KohtLiik: a description of the locality where the event happened
- MaakondNimetus: Name of the county (maakond)
- ValdLinnNimetus: name of the municipality/city
- KohtNimetus: local place name/address
- Kahjusumma: monetary value of damage/offense

The data is provided in a normalised gridded fashion, the Lest_X and Y coordinate pairs give the lower and upper boundary of each corner of each grid-square polygon:
- Lest_X: left and right (western, eastern) longitude boundary
- Lest_Y: lower and upper (southern, northern) latitude boundary

You can see the coordinates are provided in a very awkward format, in ``x_min, x_max`` and ``y_min, y_max``. But you can also recognise that they are in a projected CRS, because we don't have GPS coordinates, but metric values that look like the Estonian national grid.

So we need a few steps in order to tease apart the values an build our polygons. Why, because in order to create a heatmap, we need a point dataset, and we will generate the points from the polygon centroids. For now we will use our well-known function syntax again:


.. ipython:: python

    selected_cols = ['ToimKpv', 'ToimKell', 'ToimNadalapaev','KohtLiik','MaakondNimetus','ValdLinnNimetus','KohtNimetus','Kahjusumma','Lest_X','Lest_Y']
    df = df[selected_cols]
    # just so that we can be sure that there are no NaN values for our coordinate work
    df.dropna(subset=['Lest_X', 'Lest_Y'], inplace=True)


We drop all the rows in which the columns 'Lest_X', 'Lest_Y' have these ``nan`` values, because we won't be able to georeference them anyway.

- for each row, take the Lest_X and Lest_Y
- split the String into two fields using "-" as the point where to split
- construct a polygon from 4 points we can build from the separate coordinates
- return the polygon geometry and create the geometry column

.. ipython:: python

    def construct_poly(row):
        # for each row, take the Lest_X and Lest_Y
        lest_x = row['Lest_X']
        lest_y = row['Lest_Y']
        # split the Strings into two fields using "-" as the point where to split
        splitted_x_list = lest_x.split("-")
        splitted_y_list = lest_y.split("-")
        # we can now separate each single coordinate value
        lower_y = int(splitted_y_list[0])
        upper_y = int(splitted_y_list[1]) + 1
        lower_x = int(splitted_x_list[0])
        upper_x = int(splitted_x_list[1]) + 1
        # construct a polygon from 4 (+1 closing the ring) points we can build from the separate coordinates
        lower_left_corner = (lower_y, lower_x)
        lower_right_corner = (lower_y, upper_x)
        upper_right_corner = (upper_y, upper_x)
        upper_left_corner = (upper_y, lower_x)
        poly = Polygon([lower_left_corner, lower_right_corner, upper_right_corner, upper_left_corner, lower_left_corner])
        # return the polygon geometry
        return poly


We create this slightly more elaborate function in order to create the polygons out of the square-ish String coordinate pairs.

.. ipython:: python

    df['geometry'] = df.apply(construct_poly, axis=1)
    df.head()


We create a geodataframe from our dataframe using the Estonian national projected coordinate system.

.. ipython:: python

    from fiona.crs import from_epsg
    # we create a geodataframe from our dataframe using the Estonian national projected coordinate system
    gdf_3301_poly = gpd.GeoDataFrame(df, geometry='geometry', crs=from_epsg(3301))
    # we'll also calculate the area
    gdf_3301_poly['area_m2'] = gdf_3301_poly.geometry.area
    gdf_3301_poly.head()


.. ipython:: python

    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    plt.rcParams['figure.figsize'] = (10, 7)
    plt.rcParams['font.family'] = 'sans-serif'
    gdf_3301_poly.plot()
    @savefig crime-grid-3301_poly.png width=7in
    plt.tight_layout()

.. image:: ../../_static/crime-grid-3301_poly.png


Then we convert L-EST to WGS84 (lon-lat), because the map plugin for gmaps will need lat lon coordinates (not projected).
And because we will need points and not polygons for the heatmap, we calculate the centroid with a simple GeoDataframe function.

.. ipython:: python

    # convert L-EST to WGS84 (lon-lat), because the map plugon for gmaps will need lat lon coordinates (not projected)
    gdf_wgs84_poly = gdf_3301_poly.to_crs(epsg=4326)
    # and because we will need points and not polygons for the heatmap, we calculate the centroid with a simple GeoDataframe function
    gdf_wgs84_poly['centroids'] = gdf_wgs84_poly.centroid
    gdf_wgs84_poly.head()


Some final steps before we can use the data for the ``gmaps`` heatmap function: We are required to provide a distinct list of lat/lon coordinate pairs and make sure there are no empty or NaN fields.
As we have centroids already prepared, we will clean the remaining dataframe and split the lat/lon fields off our centroids. Let's prepare a simple function:

.. ipython:: python

    def split_lat_lon(row):
        centerp = row['centroids']
        new_row = row
        new_row['lat'] = centerp.y
        new_row['lon'] = centerp.x
        return row

And apply the function, and drop NaN fields along desired columns:

.. ipython:: python

    gdf_wgs84_poly = gdf_wgs84_poly.apply(split_lat_lon, axis=1)
    gdf_wgs84_poly.head()


A quick statistical look at the data
------------------------------------

Let's define a few functions to sort out the month, the day of the week and the hour of the event time, as well as extracting the costs of damage into separate columns.
This is always practical and helps us separating concerns we want to investigate in.

Python has a builtin ``datatime`` package which makes it easier for us to work with dates and times and converting between Strings (textual representation) and real chronological dat and time objects.

.. ipython:: python

    from datetime import datetime
    #
    noNanData = gdf_wgs84_poly.dropna(how = 'any', subset = ['ToimKell','ToimKpv','Kahjusumma','lon', 'lat','geometry']).copy()
    #
    def getMonths(item):
        datetime_str = item
        datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d')
        return datetime_object.month
    #
    def getWeekdays(item):
        datetime_str = item
        datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d')
        return datetime_object.weekday()
    #
    def getHours(item):
        datetime_str = item
        datetime_object = datetime.strptime(datetime_str, '%H:%M')
        return datetime_object.hour
    #
    def getDamageCosts(item):
        try:
            lst_spl = item.split("-")
            lst_int = [int(i) for i in lst_spl]
            value = max(lst_int)
            return value
        except:
            return np.nan


Then we apply the functions and create additional columns.


.. ipython:: python

    #
    noNanData['month'] = noNanData['ToimKpv'].map(lambda x: getMonths(x))
    #
    noNanData['dayOfWeek'] = noNanData['ToimKpv'].map(lambda x: getWeekdays(x))
    #
    noNanData['hour'] = noNanData['ToimKell'].map(lambda x: getHours(x))
    #
    noNanData['costs'] = noNanData['Kahjusumma'].map(lambda x: getDamageCosts(x))
    #
    print(noNanData.shape)
    #
    noNanData.head()


And then we can plot some different distributions of **when** the crimes happened...

.. ipython:: python

    noNanData.groupby('month').size().plot(kind='bar', color='blue')
    plt.title("crimes distribution per month")
    @savefig crime-by-month.png width=7in
    plt.tight_layout()

.. image:: ../../_static/crime-by-month.png


.. ipython:: python

    print('Monday is 0 and Sunday is 6')
    noNanData.groupby('dayOfWeek').size().plot(kind='bar', color='red')
    plt.title("crimes distribution per day of the week")
    @savefig crime-by-dayofweek.png width=7in
    plt.tight_layout()

.. image:: ../../_static/crime-by-dayofweek.png


.. ipython:: python

    noNanData.groupby('hour').size().plot(kind='bar', color='purple')
    plt.title("crimes distribution per hour of the day")
    @savefig crime-by-hourly.png width=7in
    plt.tight_layout()

.. image:: ../../_static/crime-by-hourly.png

... and what

.. ipython:: python

    noNanData["costs"].plot.hist(bins=100, color='green')
    plt.title("crimes distribution per damage costs")
    @savefig crime-costs-histogram.png width=7in
    plt.tight_layout()

.. image:: ../../_static/crime-costs-histogram.png


Creating the Heatmap
--------------------

Base configuration:

Most operations on Google Maps require that you tell Google who you are.


.. admonition:: API key note

    For the lesson we will provide an API key in Moodle!

To authenticate with Google Maps, follow `the instructions <https://console.developers.google.com/flows/enableapi?apiid=maps_backend,geocoding_backend,directions_backend,distance_matrix_backend,elevation_backend&keyType=CLIENT_SIDE&reusekey=true>`_ for creating an API key.
You will probably want to create a new project, then click on the Credentials section and create a Browser key.
The API key is a string that starts with the letters AI.

.. code::

    import gmaps
    # INPUTS
    # Google API key of Alex
    GOOGLE_API_KEY = 'xxx-code goes here'
    #
    gmaps.configure(api_key=GOOGLE_API_KEY)

Maps and layers created after the call to gmaps.configure will have access to the API key.

.. note::

    A very good tutorial can be found `on their website <https://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html>`_.


``gmaps`` is built around the idea of adding layers to a base map. After you’ve authenticated with Google maps, you start by creating a figure,
which contains a base map and adding a list of coordinates as layer.


.. code::

    fig = gmaps.figure()

    # gmaps.figure(map_type='HYBRID')
    # gmaps.figure(map_type='TERRAIN')

    # example_parameters
    # 'city' is static and for close-up views, 'county' (default) is dissipating
    #
    # 'city': 'point_radius': 0.0075, 'max_intensity': 150, 'dissipating': False}
    # 'county': {'point_radius': 29, 'max_intensity': 150, 'dissipating': True}

    locations = noNanData[['lat', 'lon']]

    heatmap_layer = gmaps.heatmap_layer(locations, point_radius=29, max_intensity=150, dissipating=True )
    # heatmap_layer = gmaps.heatmap_layer(locations)

    fig.add_layer(heatmap_layer)
    fig


Preventing dissipation on zoom If you zoom in sufficiently, you will notice that individual points disappear.
You can prevent this from happening by controlling the max_intensity setting. This caps off the maximum peak intensity.
It is useful if your data is strongly peaked. This settings is None by default, which implies no capping.
Typically, when setting the maximum intensity, you also want to set the point_radius setting to a fairly low value.
The only good way to find reasonable values for these settings is to tweak them until you have a map that you are happy with.

.. code::

    heatmap_layer.max_intensity = 100
    heatmap_layer.point_radius = 5
    fig.add_layer(heatmap_layer)
    fig

Setting the color gradient and opacity You can set the color gradient of the map by passing in a list of colors.
Google maps will interpolate linearly between those colors. You can represent a color as a string denoting the color (the colors allowed by this):

.. code::

    heatmap_layer.gradient = [
        'white',
        'silver',
        'gray'
        ]

    fig.add_layer(heatmap_layer)
    fig

If you need more flexibility wit hsize and colour, you can try several of the `more configuration options <https://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html#setting-the-color-gradient-and-opacity>`_ in the tutorial.


Weighted Heatmaps
-----------------

By default, heatmaps assume that every row is of equal importance.
You can override this by passing weights through the weights keyword argument.
The weights array is an iterable (e.g. a Python list or a Numpy array) or a single pandas series.
Weights must all be positive (this is a limitation in Google maps itself).

https://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html#weighted-heatmaps

.. code::

    fig = gmaps.figure()
    heatmap_layer = gmaps.heatmap_layer(
        noNanData[['lat', 'lon']], weights=noNanData['costs'],
        max_intensity=30, point_radius=3.0
    )
    fig.add_layer(heatmap_layer)
    fig