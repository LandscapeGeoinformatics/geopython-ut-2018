Lesson 5 Overview
=================

This lesson we will focus on learning how to create beautiful maps in Python with different levels of interactivity and modes of presentation.

1. :doc:`Static maps <static-maps>`
2. :doc:`Interactive maps with bokeh <interactive-map-bokeh>`
3. :doc:`Interactive Leaflet maps with Folium <interactive-map-folium>`
4. :doc:`Exercise 5 <ex-5>`
5. :doc:`Exercise 5 hints <exercise-5-hints>`
5. :doc:`Examples 2018 <examples_2018>`

.. commented_out:
    2.1 :doc:`Advanced map features in bokeh <advanced-bokeh>`
    4. :doc:`Sharing interactive maps on GitHub <share-on-github>`


There are many different Python modules that can be used for making visualizations. And many of them allows you to create also different kinds of maps. During this lesson we will focus on few of them, namely:

 - `Matplotlib <http://matplotlib.org/>`_ (static maps, integrated into `Geopandas <http://geopandas.org/>`_)
 - `Bokeh <http://bokeh.pydata.org/en/latest/>`_ (interactive plots)
 - `Folium <https://github.com/python-visualization/folium>`_ (interactive Web maps on Leaflet)

In addition to these modules, there are also several good and interesting other modules for making maps that we will NOT cover, but we mention them if you like to investigate by yourself later on:

 - `mplleaflet <https://github.com/jwass/mplleaflet>`_ (converts Matplotlib plots easily to interactive Leaflet maps)
 - `Basemap <http://matplotlib.org/basemap/index.html>`_ (Matplotlib's own mapping module)
 - `Cartopy <https://scitools.org.uk/cartopy/docs/latest/>`_ (The Cartopy project will replace Basemap, but it hasn’t yet implemented all of Basemap’s features.)
 - `GeoViews <http://geo.holoviews.org/>`_

Learning goals
--------------

After this lessons lesson you should be able to (at least):

 - Create a static map using Geopandas (using the integrated matplotlib module)
 - Create a simple interactive map using Bokeh
 - Create a simple interactive web map using Folium (using the LeafletJS JavaScript web map library).


Sources
-------

Following materials are partly based on documentation of `Geopandas <http://geopandas.org/geocoding.html>`_, `Matplotlib <http://matplotlib.org/>`_,
`Bokeh <http://bokeh.pydata.org/en/latest/>`_, and `Folium <https://github.com/python-visualization/folium>`_.

The lesson reuses materials from Henrikki Tenkanen from the University of Helsinki, under CC-BY-SA from `from AutoGIS GitHub repository <https://github.com/Automating-GIS-processes/2017>`_.
